# Gui
this is a gui
# run
# --standalone: 创建一个独立的可执行文件，包含所有的依赖项，以便在没有 Python 环境的情况下运行。
# --enable-plugin=pyqt5: 启用 PyQt5 插件，以确保正确处理 PyQt5 库及其依赖项
# --output-dir=output: 指定输出目录为 output，打包后的文件将放在这个目录中。
# --windows-disable-console: 禁用控制台窗口（适用于 Windows)
# --windows-icon-from-ico="D:\Gui\Tool_Gui\data\powerful.ico" 指定生成的可执行文件的图标



nuitka --standalone --enable-plugin=pyqt5 --output-dir=output  --include-data-dir="D:\Gui\.venv\Lib\site-packages\PyQt5\Qt5\resources=PyQt5\Qt5\resources"  --inc
lude-data-dir="D:\Gui\.venv\Lib\site-packages\PyQt5\bindings\QtWebEngine=PyQt5\bindings\QtWebEngine" --include-data-dir="D:\Gui\Tool_Gui\data=data" --windows-disable-console --windows-icon-from-ico="D:\Gui\Tool_Gui\data\powerful.ico" new_gui.py

# Dependency library
pip install PyQt5
pip install PyQtWebEngine
pip install folium
pip install pyqt5-tools
pip install nuitka
# 创建虚拟环境 "C:\Program Files\Python311\python.exe" -m venv venv
# 激活虚拟环境 venv\Scripts\activate
# 安装项目依赖项 pip install -r requirements.txt
