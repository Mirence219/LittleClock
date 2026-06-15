# LittleClock —— 桌面时钟小组件

---

# ⏱️极简风格桌面时钟小组件

一款基于 Python + PySide6 开发的**极简现代化风格桌面悬浮小组件**，采用实体数码灯管UI设计，通透干净透明无框窗口，轻量化常驻桌面，简约高级、无多余后台负担。

**当前版本说明(v1.1.1)：**
正式稳定可用版本，目前仅实现显示系统时间，但是已满足日常交互需求，开箱即用。

---

## 📝 v1.1.1 更新日志（最新）
1. 支持最小化至系统托盘后台驻留，点击托盘图标一键恢复窗口，右键图标可打开菜单退出LittleClock；
2. 移除任务栏图标，运行时不在系统任务栏展示程序标识；
3. 新增窗口置顶功能，时钟固定悬浮顶层；
4. LittleClock启动时自动定位至屏幕右上角；
5. LittleClock升级为工具窗口，不在 `Alt+Tab` / `Win+Tab` 窗口切换中显示，不受 `Win+D` / `Win+M` 影响；
6. 优化LittleClock进程退出逻辑。

## ✨ 项目特点
### 性能轻量化
- **极低资源占用**
打包后 Windows 平台常驻内存仅约 20MB，日常待机 CPU 占用稳定低于 0.1%，几乎不占用硬件性能；在虚拟内存作用下内存占用可低至 10MB 以内。
- **高效渲染刷新**
仅局部重绘变化灯管数字，减少全局UI刷新，界面流畅无卡顿。

### 现代化窗口
- 透明无边框设计，无标题栏，和桌面壁纸完美融合；
- 启动自动吸附屏幕右上角，无需手动摆放；
- 支持窗口置顶，时钟永久悬浮所有窗口上层；
- 最小化至系统托盘，后台静默运行；

### 布局适配
窗口尺寸自适应，数码灯管自动居中重绘，适配各类桌面分辨率与布局。

---

## 🚀 运行方式
### 1. 直接获取成品程序（推荐普通用户）
前往 [`Releases`](https://github.com/Mirence219/LittleClock/releases) 下载打包好的可执行文件
> **☞ 直达稳定版：** [`LittleClock v1.1.1`](https://github.com/Mirence219/LittleClock/releases/tag/v1.1.1)

### 2. 源码运行（开发 / 二次调试）
```bash
# 安装依赖
pip install pyside6

# 启动程序
python __main__.py
```

### 3. PyInstaller 打包
```bash
#Windows打包（.exe）
pyinstaller --onefile --windowed --name LittleClock --clean --add-data "assets;assets" __main__.py
```
```bash
#Linux打包（.bin）
pyinstaller --onefile --noconsole --name LittleClock.bin --clean --add-data "assets:assets" __main__.py
```
打包产物在 `dist` 文件夹，双击 `LittleClock.exe`/`LittleClock.bin` 即可独立运行。

---

## 📊 资源占用（v1.1.1 稳定版）
|运行平台|启动峰值内存|长期待机内存|
|---|---|---|
|Windows|≈45 MB|≈20 MB|
|Linux|≈110 MB|30MB ~ 110MB|
>补充说明：Linux 平台受 X11 图形缓存机制影响，内存会周期性小幅波动，属于系统正常特性，不影响使用。

---

