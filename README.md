# LittleClock —— 桌面时钟小组件

---

# ⏱️极简风格桌面时钟小组件

一款基于 Python \+ PySide6 开发的**极简现代化****风格的****桌面小组件**，采用精致实体灯管UI设计，通透干净的视觉风格，搭配透明无框窗口，轻量化常驻桌面，简约高级且无后台负担。

**当前版本说明(v1.0)：**
当前版本说明本版本为公开测试版，时钟核心功能可正常使用。目前窗口拖拽、功能设置等交互功能仍在开发完善中，后续迭代会逐步补充。

---

## ✨ 项目特点

- **低资源占用**
打包后常驻内存仅约 45MB，CPU 占用长期低于 0\.2%，后台挂着也不会影响电脑性能。

- **透明无框窗口**
窗口无标题栏，背景透明，可自由拖拽到桌面任意位置，和壁纸完美融合。

- **自适应布局**
~~窗口大小可自由调整~~，数码管会自动居中重绘，适配各种尺寸的桌面布局。

- **~~差分更新优化~~**
~~仅更新变化的灯管数据，减少不必要的 UI 刷新，让运行更流畅~~。

---

## 🚀 运行方式

### 1. 直接获取（使用）
直接前往 [`Releases`](https://github.com/Mirence219/LittleClock/releases) 页面获取安装包。

> **☞ 直达最新版：** [`LittleClock v1.0.0`](https://github.com/Mirence219/LittleClock/releases/tag/v1.0.0)
### 2\. 源码运行（开发 / 调试）

```bash
# 安装依赖
pip install pyside6
pip install pyinstaller

# 启动程序
python __main__.py
```

### 3\. 打包运行（PyInstaller）

```bash
pyinstaller --onefile --windowed --name LittleClock --clean --noconsole __main__.py
```

打包完成后，进入 `dist` 目录，双击 `LittleClock.exe` 即可启动。

---

## 📊 资源占用（v1.0）

|运行场景|峰值内存占用|长期运行内存|
|---|---|---|
|Window|≈45 MB|≈20MB|
|Linux|≈110 MB|30MB ~ 110MB|
>补充说明：Linux 平台受 X11 图形缓存机制影响，内存会在区间内周期性涨跌，属于正常平台特性。
