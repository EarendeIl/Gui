# -*- coding: utf-8 -*-
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# 获取当前脚本所在目录
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "data")
start_path = os.path.join(data_dir, "start1.png")


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Perf_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 849)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color:#F5F5F5")
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_3.setStyleSheet("background-color:white")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_btn = QtWidgets.QPushButton(self.groupBox)
        self.start_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.start_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.start_btn.setStyleSheet("QPushButton {\n"
                                     "    border-radius: 15px; /* 半径应该是按钮宽度和高度的一半 */\n"
                                     "    color: white; /* 设置字体颜色 */\n"
                                     "    min-width: 30px; /* 设置按钮的最小宽度 */\n"
                                     "    min-height: 30px; /* 设置按钮的最小高度 */\n"
                                     "    max-width: 30px; /* 设置按钮的最大宽度 */\n"
                                     "    max-height: 30px; /* 设置按钮的最大高度 */\n"
                                     "}\n"
                                     "")
        self.start_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(start_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_btn.setIcon(icon)
        self.start_btn.setIconSize(QtCore.QSize(30, 30))
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        self.time_label = QtWidgets.QLabel(self.groupBox)
        self.time_label.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                      "font-size: 10pt;")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.refresh_devices = QtWidgets.QPushButton(self.frame_3)
        self.refresh_devices.setMinimumSize(QtCore.QSize(0, 25))
        self.refresh_devices.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                           "font-size: 9pt;")
        self.refresh_devices.setObjectName("refresh_devices")
        self.horizontalLayout.addWidget(self.refresh_devices)
        self.devices_comboBox = QtWidgets.QComboBox(self.frame_3)
        self.devices_comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.devices_comboBox.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                            "font-size: 9pt;")
        self.devices_comboBox.setObjectName("devices_comboBox")
        self.horizontalLayout.addWidget(self.devices_comboBox)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.app_comboBox = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_comboBox.sizePolicy().hasHeightForWidth())
        self.app_comboBox.setSizePolicy(sizePolicy)
        self.app_comboBox.setMinimumSize(QtCore.QSize(200, 25))
        self.app_comboBox.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                        "font-size: 9pt;")
        self.app_comboBox.setObjectName("app_comboBox")
        self.verticalLayout_8.addWidget(self.app_comboBox)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                     "font-size: 8pt;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.perf_tableWidget = QtWidgets.QTableWidget(self.tab)
        self.perf_tableWidget.setEnabled(True)
        self.perf_tableWidget.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                            "font-size: 9pt;")
        self.perf_tableWidget.setAutoScrollMargin(16)
        self.perf_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.perf_tableWidget.setShowGrid(True)
        self.perf_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.perf_tableWidget.setRowCount(8)
        self.perf_tableWidget.setColumnCount(2)
        self.perf_tableWidget.setObjectName("perf_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.perf_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 191, 213))
        self.perf_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 191, 213))
        self.perf_tableWidget.setHorizontalHeaderItem(1, item)
        self.perf_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.perf_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.perf_tableWidget.horizontalHeader().setHighlightSections(True)
        self.perf_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.perf_tableWidget.verticalHeader().setVisible(False)
        self.perf_tableWidget.verticalHeader().setHighlightSections(True)
        self.perf_tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.perf_tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.perf_tableWidget.verticalHeader().setStretchLastSection(False)
        self.perf_tableWidget.setColumnWidth(0, 100)
        self.perf_tableWidget.setColumnWidth(1, 150)
        perf_list = ['CPU Usage', 'CPU Total', 'MEM Usage', 'MEM Total', 'Network', 'GPU Usage', 'GPU Total', 'FPS']
        perf_i = -1
        for perf_row in perf_list:
            perf_i = perf_i + 1
            perf_item = QTableWidgetItem(perf_row)
            # 创建的 QTableWidgetItem 对象 item 放置到表格 self.tableWidget 的指定位置 (row, 0) 中
            self.perf_tableWidget.setItem(perf_i, 0, perf_item)
        self.verticalLayout_4.addWidget(self.perf_tableWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.devices_tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.devices_tableWidget.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                               "font-size: 9pt;")
        self.devices_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.devices_tableWidget.setRowCount(10)
        self.devices_tableWidget.setColumnCount(2)
        self.devices_tableWidget.setObjectName("devices_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.devices_tableWidget.setHorizontalHeaderItem(1, item)
        self.devices_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.devices_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.devices_tableWidget.verticalHeader().setVisible(False)
        self.devices_tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.devices_tableWidget.verticalHeader().setStretchLastSection(False)
        self.devices_tableWidget.setColumnWidth(0, 100)
        self.devices_tableWidget.setColumnWidth(1, 150)
        devices_list = ["Devices Name", "Devices Model", "OS", "CPU Type", "CPU Info", "CPU Arch", "CPU CoreNum", "RAM",
                        "Resolution", "ROOT"]
        devices_i = -1
        for devices_row in devices_list:
            devices_i = devices_i + 1
            devices_item = QTableWidgetItem(devices_row)
            self.devices_tableWidget.setItem(devices_i, 0, devices_item)
        self.verticalLayout_5.addWidget(self.devices_tableWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.about_tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.about_tableWidget.setStyleSheet("font-family: Microsoft Yahei UI;\n"
                                             "font-size: 9pt;")
        self.about_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.about_tableWidget.setRowCount(10)
        self.about_tableWidget.setColumnCount(2)
        self.about_tableWidget.setObjectName("about_tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.about_tableWidget.setHorizontalHeaderItem(1, item)
        self.about_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.about_tableWidget.horizontalHeader().setHighlightSections(True)
        self.about_tableWidget.horizontalHeader().setMinimumSectionSize(34)
        self.about_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.about_tableWidget.verticalHeader().setVisible(False)
        self.about_tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.about_tableWidget.verticalHeader().setStretchLastSection(False)
        self.about_tableWidget.setColumnWidth(0, 100)
        self.about_tableWidget.setColumnWidth(1, 150)
        self.verticalLayout_6.addWidget(self.about_tableWidget)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.cpu_canvas = MplCanvas(self, width=4, height=4, dpi=100)
        self.cpu_canvas.axes.set_title('CPU')
        self.cpu_canvas.axes.set_ylabel('CPU (%)')
        self.verticalLayout_3.addWidget(self.cpu_canvas)

        self.mem_canvas = MplCanvas(self, width=4, height=4, dpi=100)
        self.mem_canvas.axes.set_title('MEM (MB)')
        self.mem_canvas.axes.set_ylabel('MEM (MB)')
        self.verticalLayout_3.addWidget(self.mem_canvas)

        self.network_canvas = MplCanvas(self, width=4, height=4, dpi=100)
        self.network_canvas.axes.set_title('NetWork')
        self.network_canvas.axes.set_ylabel('KB/S')
        self.verticalLayout_3.addWidget(self.network_canvas)

        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addWidget(self.widget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_label.setText(_translate("MainWindow", "00:00:00"))
        self.refresh_devices.setText(_translate("MainWindow", "刷新设备"))
        self.perf_tableWidget.setSortingEnabled(False)
        item = self.perf_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.perf_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Info"))
        item = self.perf_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Perf"))
        item = self.devices_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.devices_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Info"))
        item = self.devices_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Devices"))
        item = self.about_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.about_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Info"))
        item = self.about_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "About"))
