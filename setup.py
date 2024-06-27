# import sys
# import os
# from cx_Freeze import Executable
# from setuptools import setup, find_packages

"""
name: 你的包的名称。
version: 版本号。
packages: 包含要发布的包的列表，使用 find_packages() 可以自动查找。
include_package_data: 是否包含非 Python 文件，例如资源文件。如果设置为 True，package_data 字段会自动包含在安装包中。
package_data: 如果有额外的资源文件需要打包，可以在这里指定。
install_requires: 你的包依赖的其他 Python 包。
entry_points: 定义命令行入口点，例如可以将函数映射到命令行脚本。
author: 作者名字。
author_email: 作者邮箱。
description: 包的简短描述。
long_description: 包的详细描述，通常从 README.md 文件中读取。
long_description_content_type: 指定长描述的格式，通常是 Markdown。
url: 项目的 URL。
license: 授权许可。
classifiers: 包的分类标签，通常包括授权许可、支持的 Python 版本和操作系统等信息。
"""
# setup(
#     name='Perfect_Gui',
#     version='0.1',
#     packages=find_packages(),  # 自动查找所有包含 __init__.py 的目录
#     include_package_data=True,  # 自动包含非 Python 文件，例如资源文件
#     package_data={
#         # 如果有额外的资源文件需要打包，可以在这里指定
#         'Perfect_Gui': ['*.html', '*.png'],
#     },
# install_requires=[
#     'numpy',  # 依赖的其他 Python 包
#     'requests>=2.0',  # 版本要求大于等于2.0的 requests 包
# ],
# entry_points={
#     'console_scripts': [
#         'my_command = my_package.module:main_function',  # 命令行入口点
#     ],
# },
# author='Your Name',
# author_email='your.email@example.com',
# description='A short description of your package',
# long_description=open('README.md').read(),  # 从 README.md 文件中读取长描述
# long_description_content_type='text/markdown',  # 告知 PyPI 使用 Markdown 格式
# url='https://github.com/yourusername/your_package',  # 项目的 URL
# license='MIT',  # 授权许可
# classifiers=[
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3',
#     'Operating System :: OS Independent',
# ],
# )

# import sys
# import os
# from cx_Freeze import setup, Executable

# 定义要打包的资源文件
# build_exe_options = {
#     'packages': ['os', 'sys', 'time', 'threading', 'subprocess', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'],
#     'includes': ['Perfect_Gui.btn_operate', 'Perfect_Gui.gui_code'],  # 显式包括自定义模块
#     'include_files': [
#         os.path.join('Perfect_Gui', 'map_location.html'),
#         os.path.join('Perfect_Gui', 'bb.png'),
#         os.path.join('Perfect_Gui', 'bug.png'),
#         os.path.join('Perfect_Gui', 'lala.png'),
#         os.path.join('Perfect_Gui', 'map.png'),
#         os.path.join('Perfect_Gui', 'other.png'),
#         os.path.join('Perfect_Gui', 'performance.png'),
#         os.path.join('Perfect_Gui', 'powerful.png'),
#         os.path.join('Perfect_Gui', 'report.png'),
#         os.path.join('Perfect_Gui', 'tools.png'),
#         # 其他资源文件
#     ],
# }
#
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"  # 确保没有控制台窗口
#
# # 定义要生成的可执行文件
# executables = [
#     Executable(os.path.join('Perfect_Gui', 'new_gui.py'), base=base, target_name='ToolMaster.exe',
#                icon=os.path.join('Perfect_Gui', 'powerful.png'))
# ]
#
# setup(
#     name='Perfect_Gui',
#     version='0.1',
#     description='A short description of your package',
#     options={'build_exe': build_exe_options},
#     executables=executables
# )

