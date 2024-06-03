# Gui
this is a gui
# run
nuitka --standalone --enable-plugin=pyqt5 --output-dir=output  --include-data-dir="D:\Gui\.venv\Lib\site-packages\PyQt5\Qt5\resources=PyQt5\Qt5\resources"  --inc
lude-data-dir="D:\Gui\.venv\Lib\site-packages\PyQt5\bindings\QtWebEngine=PyQt5\bindings\QtWebEngine" --include-data-dir="D:\Gui\Tool_Gui\data=data" --windows-disable-console --windows-icon-from-ico="D:\Gui\Tool_Gui\data\powerful.ico" new_gui.py

# Dependency library
pip install PyQt5
pip install PyQtWebEngine
pip install folium
pip install pyqt5-tools

pip install nuitka