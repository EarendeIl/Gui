import logging
import os.path
import subprocess
import sys
import re  # 正则表达式模块，用于解析ADB命令的输出
import time
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtGui import QImage, QTextCursor
from matplotlib.ticker import MaxNLocator
from gui_code import UiMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from btn_operate import Btn_Operate
import threading
from PyQt5.QtCore import QTimer

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, 'data')
start_path = os.path.join(data_dir, 'start1.png')
stop_path = os.path.join(data_dir, 'stop.png')


class MainWindows(QMainWindow, UiMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.selected_app = None
        self.app_package = None
        self.install_line_edit = ""
        self.pull_one = ""
        self.pull_two = ""
        self.push_two = ""
        self.push_one = ""
        self.cmd1 = ""
        self.setupUi(self)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.thread_update_timer)
        self.start_time = QTime()
        self.result = True
        self.start = True
        self.btn_operate = Btn_Operate()
        self.timer3 = QTimer(self)
        self.timer3.timeout.connect(
            lambda: self.thread_refresh1(refresh1="adb devices"))
        self.timer3.start(1000)
        # 当Btn_Operate中的output_signal信号被触发时，将输出的内容传递给update_text槽函数，从而更新文本显示的内容
        self.btn_operate.output_signal.connect(self.update_text)
        self.btn_operate.cmd_signal.connect(self.clear_cmd)
        self.btn_operate.adb_refresh1.connect(self.devices_box)
        self.btn_operate.adb_refresh2.connect(self.app_list)
        self.btn_operate.devices1.connect(self.devices_value)
        # 连接输入框的 textChanged 信号到槽函数,每当输入框中的文本发生变化时，它会发出信号
        self.Enter_Edit.textChanged.connect(self.update_cmd1)
        self.pull_edit_one.textChanged.connect(self.pull_line_one)
        self.pull_edit_two.textChanged.connect(self.pull_line_two)
        self.push_edit_one.textChanged.connect(self.push_line_one)
        self.push_edit_two.textChanged.connect(self.push_line_two)
        self.install_edit.textChanged.connect(self.install_line)
        # 设置tools按钮为默认选中状态
        self.tools.setChecked(True)
        # 设置高德地图默认选中状态
        self.radioButton.setChecked(True)
        # 设置textEdit为只读状态
        self.textEdit.setReadOnly(True)
        # 设置文本交互标志，以允许键盘和鼠标选择文本
        self.textEdit.setTextInteractionFlags(
            self.textEdit.textInteractionFlags() | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        self.tools.clicked.connect(self.btn_clicked)
        self.bug.clicked.connect(self.btn_clicked)
        self.perf.clicked.connect(self.btn_clicked)
        self.map.clicked.connect(self.btn_clicked)
        self.report.clicked.connect(self.btn_clicked)
        self.other.clicked.connect(self.btn_clicked)
        self.radioButton.clicked.connect(self.Map_select)
        self.radioButton_2.clicked.connect(self.Map_select)
        self.perf_window.start_btn.setDisabled(True)
        self.tools.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.tools_page))
        self.bug.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.bug_reporting_page))
        self.perf.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.performance_page))
        self.map.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.map_functions_page))
        self.report.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.reports_page))
        self.other.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.other_page))

    def btn_shell_clicked(self):
        # 清空textEdit内容
        self.clear_info.clicked.connect(self.textEdit.clear)
        # 打开高德地图
        self.open_gaode.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am start -n com.autonavi.amapauto/com.autonavi.amapauto.activity.StartupActivity"))
        # 关闭高德地图
        self.close_gaode.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am force-stop com.autonavi.amapauto"))
        # 卸载高德地图
        self.uninstall_gaode.clicked.connect(lambda: self.btn_thread(
            cmd="adb uninstall com.autonavi.amapauto"))
        # 打开腾讯地图
        self.open_tencent.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am start -n com.tencent.wecarnavi/com.autonavi.amapauto.activity.StartupActivity"))
        # 关闭腾讯地图
        self.close_tencent.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am force-stop com.tencent.wecarnavi"))
        # 卸载腾讯地图
        self.uninstall_tencent.clicked.connect(lambda: self.btn_thread(
            cmd="adb uninstall com.tencent.wecarnavi"))
        # 打开AUTO助手
        self.open_auto.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am start com.autonavi.amapauto.autohelper/com.alipay.hulu.activity.SplashActivity"))
        # 关闭AUTO助手
        self.close_auto.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am force-stop com.autonavi.amapauto.autohelper"))
        # 打开屏幕指针
        self.open_point.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell settings put system pointer_location 1"))
        # 关闭屏幕指针
        self.close_point.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell settings put system pointer_location 0"))
        # 打开Wi-Fi
        self.open_wifi_2.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell svc wifi enable"))
        # 关闭Wi-Fi
        self.close_wifi_2.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell svc wifi disable"))
        # ADB LOGCAT
        self.open_logcat_2.clicked.connect(lambda: self.logcat_thread())
        # 停止抓取LOGCAT
        self.close_logcat_2.clicked.connect(lambda: self.btn_operate.kill_logcat_pid())
        # 进入安卓原生设置
        self.setting_2.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell am start com.android.settings/com.android.settings.Settings"))
        # ADB ROOT
        self.root.clicked.connect(lambda: self.btn_thread(
            cmd="adb root"))
        # ADB DISABLE VERITY
        self.verity.clicked.connect(lambda: self.btn_thread(
            cmd="adb disable-verity"))
        # ADB REBOOT
        self.reboot.clicked.connect(lambda: self.btn_thread(
            cmd="adb reboot"))
        # ADB REMOUNT
        self.remount.clicked.connect(lambda: self.btn_thread(
            cmd="adb remount"))
        # ADB ClEAR
        self.devices.clicked.connect(lambda: self.btn_thread(
            cmd="adb shell pm clear {}".format(self.app_package)))
        # ADB TCPIP
        self.tcpip.clicked.connect(lambda: self.btn_thread(
            cmd="adb tcpip 5555"))
        # MONKEY
        self.monkey.clicked.connect(lambda: self.Monkey_Start())
        # MONKEY_Stop
        self.stop.clicked.connect(lambda: self.Monkey_Stop())
        # PULL
        self.pull.clicked.connect(lambda: self.btn_thread(cmd="adb pull {} {}".format(self.pull_one, self.pull_two)))
        # PUSH
        self.push.clicked.connect(lambda: self.btn_thread(cmd="adb push {} {}".format(self.push_one, self.push_two)))
        # INSTALL
        self.install.clicked.connect(lambda: self.btn_thread(cmd=f"adb install -r -d {self.install_line_edit}"))
        # Browser_One
        self.browser_one.clicked.connect(lambda: self.browser_path(browser_btn="pull_edit_two"))
        # Browser_Two
        self.browser_two.clicked.connect(lambda: self.browser_path(browser_btn="push_edit_one"))
        # Browser_THREE
        self.browser_three.clicked.connect(lambda: self.browser_path(browser_btn="install_edit_one"))
        # refresh_devices---devices_comboBox
        self.perf_window.refresh_devices.clicked.connect(
            lambda: self.thread_refresh2(refresh2="adb shell pm list package"))
        # refresh_devices---app_comboBox
        self.perf_window.refresh_devices.clicked.connect(
            lambda: self.thread_devices_info())
        self.perf_window.start_btn.clicked.connect(lambda: self.start_icon())

    # def perf_record(self):
    def start_icon(self):
        if self.start:
            self.mem_sum = []
            self.cpu_sum = []
            self.mem_peak_max = []
            self.cpu_peak_max = []
            # 获取日志记录器实例
            self.csv = logging.getLogger()
            # 将记录器的日志级别设置为DEBUG
            self.csv.setLevel(logging.DEBUG)
            if os.path.exists(current_dir + "/perf_data"):
                pass
            else:
                os.makedirs(current_dir + "/perf_data")
            self.log_file = os.path.join(current_dir, "perf_data",
                                         time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + '.csv')
            # 创建文件处理器并设置日志级别和文件名
            self.fh = logging.FileHandler(self.log_file)
            # self.fh = logging.FileHandler(
            #     current_dir + "/perf_data/" + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + '.csv')
            self.fh.setLevel(logging.INFO)
            # 创建控制台处理器并设置日志级别
            self.ch = logging.StreamHandler()
            self.ch.setLevel(logging.INFO)
            # 创建日志格式器，默认格式为空
            formatter = logging.Formatter()
            # 将格式器设置到控制台处理器上
            self.ch.setFormatter(formatter)
            # 将格式器设置到文件处理器上
            self.fh.setFormatter(formatter)
            # 添加处理器到日志记录器
            self.csv.addHandler(self.ch)
            self.csv.addHandler(self.fh)
            # 设置表格（日志文件）的列名
            bt = "'Time', 'device info', 'package', 'MEM Usage', 'MEM Peak', 'CPU Usage', 'CPU Peak'".replace("'", "")
            self.csv.info(bt)
            self.start_time = QTime.currentTime()
            stop_icon = QtGui.QIcon()
            stop_icon.addPixmap(QtGui.QPixmap(stop_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.perf_window.start_btn.setIcon(stop_icon)
            self.perf_window.refresh_devices.setDisabled(True)
            self.perf_window.app_comboBox.setDisabled(True)
            self.perf_window.devices_comboBox.setDisabled(True)
            threading.Thread(target=self.cpu_time_info()).start()
            threading.Thread(target=self.mem_time_info()).start()
            threading.Thread(target=self.timer2.start(1000)).start()
        else:
            start_icon = QtGui.QIcon()
            start_icon.addPixmap(QtGui.QPixmap(start_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.perf_window.start_btn.setIcon(start_icon)
            self.timer.stop()
            self.timer1.stop()
            self.timer2.stop()
            self.read_file(self.log_file)
            self.ch.close()  # 关闭控制台处理器
            self.fh.close()  # 关闭文件处理器
            self.csv.removeHandler(self.ch)  # 移除控制台处理器
            self.csv.removeHandler(self.fh)  # 移除文件处理器
            self.perf_window.refresh_devices.setDisabled(False)
            self.perf_window.app_comboBox.setDisabled(False)
            self.perf_window.devices_comboBox.setDisabled(False)
        self.start = not self.start

    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as files:
                file = files.readlines()[1:]
                count = len(file)
                for i in file:
                    self.mem_sum.append(i.strip("'").split(',')[3].replace(' ', ''))
                    self.mem_peak_max.append(i.strip("'").split(',')[4].replace(' ', ''))
                    self.cpu_sum.append(i.strip("'").split(',')[5].replace(' ', ''))
                    self.cpu_peak_max.append(i.strip("'").split(',')[6].replace(' ', ''))
                mem_average = sum(list(map(float, self.mem_sum))) / count
                mem_average_peak = max(list(map(float, self.mem_peak_max)))
                cpu_average = sum(list(map(float, self.cpu_sum))) / count
                cpu_average_peak = max(list(map(float, self.cpu_peak_max)))
                sum_average = {
                    'Time': 'Total',
                    'device info': '',
                    'package': '',
                    'MEM average': '{:.2f}'.format(mem_average),
                    'MEM Peak': '{:.2f}'.format(mem_average_peak),
                    'CPU average': '{:.2f}'.format(cpu_average),
                    'CPU Peak': '{:.2f}'.format(cpu_average_peak),
                }
                average = str(list(sum_average.values())).replace("[", "").replace("]", "")
                self.csv.info(average.replace("'", ""))
        except Exception as e:
            print(e)

    def thread_refresh1(self, refresh1):
        thread = threading.Thread(target=self.btn_operate.box_refresh1,
                                  kwargs={"refresh1": refresh1})
        thread.start()

    def thread_refresh2(self, refresh2):
        threading.Thread(target=self.btn_operate.box_refresh2, kwargs={'refresh2': refresh2}).start()

    def thread_devices_info(self):
        thread = threading.Thread(target=self.btn_operate.devices_info)
        thread.start()

    def cmd_operate(self):
        self.Enter.clicked.connect(lambda: self.adb_shell_thread())
        # returnPressed  是 PyQt 中 QLineEdit 控件的一个信号,这个信号会在用户在 QLineEdit 中按下回车键（即 Enter 键）时发出
        self.Enter_Edit.returnPressed.connect(lambda: self.adb_shell_thread())

    def browser_path(self, browser_btn):
        """
        QFileDialog.getOpenFileName是一个静态方法，它接受的参数
        self - 表示父窗口，也就是FileSelector实例
        "Select File" - 对话框的标题
        " " - 初始目录，设置对话框打开时显示在特定目录
        "All Files (*);;Python Files (*.py)" - 文件过滤器
        options = options - 传递之前创建的选项对象，确保对话框使用设置的选项
        这行代码返回两个值：fileName和_。fileName是用户选择的文件的路径，_是一个占位符
        """
        # 创建QFileDialog.Options对象，包含了关于文件对话框的选项
        options = QFileDialog.Options()
        if browser_btn == "pull_edit_two":
            dirs_path = QFileDialog.getExistingDirectory(self, "Select Dirs", "", options=options)
            if dirs_path:
                self.pull_edit_two.setText(dirs_path)
        if browser_btn == "push_edit_one":
            files_path, _ = QFileDialog.getOpenFileName(self, "Select Files", "",
                                                        "apk (*.apk), APK(*.APK);;All Files (*)", options=options)
            if files_path:
                self.push_edit_one.setText(files_path)

        if browser_btn == "install_edit_one":
            install_path, _ = QFileDialog.getOpenFileName(self, "Select Files", "",
                                                          "apk (*.apk), APK(*.APK);;All Files (*)", options=options)
            if install_path:
                self.install_edit.setText(install_path)

    def pull_line_one(self, text):
        # 更新self.pull_one
        self.pull_one = text

    def pull_line_two(self, text):
        # 更新self.pull_one
        self.pull_two = text

    def push_line_one(self, text):
        # 更新self.push_one
        self.push_one = text

    def push_line_two(self, text):
        # 更新self.push_two
        self.push_two = text

    def install_line(self, text):
        # 更新self.install_edit
        self.install_line_edit = text

    def adb_shell_thread(self):
        if self.cmd1.strip() == "adb shell":
            self.textEdit.append("wo~~~~~~~~bu~~~~~~~~hui~~~~~~~~ao~~~~~~~~ao~~~~~~~~")
            # 手动滚动到底部
            self.textEdit.moveCursor(QTextCursor.End)
            # 创建了 QTextCursor 对象 控制文本插入、删除、移动
            cursor = self.textEdit.textCursor()
            # 将光标移动到文本的末尾
            cursor.movePosition(QTextCursor.End)
            image_path = "data/bb.png"
            # 创建 QImage 对象 表示图像图像
            image = QImage(image_path)
            # 检查图像是否成功加载 image.isNull() 方法用于检查图像是否为空
            if not image.isNull():
                # 将图片插入文档中
                cursor.insertImage(image)
            self.clear_cmd()
        else:
            thread = threading.Thread(target=self.btn_operate.run_shell, kwargs={"cmd1": self.cmd1, "shell": True})
            thread.start()

    def Map_select(self):
        if self.radioButton.isChecked():
            self.textEdit.append("已选择地图：高德地图；")
            self.app_package = "com.autonavi.amapauto"
        if self.radioButton_2.isChecked():
            self.textEdit.append("已选择地图：腾讯地图；")
            self.app_package = "com.tencent.wecarnavi"

    def Monkey_Start(self):
        process = subprocess.Popen("adb shell getprop ro.build.version.sdk", stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        out, err = process.communicate()
        if out:
            for self.version in out.strip().split("\n"):
                if int(self.version) >= 26:
                    self.btn_thread(
                        cmd="adb shell am start-foreground-service -a com.autonavi.amapauto.autohelper.service.monkey "
                            "-e"
                            "act start -e app {} -e runTime 9999 -e maxCrash 100".format(self.app_package))
                if int(self.version) < 26:
                    self.btn_thread(
                        cmd="adb shell am startservice -a com.autonavi.amapauto.autohelper.service.monkey -e act "
                            "start -e app {} -e runTime 9999 -e maxCrash 100".format(self.app_package))
        if err:
            self.btn_operate.output_signal.emit(err)

    def Monkey_Stop(self):
        process = subprocess.Popen("adb shell getprop ro.build.version.sdk", stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        out, err = process.communicate()
        if out:
            for self.version in out.strip().split("\n"):
                if int(self.version) >= 26:
                    self.btn_thread(
                        cmd="adb shell am start-foreground-service -a com.autonavi.amapauto.autohelper.service.monkey "
                            "-e act stop")
                if int(self.version) < 26:
                    self.btn_thread(
                        cmd="adb shell am startservice -a com.autonavi.amapauto.autohelper.service.monkey -e act stop")
        if err:
            self.btn_operate.output_signal.emit(err)

    def btn_thread(self, cmd):
        thread = threading.Thread(target=self.btn_operate.run_shell, kwargs={"cmd1": cmd})
        thread.start()

    def clear_cmd(self):
        self.Enter_Edit.setText("")

    def update_cmd1(self, text):
        # 更新 cmd1 的值
        self.cmd1 = text

    def devices_box(self, text):
        self.perf_window.devices_comboBox.clear()  # 清空现有项目
        # 解析 adb devices 的输出
        lines = text.strip().split('\n')
        for line in lines[1:]:  # 跳过第一行
            if line.strip() and 'device' in line:
                self.device = line.split()[0]
                self.perf_window.devices_comboBox.addItem(self.device)
            else:
                pass
        if self.perf_window.devices_comboBox.currentText() and self.selected_app:
            self.perf_window.start_btn.setDisabled(False)
        else:
            self.perf_window.start_btn.setDisabled(True)
            self.perf_window.app_comboBox.clear()
        if not self.start and not self.perf_window.devices_comboBox.currentText():
            self.perf_window.start_btn.setDisabled(False)
            self.timer.stop()
            self.timer1.stop()
            self.timer2.stop()
        elif not self.start and self.perf_window.devices_comboBox.currentText():
            self.perf_window.start_btn.setDisabled(False)

    def app_list(self, text):
        self.perf_window.app_comboBox.clear()
        lines = text.strip().split('\n')
        for line in lines:
            if line.strip() and 'package' in line:
                app_list1 = line.split('package:')[1]
                self.perf_window.app_comboBox.addItem(app_list1)
            else:
                pass
        self.selected_app = self.perf_window.app_comboBox.currentText()
        self.perf_window.app_comboBox.currentTextChanged.connect(self.app_name)

    def app_name(self):
        self.selected_app = self.perf_window.app_comboBox.currentText()
        # if self.selected_app:

    def logcat_thread(self):
        devices = subprocess.Popen("adb shell ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                   text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        _, err = devices.communicate()
        if "devices/emulators" and "no" in err.split():
            self.btn_operate.output_signal.emit(err)
        else:
            logtime = time.strftime('%Y-%m-%d_%H-%M-%S')
            log_path = os.path.join('D:\\logcat', f"{logtime}.log")
            self.textEdit.append("生成文件:%s" % log_path)
            # 创建一个新的线程
            thread = threading.Thread(target=self.btn_operate.catch_logcat)
            # 启动线程
            thread.start()

    def update_text(self, text):
        # 检查 textEdit 是否为空，如果不为空则插入换行符
        if not self.textEdit.toPlainText().endswith('\n'):
            self.textEdit.insertPlainText("\n")
        # 手动滚动到底部
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(text)

    def btn_clicked(self):
        # 判断当前槽函数是由哪个按钮触发的
        sender = self.sender()
        bth_list = [self.tools, self.bug, self.perf, self.map, self.report, self.other]
        for bth in bth_list:
            if bth is sender:
                bth.setChecked(True)
            elif bth is not sender:
                bth.setChecked(False)

    def devices_value(self, i, text):
        try:
            if i == 0:
                text = text.strip().split('\n')[1]
                text = text.strip().split()[0]
            if i == 1:
                self.text = text
            if i == 4:
                text = text.split(':')[-1]
                text = text.strip()
            if i == 6:
                count = text.strip().split().count("processor")
                text = str(count)
            if i == 7:
                text = text.strip().split()[1] + " KB"
            if i == 8:
                text = text.split(':')[1]
                text = text.strip()
            if i == 9:
                shell = text.strip().split()[0]
                text = shell.strip().split("(")[0].split("=")[1]
                if str(text) == "0":
                    text = "True"
                else:
                    text = "False"
            self.perf_window.devices_tableWidget.setItem(i - 1, 3, QTableWidgetItem(text))
        except Exception:
            for i in range(10):
                self.perf_window.devices_tableWidget.setItem(i - 1, 3, QTableWidgetItem(''))

    def thread_update_timer(self):
        threading.Thread(target=self.update_timer).start()

    def update_timer(self):
        elapsed_time = self.start_time.elapsed()  # Get elapsed time in milliseconds
        elapsed_seconds = elapsed_time // 1000
        hours = elapsed_seconds // 3600
        minutes = (elapsed_seconds % 3600) // 60
        seconds = elapsed_seconds % 60
        self.perf_window.time_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
        self.time_timer = f"{hours:02}:{minutes:02}:{seconds:02}"

    def mem_time_info(self):
        self.mem = []
        self.timestamps1 = []
        self.start1 = time.time()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.thread_mem)
        self.timer.start(1000)

    def cpu_time_info(self):
        self.cpu = []
        self.timestamps2 = []
        self.start2 = time.time()
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.thread_cpu)
        self.timer1.start(1000)

    def thread_mem(self):
        threading.Thread(target=self.mem_info, kwargs={"package": self.selected_app}).start()

    def thread_cpu(self):
        threading.Thread(target=self.calculate_cpu_usage, kwargs={"package": self.selected_app}).start()

    def get_mem_usage(self, package):
        try:
            process = subprocess.run(['adb', 'shell', 'dumpsys', 'meminfo', package], stderr=subprocess.PIPE, text=True,
                                     stdout=subprocess.PIPE,
                                     creationflags=subprocess.CREATE_NO_WINDOW)
            if process.returncode == 0:
                match = re.search(r'TOTAL\s+(\d+)', process.stdout)
                if match:
                    return int(match.group(1)) / 1024
                else:
                    return 0
            return None
        except Exception:
            pass

    def mem_info(self, package):
        self.mem_usage = self.get_mem_usage(package)
        if self.mem_usage is not None:
            # 将内存数值添加到列表
            self.mem.append(self.mem_usage)
            # 设置实时内存到perf_tableWidget
            self.perf_window.perf_tableWidget.setItem(1, 3, QTableWidgetItem(format(self.mem_usage, '.2f')))
            # 设置内存最大值到perf_tableWidget
            self.perf_window.perf_tableWidget.setItem(2, 3, QTableWidgetItem(format(max(self.mem), '.2f')))
            # 更新表格
            self.perf_window.perf_tableWidget.update()
            self.perf_window.mem_canvas.axes.cla()
            self.perf_window.mem_canvas.axes.set_title('MEM (MB)')
            self.perf_window.mem_canvas.axes.set_ylabel('MEM (MB)')
            self.timestamps1.append(time.time() - self.start1)
            # 格式化时间为00:00
            time1_format = ['{:d}·{:02}'.format(int(i // 60), int(i % 60)) for i in self.timestamps1]
            self.perf_window.mem_canvas.axes.plot(time1_format, self.mem, label="MEM")
            # 设置 x 轴刻度的最大数量为 8
            self.perf_window.mem_canvas.axes.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=8))

    def get_cpu_usage(self, package):
        try:
            process = subprocess.run(['adb', 'shell', 'pidof', package], stdout=subprocess.PIPE,
                                     text=True)
            pid = process.stdout.strip()
            process1 = subprocess.run('adb shell "cat /proc/stat | grep ^cpu"', stdout=subprocess.PIPE, text=True)
            cpu = process1.stdout.strip().split('\n')[0].split()[1:-3]
            # 获取CPU使用时间总和
            total_cpu = sum(list(map(int, cpu)))
            # 获取空闲的cpu时间
            idle = cpu[3]
            if pid:
                process2 = subprocess.run(f'adb shell cat /proc/{pid}/stat', stdout=subprocess.PIPE, text=True)
                cpu1 = process2.stdout.strip().split()[13:17]
                jiff = sum(list(map(int, cpu1)))
                return [total_cpu, idle, jiff]
            else:
                return [total_cpu, idle, 0]
        except Exception as e:
            print(e)

    def calculate_cpu_usage(self, package):
        total_cpu1, idle1, jiff1 = self.get_cpu_usage(package)
        total_cpu2, idle2, jiff2 = self.get_cpu_usage(package)
        self.pcpu = 100.0 * (int(jiff2) - int(jiff1)) / (int(total_cpu2) - int(total_cpu1))  # process cpu
        total_cpu1, idle1, jiff1 = total_cpu2, idle2, jiff2
        self.cpu_info()
        self.csv_info(package)

    def cpu_info(self):
        self.cpu_usage = self.pcpu
        if self.cpu_usage is not None:
            self.cpu.append(self.cpu_usage)
            self.perf_window.perf_tableWidget.setItem(-1, 3, QTableWidgetItem(format(self.pcpu, '.2f') + '%'))
            self.perf_window.perf_tableWidget.setItem(0, 3, QTableWidgetItem(format(max(self.cpu), '.2f') + '%'))
            # 强制刷新表格
            self.perf_window.perf_tableWidget.update()
            self.perf_window.cpu_canvas.axes.cla()
            self.perf_window.cpu_canvas.axes.set_title('CPU')
            self.perf_window.cpu_canvas.axes.set_ylabel('CPU (%)')
            self.timestamps2.append(time.time() - self.start2)
            self.time2_format = ['{:d}·{:02}'.format(int(i // 60), int(i % 60)) for i in self.timestamps2]
            self.perf_window.cpu_canvas.axes.plot(self.time2_format, self.cpu, label='CPU')
            # 设置 x 轴刻度的最大数量为 8
            self.perf_window.cpu_canvas.axes.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=8))
            self.perf_window.cpu_canvas.axes.legend()
            self.perf_window.mem_canvas.axes.legend()
            self.perf_window.cpu_canvas.draw()
            self.perf_window.mem_canvas.draw()

    def csv_info(self, package):
        time = self.time_timer
        device = self.text
        mem_usage = self.get_mem_usage(package)
        cpu_usage = self.pcpu
        sumdic = {'Time': time,
                  'device info': device,
                  'package': self.selected_app,
                  'MEM Usage': '{:.2f}'.format(mem_usage),
                  'MEM Peak': '{:.2f}'.format(max(self.mem)),
                  'CPU Usage': '{:.2f}'.format(cpu_usage),
                  'CPU Peak': '{:.2f}'.format(max(self.cpu)),
                  }
        list_v = str(list(sumdic.values())).replace("[", "").replace("]", "").replace("'", "")
        self.csv.info(list_v)


if __name__ == '__main__':
    # # 设置支持高分辨率屏幕自适应
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # 实例化app对象
    app = QApplication(sys.argv)
    # 实例化窗口对象
    mainWindow = MainWindows()
    mainWindow.btn_shell_clicked()
    mainWindow.cmd_operate()
    mainWindow.Map_select()
    # 设置样式表
    mainWindow.show()
    sys.exit(app.exec_())
