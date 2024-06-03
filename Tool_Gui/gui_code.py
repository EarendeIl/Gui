import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView

# 获取当前脚本所在目录
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, "data")
# 构建资源文件的相对路径
bb_path = os.path.join(data_dir, "bb.png")
bug_path = os.path.join(data_dir, "bug.png")
lala_path = os.path.join(data_dir, "lala.png")
map_path = os.path.join(data_dir, "map.png")
other_path = os.path.join(data_dir, "other.png")
performance_path = os.path.join(data_dir, "performance.png")
powerful_path = os.path.join(data_dir, "powerful.png")
report_path = os.path.join(data_dir, "report.png")
tools_path = os.path.join(data_dir, "tools.png")
map_location_path = os.path.join(data_dir, "map_location.html")


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1350, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1350, 850))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(powerful_path), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#F5F5F5")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setStyleSheet("QFrame { border: none; background-color: #FFCCDA; }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.tools = QtWidgets.QPushButton(self.frame)
        self.tools.setGeometry(QtCore.QRect(-2, -2, 282, 92))
        self.tools.setMinimumSize(QtCore.QSize(189, 70))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tools.setFont(font)
        self.tools.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tools.setStyleSheet("QPushButton {\n"
                                 "                font-family: Microsoft Yahei UI;\n"
                                 "                text-align: left;\n"
                                 "                font-size: 12pt;\n"
                                 "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                 "                font-weight: bold;\n"
                                 "                border: 2px solid #FFCCDA; /* 默认边框 */\n"
                                 "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                 "            }\n"
                                 "            QPushButton:hover {\n"
                                 "                background-color: #FFBFD5; /* 悬停时的背景色FFCCDA */\n"
                                 "            }\n"
                                 "            QPushButton:pressed {\n"
                                 "                background-color: #FEA5C3; /* 点击时的背景色 */\n"
                                 "            }\n"
                                 "            QPushButton:hover {\n"
                                 "    border-left: 0px; /* 移除左边框 */\n"
                                 "    border-right: 0px; /* 移除右边框 */\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    text-align: left; /* 使文本靠左 */\n"
                                 "    padding-left: 8px; /* 为图标腾出空间 */\n"
                                 "}"
                                 "QPushButton:checked {background-color: #FEA5C3;}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(tools_path), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.tools.setIcon(icon1)
        self.tools.setIconSize(QtCore.QSize(50, 50))
        self.tools.setCheckable(True)
        self.tools.setChecked(False)
        self.tools.setAutoDefault(False)
        self.tools.setDefault(False)
        self.tools.setObjectName("tools")
        self.bug = QtWidgets.QPushButton(self.frame)
        self.bug.setGeometry(QtCore.QRect(-2, 110, 282, 90))
        self.bug.setMinimumSize(QtCore.QSize(189, 70))
        self.bug.setStyleSheet("QPushButton {\n"
                               "                font-family: Microsoft Yahei UI;\n"
                               "                text-align: left;\n"
                               "                font-size: 12pt;\n"
                               "                background-color: #FFCCDA; /* 默认背景色 */\n"
                               "                font-weight: bold;\n"
                               "                border: 2px solid #FFCCDA; /* 默认边框 */\n"
                               "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                               "            }\n"
                               "            QPushButton:hover {\n"
                               "                background-color: #FFBFD5; /* 悬停时的背景色FFCCDA */\n"
                               "            }\n"
                               "            QPushButton:pressed {\n"
                               "                background-color: #FEA5C3; /* 点击时的背景色 */\n"
                               "            }\n"
                               "            QPushButton:hover {\n"
                               "    border-left: 0px; /* 移除左边框 */\n"
                               "    border-right: 0px; /* 移除右边框 */\n"
                               "}\n"
                               "QPushButton {\n"
                               "    text-align: left; /* 使文本靠左 */\n"
                               "    padding-left: 8px; /* 为图标腾出空间 */\n"
                               "}"
                               "QPushButton:checked {background-color: #FEA5C3;}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(bug_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bug.setIcon(icon2)
        self.bug.setIconSize(QtCore.QSize(50, 50))
        self.bug.setCheckable(True)
        self.bug.setChecked(False)
        self.bug.setObjectName("bug")
        self.perf = QtWidgets.QPushButton(self.frame)
        self.perf.setGeometry(QtCore.QRect(-2, 200, 282, 90))
        self.perf.setMinimumSize(QtCore.QSize(189, 70))
        self.perf.setStyleSheet("QPushButton {\n"
                                "                font-family: Microsoft Yahei UI;\n"
                                "                text-align: left;\n"
                                "                font-size: 12pt;\n"
                                "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                "                font-weight: bold;\n"
                                "                border: 2px solid #FFCCDA; /* 默认边框 */\n"
                                "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                "            }\n"
                                "            QPushButton:hover {\n"
                                "                background-color: #FFBFD5; /* 悬停时的背景色FFCCDA */\n"
                                "            }\n"
                                "            QPushButton:pressed {\n"
                                "                background-color: #FEA5C3; /* 点击时的背景色 */\n"
                                "            }\n"
                                "            QPushButton:hover {\n"
                                "    border-left: 0px; /* 移除左边框 */\n"
                                "    border-right: 0px; /* 移除右边框 */\n"
                                "}\n"
                                "QPushButton {\n"
                                "    text-align: left; /* 使文本靠左 */\n"
                                "    padding-left: 8px; /* 为图标腾出空间 */\n"
                                "}"
                                "QPushButton:checked {background-color: #FEA5C3;}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(performance_path), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.perf.setIcon(icon3)
        self.perf.setIconSize(QtCore.QSize(50, 50))
        self.perf.setCheckable(True)
        self.perf.setChecked(False)
        self.perf.setObjectName("perf")
        self.map = QtWidgets.QPushButton(self.frame)
        self.map.setGeometry(QtCore.QRect(-2, 310, 282, 90))
        self.map.setMinimumSize(QtCore.QSize(189, 70))
        self.map.setStyleSheet("QPushButton {\n"
                               "                font-family: Microsoft Yahei UI;\n"
                               "                text-align: left;\n"
                               "                font-size: 12pt;\n"
                               "                background-color: #FFCCDA; /* 默认背景色 */\n"
                               "                font-weight: bold;\n"
                               "                border: 2px solid #FFCCDA; /* 默认边框 */\n"
                               "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                               "            }\n"
                               "            QPushButton:hover {\n"
                               "                background-color: #FFBFD5; /* 悬停时的背景色FFCCDA */\n"
                               "            }\n"
                               "            QPushButton:pressed {\n"
                               "                background-color: #FEA5C3; /* 点击时的背景色 */\n"
                               "            }\n"
                               "            QPushButton:hover {\n"
                               "    border-left: 0px; /* 移除左边框 */\n"
                               "    border-right: 0px; /* 移除右边框 */\n"
                               "}\n"
                               "QPushButton {\n"
                               "    text-align: left; /* 使文本靠左 */\n"
                               "    padding-left: 8px; /* 为图标腾出空间 */\n"
                               "}"
                               "QPushButton:checked {background-color: #FEA5C3;}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(map_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.map.setIcon(icon4)
        self.map.setIconSize(QtCore.QSize(50, 50))
        self.map.setCheckable(True)
        self.map.setChecked(False)
        self.map.setObjectName("map")
        self.more = QtWidgets.QPushButton(self.frame)
        self.more.setGeometry(QtCore.QRect(37, 750, 200, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.more.sizePolicy().hasHeightForWidth())
        self.more.setSizePolicy(sizePolicy)
        self.more.setMinimumSize(QtCore.QSize(0, 40))
        self.more.setAutoFillBackground(False)
        self.more.setStyleSheet("QPushButton {\n"
                                "                border-radius: 20px;\n"
                                "                font-family: Microsoft Yahei UI;\n"
                                "                font-size: 12pt;\n"
                                "                font-weight: bold;\n"
                                "                background-color: #FEA5C3; /* 默认背景色 */\n"
                                "                border: 2px solid #FEA5C3; /* 默认边框 */\n"
                                "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                "            }\n"
                                "            QPushButton:hover {\n"
                                "                background-color: #FD7EB0  ; /* 悬停时的背景色 */\n"
                                "            }\n"
                                "            QPushButton:pressed {\n"
                                "                background-color: #FA57A1; /* 点击时的背景色 */\n"
                                "            }\n"
                                "")
        self.more.setObjectName("more")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 271, 1))
        self.label_2.setStyleSheet("\n"
                                   "                font-family: \"楷体\";\n"
                                   "                font-size: 8pt;\n"
                                   "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                   "                font-weight: bold;\n"
                                   "                color:#5A003E\n"
                                   "\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.report = QtWidgets.QPushButton(self.frame)
        self.report.setGeometry(QtCore.QRect(-2, 400, 282, 90))
        self.report.setMinimumSize(QtCore.QSize(189, 70))
        self.report.setStyleSheet("QPushButton {\n"
                                  "                font-family: Microsoft Yahei UI;\n"
                                  "                text-align: left;\n"
                                  "                font-size: 12pt;\n"
                                  "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                  "                font-weight: bold;\n"
                                  "                border: 2px solid #FFCCDA; /* 默认边框 */\n"
                                  "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                  "            }\n"
                                  "            QPushButton:hover {\n"
                                  "                background-color: #FFBFD5; /* 悬停时的背景色FFCCDA */\n"
                                  "            }\n"
                                  "            QPushButton:pressed {\n"
                                  "                background-color: #FEA5C3; /* 点击时的背景色 */\n"
                                  "            }\n"
                                  "            QPushButton:hover {\n"
                                  "    border-left: 0px; /* 移除左边框 */\n"
                                  "    border-right: 0px; /* 移除右边框 */\n"
                                  "}\n"
                                  "QPushButton {\n"
                                  "    text-align: left; /* 使文本靠左 */\n"
                                  "    padding-left: 8px; /* 为图标腾出空间 */\n"
                                  "}"
                                  "QPushButton:checked {background-color: #FEA5C3;}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(report_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.report.setIcon(icon5)
        self.report.setIconSize(QtCore.QSize(50, 50))
        self.report.setCheckable(True)
        self.report.setChecked(False)
        self.report.setObjectName("report")
        self.other = QtWidgets.QPushButton(self.frame)
        self.other.setGeometry(QtCore.QRect(-2, 510, 282, 90))
        self.other.setMinimumSize(QtCore.QSize(189, 70))
        self.other.setStyleSheet("QPushButton {\n"
                                 "                font-family: Microsoft Yahei UI;\n"
                                 "                text-align: left;\n"
                                 "                font-size: 12pt;\n"
                                 "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                 "                font-weight: bold;\n"
                                 "                border: 2px solid #FFCCDA; /* 默认边框 */\n"
                                 "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                 "            }\n"
                                 "            QPushButton:hover {\n"
                                 "                background-color: #FFBFD5; /* 悬停时的背景色FFCCDA */\n"
                                 "            }\n"
                                 "            QPushButton:pressed {\n"
                                 "                background-color: #FEA5C3; /* 点击时的背景色 */\n"
                                 "            }\n"
                                 "            QPushButton:hover {\n"
                                 "    border-left: 0px; /* 移除左边框 */\n"
                                 "    border-right: 0px; /* 移除右边框 */\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    text-align: left; /* 使文本靠左 */\n"
                                 "    padding-left: 8px; /* 为图标腾出空间 */\n"
                                 "}"
                                 "QPushButton:checked {background-color: #FEA5C3;}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(other_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.other.setIcon(icon6)
        self.other.setIconSize(QtCore.QSize(50, 50))
        self.other.setCheckable(True)
        self.other.setChecked(False)
        self.other.setObjectName("other")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 300, 271, 1))
        self.label.setStyleSheet("\n"
                                 "                font-family: \"楷体\";\n"
                                 "                font-size: 8pt;\n"
                                 "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                 "                font-weight: bold;\n"
                                 "                color:#5A003E\n"
                                 "\n"
                                 "")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 500, 271, 1))
        self.label_5.setStyleSheet("\n"
                                   "                font-family: \"楷体\";\n"
                                   "                font-size: 8pt;\n"
                                   "                background-color: #FFCCDA; /* 默认背景色 */\n"
                                   "                font-weight: bold;\n"
                                   "                color:#5A003E\n"
                                   "\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame)
        self.tools_page = QtWidgets.QWidget(self.centralwidget)
        self.tools_page.setStyleSheet("background-color:#F5F5F5")
        self.tools_page.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tools_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.tools_page)
        self.radioButton.setMinimumSize(QtCore.QSize(0, 39))
        self.radioButton.setMaximumSize(QtCore.QSize(16777215, 39))
        self.radioButton.setStyleSheet("QRadioButton {\n"
                                       "                font-family: Microsoft Yahei UI;\n"
                                       "\n"
                                       "        color: #FEA5C3; /* 文本颜色 */\n"
                                       "        font-size: 25px;\n"
                                       "        font-weight: bold;\n"
                                       "\n"
                                       "    }\n"
                                       "    QRadioButton::indicator {\n"
                                       "        width: 20px; /* 指示器宽度 */\n"
                                       "        height: 20px; /* 指示器高度 */\n"
                                       "        border-radius: 10px; /* 圆形指示器 */\n"
                                       "        border: 2px solid #FEA5C3; /* 指示器边框 */\n"
                                       "    }\n"
                                       "\n"
                                       "    QRadioButton::indicator:checked {\n"
                                       "        background-color: #FEA5C3; /* 指示器选中时的颜色 */\n"
                                       "    }")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tools_page)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 39))
        self.radioButton_2.setMaximumSize(QtCore.QSize(16777215, 39))
        self.radioButton_2.setStyleSheet("QRadioButton {\n"
                                         "                font-family: Microsoft Yahei UI;\n"
                                         "\n"
                                         "        color: #FEA5C3; /* 文本颜色 */\n"
                                         "        font-size: 25px;\n"
                                         "        font-weight: bold;\n"
                                         "\n"
                                         "    }\n"
                                         "    QRadioButton::indicator {\n"
                                         "        width: 20px; /* 指示器宽度 */\n"
                                         "        height: 20px; /* 指示器高度 */\n"
                                         "        border-radius: 10px; /* 圆形指示器 */\n"
                                         "        border: 2px solid #FEA5C3; /* 指示器边框 */\n"
                                         "    }\n"
                                         "\n"
                                         "    QRadioButton::indicator:checked {\n"
                                         "        background-color: #FEA5C3; /* 指示器选中时的颜色 */\n"
                                         "    }")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.clear_info = QtWidgets.QPushButton(self.tools_page)
        self.clear_info.setMinimumSize(QtCore.QSize(250, 45))
        self.clear_info.setMaximumSize(QtCore.QSize(16777215, 45))
        self.clear_info.setStyleSheet("QPushButton {\n"
                                      "                font-family: Microsoft Yahei UI;\n"
                                      "font-size: 16px;\n"
                                      "                border-radius: 8px;\n"
                                      "\n"
                                      "                background-color: #FEA5C3; /* 默认背景色 */\n"
                                      "                border: 2px solid #FEA5C3; /* 默认边框 */\n"
                                      "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                      "            }\n"
                                      "            QPushButton:hover {\n"
                                      "                background-color: #FD7EB0; /* 悬停时的背景色 */\n"
                                      "            }\n"
                                      "            QPushButton:pressed {\n"
                                      "                background-color: #FA57A1; /* 点击时的背景色 */\n"
                                      "            }")
        self.clear_info.setObjectName("clear_info")
        self.horizontalLayout_2.addWidget(self.clear_info)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_gaode = QtWidgets.QPushButton(self.tools_page)
        self.open_gaode.setMinimumSize(QtCore.QSize(0, 0))
        self.open_gaode.setMinimumSize(QtCore.QSize(0, 42))
        self.open_gaode.setMaximumSize(QtCore.QSize(16777215, 42))
        self.open_gaode.setAutoFillBackground(False)
        self.open_gaode.setStyleSheet("QPushButton {\n"
                                      "                font-family: Microsoft Yahei UI;\n"
                                      "font-size: 16px;\n"
                                      "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                      "    color: black;\n"
                                      "    border: 2px solid transparent;\n"
                                      "    border-radius: 8px;\n"
                                      "    padding: 10px 20px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                      "    border-color: #FFB6C1\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                      "    border-color: #FEA5C3\n"
                                      "}")
        self.open_gaode.setObjectName("open_gaode")
        self.horizontalLayout_3.addWidget(self.open_gaode)
        self.close_gaode = QtWidgets.QPushButton(self.tools_page)
        self.close_gaode.setMinimumSize(QtCore.QSize(0, 42))
        self.close_gaode.setMaximumSize(QtCore.QSize(16777215, 42))
        self.close_gaode.setStyleSheet("QPushButton {\n"
                                       "                font-family: Microsoft Yahei UI;\n"
                                       "font-size: 16px;\n"
                                       "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                       "    color: black;\n"
                                       "    border: 2px solid transparent;\n"
                                       "    border-radius: 8px;\n"
                                       "    padding: 10px 20px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                       "    border-color: #FFB6C1\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                       "    border-color: #FEA5C3\n"
                                       "}")
        self.close_gaode.setObjectName("close_gaode")
        self.horizontalLayout_3.addWidget(self.close_gaode)
        self.uninstall_gaode = QtWidgets.QPushButton(self.tools_page)
        self.uninstall_gaode.setMinimumSize(QtCore.QSize(0, 42))
        self.uninstall_gaode.setMaximumSize(QtCore.QSize(16777215, 42))
        self.uninstall_gaode.setStyleSheet("QPushButton {\n"
                                           "                font-family: Microsoft Yahei UI;\n"
                                           "font-size: 16px;\n"
                                           "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                           "    color: black;\n"
                                           "    border: 2px solid transparent;\n"
                                           "    border-radius: 8px;\n"
                                           "    padding: 10px 20px;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                           "    border-color: #FFB6C1\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                           "    border-color: #FEA5C3\n"
                                           "}")
        self.uninstall_gaode.setObjectName("uninstall_gaode")
        self.horizontalLayout_3.addWidget(self.uninstall_gaode)
        self.open_tencent = QtWidgets.QPushButton(self.tools_page)
        self.open_tencent.setMinimumSize(QtCore.QSize(0, 42))
        self.open_tencent.setMaximumSize(QtCore.QSize(16777215, 42))
        self.open_tencent.setStyleSheet("QPushButton {\n"
                                        "                font-family: Microsoft Yahei UI;\n"
                                        "font-size: 16px;\n"
                                        "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                        "    color: black;\n"
                                        "    border: 2px solid transparent;\n"
                                        "    border-radius: 8px;\n"
                                        "    padding: 10px 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                        "    border-color: #FFB6C1\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                        "    border-color: #FEA5C3\n"
                                        "}")
        self.open_tencent.setObjectName("open_tencent")
        self.horizontalLayout_3.addWidget(self.open_tencent)
        self.close_tencent = QtWidgets.QPushButton(self.tools_page)
        self.close_tencent.setMinimumSize(QtCore.QSize(0, 42))
        self.close_tencent.setMaximumSize(QtCore.QSize(16777215, 42))
        self.close_tencent.setStyleSheet("QPushButton {\n"
                                         "                font-family: Microsoft Yahei UI;\n"
                                         "font-size: 16px;\n"
                                         "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                         "    color: black;\n"
                                         "    border: 2px solid transparent;\n"
                                         "    border-radius: 8px;\n"
                                         "    padding: 10px 20px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                         "    border-color: #FFB6C1\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                         "    border-color: #FEA5C3\n"
                                         "}")
        self.close_tencent.setObjectName("close_tencent")
        self.horizontalLayout_3.addWidget(self.close_tencent)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uninstall_tencent = QtWidgets.QPushButton(self.tools_page)
        self.uninstall_tencent.setMinimumSize(QtCore.QSize(0, 42))
        self.uninstall_tencent.setMaximumSize(QtCore.QSize(16777215, 42))
        self.uninstall_tencent.setStyleSheet("QPushButton {\n"
                                             "                font-family: Microsoft Yahei UI;\n"
                                             "font-size: 16px;\n"
                                             "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                             "    color: black;\n"
                                             "    border: 2px solid transparent;\n"
                                             "    border-radius: 8px;\n"
                                             "    padding: 10px 20px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                             "    border-color: #FFB6C1\n"
                                             "}\n"
                                             "QPushButton:pressed {\n"
                                             "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                             "    border-color: #FEA5C3\n"
                                             "}")
        self.uninstall_tencent.setObjectName("uninstall_tencent")
        self.horizontalLayout_4.addWidget(self.uninstall_tencent)
        self.open_auto = QtWidgets.QPushButton(self.tools_page)
        self.open_auto.setMinimumSize(QtCore.QSize(0, 42))
        self.open_auto.setMaximumSize(QtCore.QSize(16777215, 42))
        self.open_auto.setStyleSheet("QPushButton {\n"
                                     "                font-family: Microsoft Yahei UI;\n"
                                     "font-size: 16px;\n"
                                     "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                     "    color: black;\n"
                                     "    border: 2px solid transparent;\n"
                                     "    border-radius: 8px;\n"
                                     "    padding: 10px 20px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                     "    border-color: #FFB6C1\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                     "    border-color: #FEA5C3\n"
                                     "}")
        self.open_auto.setObjectName("open_auto")
        self.horizontalLayout_4.addWidget(self.open_auto)
        self.close_auto = QtWidgets.QPushButton(self.tools_page)
        self.close_auto.setMinimumSize(QtCore.QSize(0, 42))
        self.close_auto.setMaximumSize(QtCore.QSize(16777215, 42))
        self.close_auto.setStyleSheet("QPushButton {\n"
                                      "                font-family: Microsoft Yahei UI;\n"
                                      "font-size: 16px;\n"
                                      "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                      "    color: black;\n"
                                      "    border: 2px solid transparent;\n"
                                      "    border-radius: 8px;\n"
                                      "    padding: 10px 20px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                      "    border-color: #FFB6C1\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                      "    border-color: #FEA5C3\n"
                                      "}")
        self.close_auto.setObjectName("close_auto")
        self.horizontalLayout_4.addWidget(self.close_auto)
        self.open_point = QtWidgets.QPushButton(self.tools_page)
        self.open_point.setMinimumSize(QtCore.QSize(0, 42))
        self.open_point.setMaximumSize(QtCore.QSize(16777215, 42))
        self.open_point.setStyleSheet("QPushButton {\n"
                                      "                font-family: Microsoft Yahei UI;\n"
                                      "font-size: 16px;\n"
                                      "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                      "    color: black;\n"
                                      "    border: 2px solid transparent;\n"
                                      "    border-radius: 8px;\n"
                                      "    padding: 10px 20px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                      "    border-color: #FFB6C1\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                      "    border-color: #FEA5C3\n"
                                      "}")
        self.open_point.setObjectName("open_point")
        self.horizontalLayout_4.addWidget(self.open_point)
        self.close_point = QtWidgets.QPushButton(self.tools_page)
        self.close_point.setMinimumSize(QtCore.QSize(0, 42))
        self.close_point.setMaximumSize(QtCore.QSize(16777215, 42))
        self.close_point.setStyleSheet("QPushButton {\n"
                                       "                font-family: Microsoft Yahei UI;\n"
                                       "font-size: 16px;\n"
                                       "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                       "    color: black;\n"
                                       "    border: 2px solid transparent;\n"
                                       "    border-radius: 8px;\n"
                                       "    padding: 10px 20px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                       "    border-color: #FFB6C1\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                       "    border-color: #FEA5C3\n"
                                       "}")
        self.close_point.setObjectName("close_point")
        self.horizontalLayout_4.addWidget(self.close_point)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.open_wifi_2 = QtWidgets.QPushButton(self.tools_page)
        self.open_wifi_2.setMinimumSize(QtCore.QSize(0, 42))
        self.open_wifi_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.open_wifi_2.setStyleSheet("QPushButton {\n"
                                       "                font-family: Microsoft Yahei UI;\n"
                                       "font-size: 16px;\n"
                                       "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                       "    color: black;\n"
                                       "    border: 2px solid transparent;\n"
                                       "    border-radius: 8px;\n"
                                       "    padding: 10px 20px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                       "    border-color: #FFB6C1\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                       "    border-color: #FEA5C3\n"
                                       "}")
        self.open_wifi_2.setObjectName("open_wifi_2")
        self.horizontalLayout_5.addWidget(self.open_wifi_2)
        self.close_wifi_2 = QtWidgets.QPushButton(self.tools_page)
        self.close_wifi_2.setMinimumSize(QtCore.QSize(0, 42))
        self.close_wifi_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.close_wifi_2.setStyleSheet("QPushButton {\n"
                                        "                font-family: Microsoft Yahei UI;\n"
                                        "font-size: 16px;\n"
                                        "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                        "    color: black;\n"
                                        "    border: 2px solid transparent;\n"
                                        "    border-radius: 8px;\n"
                                        "    padding: 10px 20px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                        "    border-color: #FFB6C1\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                        "    border-color: #FEA5C3\n"
                                        "}")
        self.close_wifi_2.setObjectName("close_wifi_2")
        self.horizontalLayout_5.addWidget(self.close_wifi_2)
        self.open_logcat_2 = QtWidgets.QPushButton(self.tools_page)
        self.open_logcat_2.setMinimumSize(QtCore.QSize(0, 42))
        self.open_logcat_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.open_logcat_2.setStyleSheet("QPushButton {\n"
                                         "                font-family: Microsoft Yahei UI;\n"
                                         "font-size: 16px;\n"
                                         "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                         "    color: black;\n"
                                         "    border: 2px solid transparent;\n"
                                         "    border-radius: 8px;\n"
                                         "    padding: 10px 20px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                         "    border-color: #FFB6C1\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                         "    border-color: #FEA5C3\n"
                                         "}")
        self.open_logcat_2.setObjectName("open_logcat_2")
        self.horizontalLayout_5.addWidget(self.open_logcat_2)
        self.close_logcat_2 = QtWidgets.QPushButton(self.tools_page)
        self.close_logcat_2.setMinimumSize(QtCore.QSize(0, 42))
        self.close_logcat_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.close_logcat_2.setStyleSheet("QPushButton {\n"
                                          "                font-family: Microsoft Yahei UI;\n"
                                          "font-size: 16px;\n"
                                          "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                          "    color: black;\n"
                                          "    border: 2px solid transparent;\n"
                                          "    border-radius: 8px;\n"
                                          "    padding: 10px 20px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                          "    border-color: #FFB6C1\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                          "    border-color: #FEA5C3\n"
                                          "}")
        self.close_logcat_2.setObjectName("close_logcat_2")
        self.horizontalLayout_5.addWidget(self.close_logcat_2)
        self.setting_2 = QtWidgets.QPushButton(self.tools_page)
        self.setting_2.setMinimumSize(QtCore.QSize(0, 42))
        self.setting_2.setMaximumSize(QtCore.QSize(16777215, 42))
        self.setting_2.setStyleSheet("QPushButton {\n"
                                     "                font-family: Microsoft Yahei UI;\n"
                                     "font-size: 16px;\n"
                                     "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                     "    color: black;\n"
                                     "    border: 2px solid transparent;\n"
                                     "    border-radius: 8px;\n"
                                     "    padding: 10px 20px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                     "    border-color: #FFB6C1\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                     "    border-color: #FEA5C3\n"
                                     "}")
        self.setting_2.setObjectName("setting_2")
        self.horizontalLayout_5.addWidget(self.setting_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.root = QtWidgets.QPushButton(self.tools_page)
        self.root.setMinimumSize(QtCore.QSize(0, 42))
        self.root.setMaximumSize(QtCore.QSize(16777215, 42))
        self.root.setStyleSheet("QPushButton {\n"
                                "                font-family: Microsoft Yahei UI;\n"
                                "font-size: 16px;\n"
                                "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                "    color: black;\n"
                                "    border: 2px solid transparent;\n"
                                "    border-radius: 8px;\n"
                                "    padding: 10px 20px;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                "    border-color: #FFB6C1\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                "    border-color: #FEA5C3\n"
                                "}")
        self.root.setObjectName("root")
        self.horizontalLayout_6.addWidget(self.root)
        self.verity = QtWidgets.QPushButton(self.tools_page)
        self.verity.setMinimumSize(QtCore.QSize(0, 42))
        self.verity.setMaximumSize(QtCore.QSize(16777215, 42))
        self.verity.setStyleSheet("QPushButton {\n"
                                  "                font-family: Microsoft Yahei UI;\n"
                                  "font-size: 16px;\n"
                                  "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                  "    color: black;\n"
                                  "    border: 2px solid transparent;\n"
                                  "    border-radius: 8px;\n"
                                  "    padding: 10px 20px;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                  "    border-color: #FFB6C1\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                  "    border-color: #FEA5C3\n"
                                  "}")
        self.verity.setObjectName("verity")
        self.horizontalLayout_6.addWidget(self.verity)
        self.reboot = QtWidgets.QPushButton(self.tools_page)
        self.reboot.setMinimumSize(QtCore.QSize(0, 42))
        self.reboot.setMaximumSize(QtCore.QSize(16777215, 42))
        self.reboot.setStyleSheet("QPushButton {\n"
                                  "                font-family: Microsoft Yahei UI;\n"
                                  "font-size: 16px;\n"
                                  "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                  "    color: black;\n"
                                  "    border: 2px solid transparent;\n"
                                  "    border-radius: 8px;\n"
                                  "    padding: 10px 20px;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                  "    border-color: #FFB6C1\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                  "    border-color: #FEA5C3\n"
                                  "}")
        self.reboot.setObjectName("reboot")
        self.horizontalLayout_6.addWidget(self.reboot)
        self.remount = QtWidgets.QPushButton(self.tools_page)
        self.remount.setMinimumSize(QtCore.QSize(0, 42))
        self.remount.setMaximumSize(QtCore.QSize(16777215, 42))
        self.remount.setStyleSheet("QPushButton {\n"
                                   "                font-family: Microsoft Yahei UI;\n"
                                   "font-size: 16px;\n"
                                   "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                   "    color: black;\n"
                                   "    border: 2px solid transparent;\n"
                                   "    border-radius: 8px;\n"
                                   "    padding: 10px 20px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                   "    border-color: #FFB6C1\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                   "    border-color: #FEA5C3\n"
                                   "}")
        self.remount.setObjectName("remount")
        self.horizontalLayout_6.addWidget(self.remount)
        self.devices = QtWidgets.QPushButton(self.tools_page)
        self.devices.setMinimumSize(QtCore.QSize(0, 42))
        self.devices.setMaximumSize(QtCore.QSize(16777215, 42))
        self.devices.setStyleSheet("QPushButton {\n"
                                   "                font-family: Microsoft Yahei UI;\n"
                                   "font-size: 16px;\n"
                                   "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                   "    color: black;\n"
                                   "    border: 2px solid transparent;\n"
                                   "    border-radius: 8px;\n"
                                   "    padding: 10px 20px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                   "    border-color: #FFB6C1\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                   "    border-color: #FEA5C3\n"
                                   "}")
        self.devices.setObjectName("devices")
        self.horizontalLayout_6.addWidget(self.devices)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tools_page)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setStyleSheet("QLabel {\n"
                                   "                font-family: Microsoft Yahei UI;\n"
                                   "        font-weight: bold;\n"
                                   "\n"
                                   "        color: #FEA5C3; /* 文本颜色 */\n"
                                   "        font-size: 15px; /* 字体大小 */\n"
                                   "    }")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tcpip = QtWidgets.QPushButton(self.tools_page)
        self.tcpip.setMinimumSize(QtCore.QSize(0, 39))
        self.tcpip.setStyleSheet("QPushButton {\n"
                                 "                    font-family: Microsoft Yahei UI;\n"
                                 "font-size: 16px;\n"
                                 "                border-radius: 8px;\n"
                                 "                background-color: #FFBFD5; /* 默认背景色 */\n"
                                 "                border: 2px solid #FFBFD5; /* 默认边框 */\n"
                                 "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                 "            }\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                 "    border-color: #FFB6C1\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                 "    border-color: #FEA5C3\n"
                                 "}")
        self.tcpip.setObjectName("tcpip")
        self.horizontalLayout_8.addWidget(self.tcpip)
        self.monkey = QtWidgets.QPushButton(self.tools_page)
        self.monkey.setMinimumSize(QtCore.QSize(0, 39))
        self.monkey.setStyleSheet("QPushButton {\n"
                                  "                    font-family: Microsoft Yahei UI;\n"
                                  "font-size: 16px;\n"
                                  "                border-radius: 8px;\n"
                                  "                background-color: #FFBFD5; /* 默认背景色 */\n"
                                  "                border: 2px solid #FFBFD5; /* 默认边框 */\n"
                                  "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                  "            }\n"
                                  "QPushButton:hover {\n"
                                  "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                  "    border-color: #FFB6C1\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                  "    border-color: #FEA5C3\n"
                                  "}")
        self.monkey.setObjectName("monkey")
        self.horizontalLayout_8.addWidget(self.monkey)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.stop = QtWidgets.QPushButton(self.tools_page)
        self.stop.setMinimumSize(QtCore.QSize(0, 39))
        self.stop.setStyleSheet("QPushButton {\n"
                                "                    font-family: Microsoft Yahei UI;\n"
                                "font-size: 16px;\n"
                                "                border-radius: 8px;\n"
                                "                background-color: #FFBFD5; /* 默认背景色 */\n"
                                "                border: 2px solid #FFBFD5; /* 默认边框 */\n"
                                "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                "            }\n"
                                "QPushButton:hover {\n"
                                "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                "    border-color: #FFB6C1\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                "    border-color: #FEA5C3\n"
                                "}")
        self.stop.setObjectName("stop")
        self.horizontalLayout_8.addWidget(self.stop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tools_page)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setStyleSheet("QLabel {\n"
                                   "                font-family: Microsoft Yahei UI;\n"
                                   "        font-weight: bold;\n"
                                   "\n"
                                   "        color: #FEA5C3; /* 文本颜色 */\n"
                                   "        font-size: 15px; /* 字体大小 */\n"
                                   "    }")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pull = QtWidgets.QPushButton(self.tools_page)
        self.pull.setMinimumSize(QtCore.QSize(168, 39))
        self.pull.setStyleSheet("QPushButton {\n"
                                "                font-family: Microsoft Yahei UI;\n"
                                "font-size: 16px;\n"
                                "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                "    color: black;\n"
                                "    border: 2px solid transparent;\n"
                                "    border-radius: 8px;\n"
                                "    padding: 10px 20px;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                "    border-color: #FFB6C1\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                "    border-color: #FEA5C3\n"
                                "}")
        self.pull.setObjectName("pull")
        self.horizontalLayout_9.addWidget(self.pull)
        self.pull_edit_one = QtWidgets.QLineEdit(self.tools_page)
        self.pull_edit_one.setMinimumSize(QtCore.QSize(0, 39))
        self.pull_edit_one.setObjectName("pull_edit_one")
        self.pull_edit_one.setStyleSheet(
            "QLineEdit:focus {border: none; border-bottom: 2px solid #FFBFD5; color: #FA57A1;}\n"
            "QLineEdit {color: #FA57A1;}")
        # 设置字体大小和种类
        font = QFont("Microsoft Yahei UI", 12)  # Microsoft Yahei UI，大小为10
        self.pull_edit_one.setFont(font)
        self.horizontalLayout_9.addWidget(self.pull_edit_one)
        self.pull_edit_two = QtWidgets.QLineEdit(self.tools_page)
        self.pull_edit_two.setMinimumSize(QtCore.QSize(0, 39))
        self.pull_edit_two.setStyleSheet(
            "QLineEdit:focus {border: none; border-bottom: 2px solid #FFBFD5; color: #FA57A1;}\n"
            "QLineEdit {color: #FA57A1;}")
        # 设置字体大小和种类
        font = QFont("Microsoft Yahei UI", 12)  # Microsoft Yahei UI，大小为10
        self.pull_edit_two.setFont(font)
        self.pull_edit_two.setObjectName("pull_edit_two")
        self.horizontalLayout_9.addWidget(self.pull_edit_two)
        self.browser_one = QtWidgets.QPushButton(self.tools_page)
        self.browser_one.setMinimumSize(QtCore.QSize(100, 35))
        self.browser_one.setStyleSheet("QPushButton {\n"
                                       "                            font-family: Microsoft Yahei UI;\n"
                                       "font-size: 16px;\n"
                                       "                border-radius: 8px;\n"
                                       "                background-color: #FFBFD5; /* 默认背景色 */\n"
                                       "                border: 2px solid #FFBFD5; /* 默认边框 */\n"
                                       "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                       "            }\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                       "    border-color: #FFB6C1\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                       "    border-color: #FEA5C3\n"
                                       "}")
        self.browser_one.setObjectName("browser_one")
        self.horizontalLayout_9.addWidget(self.browser_one)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.push = QtWidgets.QPushButton(self.tools_page)
        self.push.setMinimumSize(QtCore.QSize(168, 39))
        self.push.setStyleSheet("QPushButton {\n"
                                "                font-family: Microsoft Yahei UI;\n"
                                "font-size: 16px;\n"
                                "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                "    color: black;\n"
                                "    border: 2px solid transparent;\n"
                                "    border-radius: 8px;\n"
                                "    padding: 10px 20px;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                "    border-color: #FFB6C1\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                "    border-color: #FEA5C3\n"
                                "}")
        self.push.setObjectName("push")
        self.horizontalLayout_10.addWidget(self.push)
        self.push_edit_one = QtWidgets.QLineEdit(self.tools_page)
        self.push_edit_one.setMinimumSize(QtCore.QSize(0, 39))
        self.push_edit_one.setStyleSheet(
            "QLineEdit:focus {border: none; border-bottom: 2px solid #FFBFD5; color: #FA57A1;}\n"
            "QLineEdit {color: #FA57A1;}")
        # 设置字体大小和种类
        font = QFont("Microsoft Yahei UI", 12)  # Microsoft Yahei UI，大小为10
        self.push_edit_one.setFont(font)
        self.push_edit_one.setObjectName("push_edit_one")
        self.horizontalLayout_10.addWidget(self.push_edit_one)
        self.push_edit_two = QtWidgets.QLineEdit(self.tools_page)
        self.push_edit_two.setMinimumSize(QtCore.QSize(0, 39))
        self.push_edit_two.setStyleSheet(
            "QLineEdit:focus {border: none; border-bottom: 2px solid #FFBFD5; color: #FA57A1;}\n"
            "QLineEdit {color: #FA57A1;}")
        # 设置字体大小和种类
        font = QFont("Microsoft Yahei UI", 12)  # Microsoft Yahei UI，大小为10
        self.push_edit_two.setFont(font)
        self.push_edit_two.setObjectName("push_edit_two")
        self.horizontalLayout_10.addWidget(self.push_edit_two)
        self.browser_two = QtWidgets.QPushButton(self.tools_page)
        self.browser_two.setMinimumSize(QtCore.QSize(100, 35))
        self.browser_two.setStyleSheet("QPushButton {\n"
                                       "                            font-family: Microsoft Yahei UI;\n"
                                       "font-size: 16px;\n"
                                       "                border-radius: 8px;\n"
                                       "                background-color: #FFBFD5; /* 默认背景色 */\n"
                                       "                border: 2px solid #FFBFD5; /* 默认边框 */\n"
                                       "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                       "            }\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                       "    border-color: #FFB6C1\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                       "    border-color: #FEA5C3\n"
                                       "}")
        self.browser_two.setObjectName("browser_two")
        self.horizontalLayout_10.addWidget(self.browser_two)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.install = QtWidgets.QPushButton(self.tools_page)
        self.install.setMinimumSize(QtCore.QSize(168, 39))
        self.install.setStyleSheet("QPushButton {\n"
                                   "                font-family: Microsoft Yahei UI;\n"
                                   "font-size: 16px;\n"
                                   "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                   "    color: black;\n"
                                   "    border: 2px solid transparent;\n"
                                   "    border-radius: 8px;\n"
                                   "    padding: 10px 20px;\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                   "    border-color: #FFB6C1\n"
                                   "}\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                   "    border-color: #FEA5C3\n"
                                   "}")
        self.install.setObjectName("install")
        self.horizontalLayout_7.addWidget(self.install)
        self.install_edit = QtWidgets.QLineEdit(self.tools_page)
        self.install_edit.setMinimumSize(QtCore.QSize(0, 39))
        # 设置样式表，定义焦点时的字体颜色和边框
        self.install_edit.setStyleSheet(
            "QLineEdit:focus {border: none; border-bottom: 2px solid #FFBFD5; color: #FA57A1;}\n"
            "QLineEdit {color: #FA57A1;}")
        # 设置字体大小和种类
        font = QFont("Microsoft Yahei UI", 12)  # Microsoft Yahei UI，大小为10
        self.install_edit.setFont(font)
        self.install_edit.setObjectName("install_edit")
        self.horizontalLayout_7.addWidget(self.install_edit)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Enter_Edit = QtWidgets.QLineEdit(self.tools_page)
        self.Enter_Edit.setMinimumSize(QtCore.QSize(0, 39))
        # 设置样式表，定义焦点时的字体颜色和边框
        self.Enter_Edit.setStyleSheet(
            "QLineEdit:focus {border: none; border-bottom: 2px solid #FFBFD5; color: #FA57A1;}\n"
            "QLineEdit {color: #FA57A1;}")
        # 设置字体大小和种类
        font = QFont("Microsoft Yahei UI", 12)  # Microsoft Yahei UI，大小为10
        self.Enter_Edit.setFont(font)
        self.Enter_Edit.setObjectName("Enter_Edit")
        self.Enter = QtWidgets.QPushButton(self.tools_page)
        self.Enter.setMinimumSize(QtCore.QSize(100, 39))
        self.Enter.setMaximumSize(QtCore.QSize(100, 39))
        self.Enter.setStyleSheet("QPushButton {\n"
                                 "                font-family: Microsoft Yahei UI;\n"
                                 "font-size: 16px;\n"
                                 "    background-color: #FFBFD5; /* 默认状态下的颜色 */\n"
                                 "    color: black;\n"
                                 "    border: 2px solid transparent;\n"
                                 "    border-radius: 8px;\n"
                                 "    padding: 10px 20px;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                 "    border-color: #FFB6C1\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                 "    border-color: #FEA5C3\n"
                                 "}")
        self.Enter.setObjectName("Enter")
        self.horizontalLayout_11.addWidget(self.Enter_Edit)
        self.horizontalLayout_11.addWidget(self.Enter)
        self.browser_three = QtWidgets.QPushButton(self.tools_page)
        self.browser_three.setMinimumSize(QtCore.QSize(100, 35))
        self.browser_three.setStyleSheet("QPushButton {\n"
                                         "                            font-family: Microsoft Yahei UI;\n"
                                         "font-size: 16px;\n"
                                         "                border-radius: 8px;\n"
                                         "                background-color: #FFBFD5; /* 默认背景色 */\n"
                                         "                border: 2px solid #FFBFD5; /* 默认边框 */\n"
                                         "                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */\n"
                                         "            }\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFCCDA; /* 悬停状态下的颜色 */\n"
                                         "    border-color: #FFB6C1\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: #FEA5C3; /* 点击状态下的颜色 */\n"
                                         "    border-color: #FEA5C3\n"
                                         "}")
        self.browser_three.setObjectName("browser_three")
        self.horizontalLayout_7.addWidget(self.browser_three)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.textEdit = QtWidgets.QTextEdit(self.tools_page)
        self.textEdit.setStyleSheet("QTextEdit { color: #FA57A1; }"
                                    "QTextEdit:focus { border: none; border-bottom: 2px solid #FFBFD5; color: "
                                    "#FA57A1; }"
                                    )
        font = QFont("Microsoft Yahei UI", 14)  # Microsoft Yahei UI，大小为12
        # 设置垂直滚动条样式
        self.textEdit.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    background-color: #f0f0f0;"  # 滚动条背景色
            "    width: 8px;"  # 滚动条宽度
            "}"
            "QScrollBar::handle:vertical {"
            "    background-color: #FFCCDA;"  # 滑块颜色
            "    min-height: 20px;"  # 滑块最小高度
            "}"
            "QScrollBar::handle:vertical:pressed {"
            "    background-color: #FD7EB0;"  # 滑块被点击时的颜色
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    background: none;"
            "}"
        )
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.tools_page)
        # self.horizontalLayout.setStretch(0, 3)
        # self.horizontalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 添加QStackedWidget
        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.horizontalLayout.addWidget(self.stacked_widget)
        self.stacked_widget.addWidget(self.tools_page)
        self.bug_reporting_page = QtWidgets.QWidget(self.centralwidget)
        self.bug_reporting_page.setObjectName("bug_reporting_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bug_reporting_page)
        self.stacked_widget.addWidget(self.bug_reporting_page)
        self.performance_page = QtWidgets.QWidget(self.centralwidget)
        self.performance_page.setObjectName("performance_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.performance_page)
        self.stacked_widget.addWidget(self.performance_page)
        self.reports_page = QtWidgets.QWidget(self.centralwidget)
        self.reports_page.setObjectName("reports_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.reports_page)
        self.stacked_widget.addWidget(self.reports_page)
        self.other_page = QtWidgets.QWidget(self.centralwidget)
        self.other_page.setObjectName("other_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.other_page)
        self.stacked_widget.addWidget(self.other_page)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 19)
        self.retranslateUi(MainWindow)
        self.map_functions_table()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def map_functions_table(self):
        self.map_functions_page = QtWidgets.QWidget(self.centralwidget)
        self.map_functions_page.setObjectName("map_functions_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.map_functions_page)
        self.stacked_widget.addWidget(self.map_functions_page)
        self.map_functions_page.setStyleSheet("background-color:#F5F5F5")
        # 创建一个 QWebEngineView 并加载 HTML 文件
        self.web_view = QWebEngineView()
        # 请将 'path/to/your/map_with_input.html' 替换为你的 HTML 文件的实际路径
        self.web_view.load(QUrl.fromLocalFile(map_location_path))
        # 将 QWebEngineView 添加到布局中
        self.verticalLayout_2.addWidget(self.web_view)
        self.stacked_widget.addWidget(self.map_functions_page)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToolMaster"))
        self.tools.setText(_translate("MainWindow", "  Tools"))
        self.bug.setText(_translate("MainWindow", "  Bug Reporting"))
        self.perf.setText(_translate("MainWindow", "  Performance"))
        self.map.setText(_translate("MainWindow", "  Map Coordinates"))
        self.more.setText(_translate("MainWindow", "摇一摇"))
        self.label_2.setText(_translate("MainWindow", "-----------------------------------------------"))
        self.report.setText(_translate("MainWindow", "  Reports"))
        self.other.setText(_translate("MainWindow", "  Other"))
        self.label.setText(_translate("MainWindow", "-------------------------------------------------------"))
        self.label_5.setText(_translate("MainWindow", "-------------------------------------------------------"))
        self.radioButton.setText(_translate("MainWindow", "高德地图"))
        self.radioButton_2.setText(_translate("MainWindow", "腾讯地图"))
        self.clear_info.setText(_translate("MainWindow", "CLEAR INFO LOG"))
        self.open_gaode.setText(_translate("MainWindow", "打开高德地图"))
        self.close_gaode.setText(_translate("MainWindow", "关闭高德地图"))
        self.uninstall_gaode.setText(_translate("MainWindow", "卸载高德地图"))
        self.open_tencent.setText(_translate("MainWindow", "打开腾讯地图"))
        self.close_tencent.setText(_translate("MainWindow", "关闭腾讯地图"))
        self.uninstall_tencent.setText(_translate("MainWindow", "卸载腾讯地图"))
        self.open_auto.setText(_translate("MainWindow", "打开AUTO助手"))
        self.close_auto.setText(_translate("MainWindow", "关闭AUTO助手"))
        self.open_point.setText(_translate("MainWindow", "打开屏幕指针"))
        self.close_point.setText(_translate("MainWindow", "关闭屏幕指针"))
        self.open_wifi_2.setText(_translate("MainWindow", "打开Wi-Fi"))
        self.close_wifi_2.setText(_translate("MainWindow", "关闭Wi-Fi"))
        self.open_logcat_2.setText(_translate("MainWindow", "抓取LOGCAT"))
        self.close_logcat_2.setText(_translate("MainWindow", "停止LOGCAT"))
        self.setting_2.setText(_translate("MainWindow", "安卓原生设置"))
        self.root.setText(_translate("MainWindow", "ADB ROOT"))
        self.verity.setText(_translate("MainWindow", "DISABLE"))
        self.reboot.setText(_translate("MainWindow", "ADB REBOOT"))
        self.remount.setText(_translate("MainWindow", "ADB REMOUNT"))
        self.devices.setText(_translate("MainWindow", "ADB ClEAR"))
        self.label_3.setText(_translate("MainWindow", "Monkey"))
        self.tcpip.setText(_translate("MainWindow", "TCP IP"))
        self.monkey.setText(_translate("MainWindow", "START MONKEY"))
        self.label_4.setText(_translate("MainWindow", "File operation"))
        self.pull.setText(_translate("MainWindow", "ADB PULL"))
        self.browser_one.setText(_translate("MainWindow", "BROWSER"))
        self.push.setText(_translate("MainWindow", "ADB PUSH"))
        self.browser_two.setText(_translate("MainWindow", "BROWSER"))
        self.install.setText(_translate("MainWindow", "ADB INSTALL"))
        self.browser_three.setText(_translate("MainWindow", "BROWSER"))
        self.Enter.setText(_translate("MainWindow", "ENTER"))
        self.stop.setText(_translate("MainWindow", "STOP MONKEY"))
