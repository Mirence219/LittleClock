#!/usr/bin/env python3
# 批量转换.ui文件为.py类文件
import os
import sys
import subprocess
from pathlib import Path

# ===================== 可配置项（根据项目修改） =====================
UI_ROOT_DIR = "assets/qt_ui"       # .ui文件根目录（会递归遍历所有子目录）
PY_OUTPUT_ROOT_DIR = "src/view/py_ui"   # .py文件输出根目录（保持原目录结构）
UIC_COMMAND = "pyside6-uic"     # pyside6-uic命令（环境变量已配则无需改）
PY_FILE_PREFIX = "ui_"          # 生成的py文件前缀（main.ui → ui_main.py）
ENCODING = "utf-8"              # 编码（解决中文路径/文件名问题）
# ====================================================================

def convert_ui_to_py(ui_file_path: Path, py_file_path: Path):
    """
    转换单个.ui文件为.py文件
    :param ui_file_path: .ui文件的绝对/相对路径
    :param py_file_path: 生成的.py文件路径
    """
    try:
        # 执行转换命令（捕获输出，支持中文）
        result = subprocess.run(
            [UIC_COMMAND, str(ui_file_path), "-o", str(py_file_path)],
            check=True,
            capture_output=True,
            text=True,
            encoding=ENCODING
        )
        return True, f"转换成功: {ui_file_path}"
    except subprocess.CalledProcessError as e:
        error_msg = f"转换失败（命令执行错误）: {e.stderr[:100]}..."
        return False, error_msg
    except FileNotFoundError:
        error_msg = f"转换失败: 未找到pyside6-uic命令，请检查环境变量"
        return False, error_msg
    except Exception as e:
        error_msg = f"转换失败（未知错误）: {str(e)[:100]}..."
        return False, error_msg

def main():
    ui_root = Path(UI_ROOT_DIR).resolve()  # 转为绝对路径
    py_output_root = Path(PY_OUTPUT_ROOT_DIR).resolve()

    # 检查UI目录是否存在
    if not ui_root.exists():
        print(f"❌ 错误：UI根目录不存在 → {ui_root}")
        sys.exit(1)

    # 确保输出目录存在
    py_output_root.mkdir(parents=True, exist_ok=True)

    # 统计信息
    total_count = 0
    success_count = 0
    fail_count = 0
    fail_list = []

    print(f"📡 开始扫描UI目录（含所有子目录）：{ui_root}")
    print("-" * 60)

    # 递归遍历所有.ui文件
    for ui_file in ui_root.rglob("*.ui"):
        total_count += 1
        
        try:
            # 关键修复：基于绝对路径计算相对路径
            relative_ui_path = ui_file.relative_to(ui_root)
        except ValueError as e:
            error_msg = f"路径错误：{ui_file} 不在 {ui_root} 目录下"
            fail_count += 1
            fail_list.append(error_msg)
            print(f"❌ {error_msg}")
            continue
        
        # 生成py文件路径（替换后缀+加前缀）
        py_file_name = f"{PY_FILE_PREFIX}{relative_ui_path.stem}.py"
        py_file_path = py_output_root / relative_ui_path.parent / py_file_name

        # 确保py文件所在目录存在
        py_file_path.parent.mkdir(parents=True, exist_ok=True)

        # 执行转换
        success, msg = convert_ui_to_py(ui_file, py_file_path)
        
        if success:
            success_count += 1
            print(f"✅ {msg} → {py_file_path}")
        else:
            fail_count += 1
            fail_list.append(msg)
            print(f"❌ {msg}")

    # 输出汇总信息
    print("-" * 60)
    print(f"📊 转换完成 | 总计：{total_count} | 成功：{success_count} | 失败：{fail_count}")
    
    if fail_list:
        print("\n❌ 失败列表：")
        for fail_msg in fail_list:
            print(f"  {fail_msg}")
    
    sys.exit(0 if fail_count == 0 else 1)

if __name__ == "__main__":
    main()