# from distutils.core import setup
# from py2exe import freeze
#
# import sys
# import os
# from cx_Freeze import setup, Executable
# from py2exe import freeze
# import os
# # 在 new_gui.py 顶部添加导入语句
#
#
# # 确保路径正确
# script_path = os.path.join('Perfect_Gui', 'new_gui.py')
# icon_path = os.path.join('Perfect_Gui', 'powerful.ico')
#
# # 定义打包选项
# options = {
#     'includes': ['Perfect_Gui.btn_operate', 'Perfect_Gui.gui_code'],
#     'packages': ['os', 'sys', 'time', 'threading', 'subprocess', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'],
#     'bundle_files': 1,  # 1 表示将所有内容打包到一个文件中
#     'compressed': True,
#     'optimize': 2,
#     'dist_dir': 'dist',  # 输出目录
# }
#
# # 定义要生成的可执行文件和资源文件
# executables = [
#     {
#         'script': script_path,
#         'icon_resources': [(0, icon_path)],
#     }
# ]
#
# data_files = [
#     ('', [os.path.join('Perfect_Gui', 'map_location.html')]),
#     ('', [os.path.join('Perfect_Gui', 'bb.png')]),
#     ('', [os.path.join('Perfect_Gui', 'bug.png')]),
#     ('', [os.path.join('Perfect_Gui', 'lala.png')]),
#     ('', [os.path.join('Perfect_Gui', 'map.png')]),
#     ('', [os.path.join('Perfect_Gui', 'other.png')]),
#     ('', [os.path.join('Perfect_Gui', 'performance.png')]),
#     ('', [os.path.join('Perfect_Gui', 'powerful.png')]),
#     ('', [os.path.join('Perfect_Gui', 'report.png')]),
#     ('', [os.path.join('Perfect_Gui', 'tools.png')]),
# ]
#
# # 调用 freeze 函数
# freeze(
#     console=executables,
#     options={'py2exe': options},
#     data_files=data_files
# )
#
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[3])
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QTime

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_timer)
#
#         self.start_time = QTime()
#
#     def initUI(self):
#         self.layout = QVBoxLayout()
#
#         self.time_label = QLabel("00:00:00")
#         self.layout.addWidget(self.time_label)
#
#         self.start_button = QPushButton('Start Timer')
#         self.start_button.clicked.connect(self.start_timer)
#         self.layout.addWidget(self.start_button)
#
#         self.stop_button = QPushButton('Stop Timer')
#         self.stop_button.clicked.connect(self.stop_timer)
#         self.layout.addWidget(self.stop_button)
#
#         self.setLayout(self.layout)
#         self.setWindowTitle('Timer Example')
#         self.show()
#
#     def start_timer(self):
#         self.start_time = QTime.currentTime()
#         self.timer.start(1000)  # Start the timer to update every second
#
#     def stop_timer(self):
#         self.timer.stop()
#
#     def update_timer(self):
#         elapsed_time = self.start_time.elapsed()  # Get elapsed time in milliseconds
#         elapsed_seconds = elapsed_time // 1000
#         hours = elapsed_seconds // 3600
#         minutes = (elapsed_seconds % 3600) // 60
#         seconds = elapsed_seconds % 60
#         self.time_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())
#
import sys
import subprocess
import re
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memory Usage Trend')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.canvas1 = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas1.axes.set_title('MEM (MB)')
        self.canvas1.axes.set_xlabel('Time (m:ss)')
        self.canvas1.axes.set_ylabel('MEM (MB)')
        layout.addWidget(self.canvas1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.data = []
        self.timestamps = []
        self.start_time = time.time()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Update every 1 second (1000 ms)

    def update_plot(self):
        mem_usage = self.get_memory_usage()
        if mem_usage is not None:
            self.data.append(mem_usage)

            current_time = time.time() - self.start_time
            self.timestamps.append(current_time)

            plot_data = self.data[1:]
            plot_timestamps = self.timestamps[1:]

            self.canvas1.axes.clear()  # Clear the previous plot and axis settings

            self.canvas1.axes.plot(plot_timestamps, plot_data, label='Memory Usage')
            self.canvas1.axes.legend()

            # Limit the number of ticks to 5, always including the current time
            # max_ticks = 5
            # if len(plot_timestamps) > max_ticks:
            #     step = max(1, len(plot_timestamps) // (max_ticks - 1))
            #     x_ticks = plot_timestamps[::step] + [plot_timestamps[-1]]
            #     x_ticks = list(dict.fromkeys(x_ticks))  # Remove duplicates
            #     x_labels = ['{:d}:{:02}'.format(int(t // 60), int(t % 60)) for t in x_ticks]
            # else:
            x_ticks = plot_timestamps
            x_labels = ['{:d}:{:02}'.format(int(t // 60), int(t % 60)) for t in plot_timestamps]

            self.canvas1.axes.set_xticks(x_ticks)  # Set limited tick positions
            self.canvas1.axes.set_xticklabels(x_labels)  # Rotate labels to prevent overlap

            # self.canvas1.axes.set_title('MEM (MB)')
            # self.canvas1.axes.set_xlabel('Time (m:ss)')
            # self.canvas1.axes.set_ylabel('MEM (MB)')
            self.canvas1.draw()

    def get_memory_usage(self):
        try:
            result = subprocess.run(['adb', 'shell', 'dumpsys', 'meminfo', 'com.tencent.wecarnavi'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                match = re.search(r'TOTAL\s+(\d+)', result.stdout)
                if match:
                    return int(match.group(1)) / 1024  # Convert to MB
            return None
        except Exception as e:
            print(f"Error fetching memory usage: {e}")
            return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
