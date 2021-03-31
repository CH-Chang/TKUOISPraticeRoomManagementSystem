# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Downloads\TEST-20200518T051015Z-001\TEST\teste\uiFile\ManagmentSystem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtSvg
from widgets.QLineEdit import QLineEdit
from widgets.QPushButton import QPushButton

import base64

from imageResource.svg import *


class Ui_ManagementSystem(object):
    def setupUi(self, ManagementSystem):
        ManagementSystem.setObjectName("ManagementSystem")
        ManagementSystem.resize(1350, 720)
        ManagementSystem.setFixedSize(1350, 720)
        ManagementSystem.setWindowTitle('淡江大學 實習上機系統')
        ManagementSystem.setWindowFlags(Qt.Qt.FramelessWindowHint)
        img = base64.b64decode(tku)
        ManagementSystem.setWindowIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(512, 512))))

        self.centralwidget = QtWidgets.QWidget(ManagementSystem)
        self.centralwidget.setObjectName("centralwidget")

        self.setupToolbar()
        self.setupContent()

        ManagementSystem.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManagementSystem)
        QtCore.QMetaObject.connectSlotsByName(ManagementSystem)

    def retranslateUi(self, ManagementSystem):
        _translate = QtCore.QCoreApplication.translate
        ManagementSystem.setWindowTitle(
            _translate("ManagementSystem", "MainWindow"))

    def setupToolbar(self):
        # -- Toolbar

        self.toolbar = QtWidgets.QFrame(self.centralwidget)
        self.toolbar.setGeometry(QtCore.QRect(0, 0, 70, 720))
        self.toolbar.setStyleSheet(
            "QFrame{background-color: rgb(207, 49, 49);}")
        self.toolbar.setObjectName("toolbar")

        self.info = QtWidgets.QPushButton()
        self.info.setToolTip('關於我們')
        img = base64.b64decode(info)
        self.info.setIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.info.setIconSize(QtCore.QSize(30, 30))
        self.info.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.logout = QtWidgets.QPushButton()
        self.logout.setToolTip('帳號登出')
        img = base64.b64decode(logout)
        self.logout.setIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.logout.setIconSize(QtCore.QSize(30, 30))
        self.logout.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.seatTime = QtWidgets.QPushButton()
        self.seatTime.setToolTip('座位用時')
        img = base64.b64decode(seatTime)
        self.seatTime.setIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.seatTime.setIconSize(QtCore.QSize(30, 30))
        self.seatTime.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.setting = QtWidgets.QPushButton()
        self.setting.setToolTip('程序設定')
        img = base64.b64decode(setting)
        self.setting.setIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.setting.setIconSize(QtCore.QSize(30, 30))
        self.setting.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.classSeat = QtWidgets.QPushButton()
        self.classSeat.setToolTip('班級上機')
        img = base64.b64decode(classes)
        self.classSeat.setIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.classSeat.setIconSize(QtCore.QSize(30, 30))
        self.classSeat.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.clean = QtWidgets.QPushButton()
        self.clean.setToolTip('維修時間')
        img = base64.b64decode(clean)
        self.clean.setIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.clean.setIconSize(QtCore.QSize(30, 30))
        self.clean.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.clear = QtWidgets.QPushButton()
        self.clear.setToolTip('清除全部')
        img = base64.b64decode(clear)
        self.clear.setIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.clear.setIconSize(QtCore.QSize(30, 30))
        self.clear.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.reservation = QtWidgets.QPushButton()
        self.reservation.setToolTip('預約查詢')
        img = base64.b64decode(reservation)
        self.reservation.setIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(30, 30))))
        self.reservation.setIconSize(QtCore.QSize(30, 30))
        self.reservation.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none; padding:5px;} QPushButton:hover{background-color: #B42727; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #981616; border-style:none; border-radius:5px;}')

        self.toolbarLayout = QtWidgets.QVBoxLayout(self.toolbar)
        self.toolbarLayout.setContentsMargins(10, 10, 10, 10)
        self.toolbarLayout.setSpacing(10)
        self.toolbarLayout.addStretch()
        self.toolbarLayout.addWidget(self.seatTime)
        self.toolbarLayout.addWidget(self.classSeat)
        self.toolbarLayout.addWidget(self.clear)
        self.toolbarLayout.addWidget(self.clean)
        self.toolbarLayout.addWidget(self.reservation)
        self.toolbarLayout.addWidget(self.setting)
        self.toolbarLayout.addWidget(self.logout)
        self.toolbarLayout.addWidget(self.info)

        # --

    def setupContent(self):
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(70, 0, 1280, 720))
        self.content.setStyleSheet("QFrame{background-color: white;}")
        self.content.setObjectName("content")

        self.setupNavigation()
        self.setupSeatTable()
        self.setupDashboard()

    def setupNavigation(self):
        self.close = QtWidgets.QPushButton(self.content)
        img = base64.b64decode(close)
        self.close.setIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(25, 25))))
        self.close.setIconSize(QtCore.QSize(25, 25))
        self.close.setGeometry(QtCore.QRect(1200, 30, 25, 25))
        self.close.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none;} QPushButton:hover{background-color: #eeeeee; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #999999; border-style:none; border-radius:5px;}')

        self.minimal = QtWidgets.QPushButton(self.content)
        img = base64.b64decode(minimal)
        self.minimal.setIcon(QtGui.QIcon(
            self.svg2pixmap(img, Qt.QSize(25, 25))))
        self.minimal.setIconSize(QtCore.QSize(25, 25))
        self.minimal.setGeometry(QtCore.QRect(1170, 30, 25, 25))
        self.minimal.setStyleSheet(
            'QPushButton{background-color: transparent; border-style:none;} QPushButton:hover{background-color: #eeeeee; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #999999; border-style:none; border-radius:5px;}')

    def setupSeatTable(self):
        self.seatTable = QtWidgets.QFrame(self.content)
        self.seatTable.setGeometry(QtCore.QRect(30, 75, 1220, 400))

        self.seatTableLayout = QtWidgets.QGridLayout(self.seatTable)
        self.parseSeatConfig(self.seatTableLayout)

    def setupDashboard(self):
        self.dashboard = QtWidgets.QFrame(self.content)
        self.dashboard.setGeometry(QtCore.QRect(30, 500, 1220, 200))

        self.dashboardLayout = QtWidgets.QHBoxLayout(self.dashboard)

        self.setupControl()
        self.setupInformation()

    def setupInformation(self):
        self.information = QtWidgets.QGridLayout()

        # 日期
        dateIcon = QtWidgets.QLabel()
        img = base64.b64decode(date)
        dateIcon.setPixmap(QtGui.QPixmap(
            self.svg2pixmap(img, Qt.QSize(20, 20))))
        dateIcon.setFixedSize(QtCore.QSize(20, 20))
        dateIcon.setScaledContents(True)

        self.date = QtWidgets.QLabel('')
        self.date.setFont(QtGui.QFont('微軟正黑體', 12))

        # 時間
        timeIcon = QtWidgets.QLabel()
        img = base64.b64decode(time)
        timeIcon.setPixmap(QtGui.QPixmap(
            self.svg2pixmap(img, Qt.QSize(20, 20))))
        timeIcon.setFixedSize(QtCore.QSize(20, 20))
        timeIcon.setScaledContents(True)

        self.time = QtWidgets.QLabel('')
        self.time.setFont(QtGui.QFont('微軟正黑體', 12))

        # 位置
        locationIcon = QtWidgets.QLabel()
        img = base64.b64decode(location)
        locationIcon.setPixmap(QtGui.QPixmap(
            self.svg2pixmap(img, Qt.QSize(20, 20))))
        locationIcon.setFixedSize(QtCore.QSize(20, 20))
        locationIcon.setScaledContents(True)

        self.location = QtWidgets.QLabel('')
        self.location.setFont(QtGui.QFont('微軟正黑體', 12))

        # 天氣
        weatherIcon = QtWidgets.QLabel()
        img = base64.b64decode(weather)
        weatherIcon.setPixmap(QtGui.QPixmap(
            self.svg2pixmap(img, Qt.QSize(20, 20))))
        weatherIcon.setFixedSize(QtCore.QSize(20, 20))
        weatherIcon.setScaledContents(True)

        self.weather = QtWidgets.QLabel('')
        self.weather.setFont(QtGui.QFont('微軟正黑體', 12))

        # 心情
        moodIcon = QtWidgets.QLabel()
        img = base64.b64decode(mood)
        moodIcon.setPixmap(QtGui.QPixmap(
            self.svg2pixmap(img, Qt.QSize(20, 20))))
        moodIcon.setFixedSize(QtCore.QSize(20, 20))
        moodIcon.setScaledContents(True)

        self.mood = QtWidgets.QLabel('快要下班瞜，再堅持一下')
        self.mood.setFont(QtGui.QFont('微軟正黑體', 12))

        self.information.addWidget(dateIcon, 0, 0)
        self.information.addWidget(self.date, 0, 1)
        self.information.addWidget(timeIcon, 1, 0)
        self.information.addWidget(self.time, 1, 1)
        self.information.addWidget(locationIcon, 2, 0)
        self.information.addWidget(self.location, 2, 1)
        self.information.addWidget(weatherIcon, 3, 0)
        self.information.addWidget(self.weather, 3, 1)
        self.information.addWidget(moodIcon, 4, 0)
        self.information.addWidget(self.mood, 4, 1)

        self.dashboardLayout.addLayout(self.information)
        self.dashboardLayout.setStretchFactor(self.information, 2)

    def setupControl(self):

        stuIDReg = Qt.QRegExp('^\d{0,9}$')
        stuIDRegValidator = Qt.QRegExpValidator()
        stuIDRegValidator.setRegExp(stuIDReg)

        seatReg = Qt.QRegExp('^\d{0,}$')
        intValidator = Qt.QRegExpValidator()
        intValidator.setRegExp(seatReg)

        self.control = QtWidgets.QGridLayout()

        autoOnlineStuIDLabel = QtWidgets.QLabel()
        autoOnlineStuIDLabel.setText('自動上機學號')
        autoOnlineStuIDLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.autoOnlineStuID = QLineEdit()
        self.autoOnlineStuID.setFont(QtGui.QFont('微軟正黑體', 10))
        self.autoOnlineStuID.setValidator(stuIDRegValidator)
        self.autoOnlineStuID.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.autoOnlineStuIDCommit = QtWidgets.QPushButton()
        self.autoOnlineStuIDCommit.setText('上機')
        self.autoOnlineStuIDCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.autoOnlineStuIDCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.autoOnlineStuIDCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        self.autoOnlineStatus = QtWidgets.QLabel()
        self.autoOnlineStatus.setText('您已輸入0人')
        self.autoOnlineStatus.setFont(QtGui.QFont('微軟正黑體', 10))

        singleOnlineStuIDLabel = QtWidgets.QLabel()
        singleOnlineStuIDLabel.setText('手動單一上機學號')
        singleOnlineStuIDLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.singleOnlineStuID = QLineEdit()
        self.singleOnlineStuID.setValidator(stuIDRegValidator)
        self.singleOnlineStuID.setFont(QtGui.QFont('微軟正黑體', 10))
        self.singleOnlineStuID.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.singleOnlineStuIDCommit = QtWidgets.QPushButton()
        self.singleOnlineStuIDCommit.setText('輸入')
        self.singleOnlineStuIDCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.singleOnlineStuIDCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.singleOnlineStuIDCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        singleOnlineSeatLabel = QtWidgets.QLabel()
        singleOnlineSeatLabel.setText('手動單一上機座號')
        singleOnlineSeatLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.singleOnlineSeat = QLineEdit()
        self.singleOnlineSeat.setFont(QtGui.QFont('微軟正黑體', 10))
        self.singleOnlineSeat.setValidator(intValidator)
        self.singleOnlineSeat.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.singleOnlineSeatCommit = QtWidgets.QPushButton()
        self.singleOnlineSeatCommit.setText('上機')
        self.singleOnlineSeatCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.singleOnlineSeatCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.singleOnlineSeatCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        singleOfflineSeatLabel = QtWidgets.QLabel()
        singleOfflineSeatLabel.setText('手動單一下機座號')
        singleOfflineSeatLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.singleOfflineSeat = QLineEdit()
        self.singleOfflineSeat.setFont(QtGui.QFont('微軟正黑體', 10))
        self.singleOfflineSeat.setValidator(intValidator)
        self.singleOfflineSeat.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.singleOfflineSeatCommit = QtWidgets.QPushButton()
        self.singleOfflineSeatCommit.setText('下機')
        self.singleOfflineSeatCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.singleOfflineSeatCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.singleOfflineSeatCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        manyOnlineStuIDLabel = QtWidgets.QLabel()
        manyOnlineStuIDLabel.setText('手動批量上機學號')
        manyOnlineStuIDLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.manyOnlineStuID = QLineEdit()
        self.manyOnlineStuID.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOnlineStuID.setValidator(stuIDRegValidator)
        self.manyOnlineStuID.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.manyOnlineStuIDCommit = QtWidgets.QPushButton()
        self.manyOnlineStuIDCommit.setText('輸入')
        self.manyOnlineStuIDCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.manyOnlineStuIDCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOnlineStuIDCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        self.manyOnlineStuIDStatus = QtWidgets.QLabel()
        self.manyOnlineStuIDStatus.setText('您已輸入0人')
        self.manyOnlineStuIDStatus.setFont(QtGui.QFont('微軟正黑體', 10))

        manyOnlineSeatLabel = QtWidgets.QLabel()
        manyOnlineSeatLabel.setText('手動批量上機座號')
        manyOnlineSeatLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.manyOnlineSeatStart = QLineEdit()
        self.manyOnlineSeatStart.setValidator(intValidator)
        self.manyOnlineSeatStart.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOnlineSeatStart.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.manyOnlineSeatEnd = QLineEdit()
        self.manyOnlineSeatEnd.setValidator(intValidator)
        self.manyOnlineSeatEnd.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOnlineSeatEnd.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.manyOnlineSeatCommit = QtWidgets.QPushButton()
        self.manyOnlineSeatCommit.setText('上機')
        self.manyOnlineSeatCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.manyOnlineSeatCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOnlineSeatCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        manyOfflineSeatLabel = QtWidgets.QLabel()
        manyOfflineSeatLabel.setText('手動批量下機座號')
        manyOfflineSeatLabel.setFont(QtGui.QFont('微軟正黑體', 10))

        self.manyOfflineSeatStart = QLineEdit()
        self.manyOfflineSeatStart.setValidator(intValidator)
        self.manyOfflineSeatStart.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOfflineSeatStart.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.manyOfflineSeatEnd = QLineEdit()
        self.manyOfflineSeatEnd.setValidator(intValidator)
        self.manyOfflineSeatEnd.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOfflineSeatEnd.setStyleSheet(
            'QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')

        self.manyOfflineSeatCommit = QtWidgets.QPushButton()
        self.manyOfflineSeatCommit.setSizePolicy(Qt.QSizePolicy(
            Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding))
        self.manyOfflineSeatCommit.setText('下機')
        self.manyOfflineSeatCommit.setFont(QtGui.QFont('微軟正黑體', 10))
        self.manyOfflineSeatCommit.setStyleSheet(
            'QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

        self.control.addWidget(autoOnlineStuIDLabel, 0, 0, 1, 3)
        self.control.addWidget(self.autoOnlineStuID, 1, 0, 1, 2)
        self.control.addWidget(self.autoOnlineStuIDCommit, 1, 2, 1, 1)
        self.control.addWidget(self.autoOnlineStatus, 2, 0, 1, 3)

        self.control.addWidget(singleOnlineStuIDLabel, 0, 3, 1, 3)
        self.control.addWidget(self.singleOnlineStuID, 1, 3, 1, 2)
        self.control.addWidget(self.singleOnlineStuIDCommit, 1, 5, 1, 1)

        self.control.addWidget(singleOnlineSeatLabel, 0, 6, 1, 3)
        self.control.addWidget(self.singleOnlineSeat, 1, 6, 1, 2)
        self.control.addWidget(self.singleOnlineSeatCommit, 1, 8, 1, 1)

        self.control.addWidget(singleOfflineSeatLabel, 0, 9, 1, 3)
        self.control.addWidget(self.singleOfflineSeat, 1, 9, 1, 2)
        self.control.addWidget(self.singleOfflineSeatCommit, 1, 11, 1, 1)

        self.control.addWidget(singleOfflineSeatLabel, 0, 12, 1, 3)
        self.control.addWidget(self.singleOfflineSeat, 1, 12, 1, 2)
        self.control.addWidget(self.singleOfflineSeatCommit, 1, 14, 1, 1)

        self.control.addWidget(manyOnlineStuIDLabel, 2, 3, 1, 3)
        self.control.addWidget(self.manyOnlineStuID, 3, 3, 1, 2)
        self.control.addWidget(self.manyOnlineStuIDCommit, 3, 5, 1, 1)
        self.control.addWidget(self.manyOnlineStuIDStatus, 4, 3, 1, 3)

        self.control.addWidget(manyOnlineSeatLabel, 2, 6, 1, 3)
        self.control.addWidget(self.manyOnlineSeatStart, 3, 6, 1, 1)
        self.control.addWidget(self.manyOnlineSeatEnd, 3, 7, 1, 1)
        self.control.addWidget(self.manyOnlineSeatCommit, 3, 8, 1, 1)

        self.control.addWidget(manyOfflineSeatLabel, 2, 9, 1, 3)
        self.control.addWidget(self.manyOfflineSeatStart, 3, 9, 1, 1)
        self.control.addWidget(self.manyOfflineSeatEnd, 3, 10, 1, 1)
        self.control.addWidget(self.manyOfflineSeatCommit, 3, 11, 1, 1)

        for i in range(0, self.control.columnCount()):
            self.control.setColumnStretch(i, 1)

        for i in range(0, self.control.rowCount()):
            self.control.setRowStretch(i, 1)
        self.dashboardLayout.addLayout(self.control)
        self.dashboardLayout.setStretchFactor(self.control, 8)

    def parseSeatConfig(self, seatTableLayout):
        config = open('./configs/seatConfig', 'r')
        configContent = config.readlines()
        config.close()

        seatNum = 0

        scannericon = base64.b64decode(scanner)
        printericon = base64.b64decode(printer)
        computericon = base64.b64decode(computer)

        for i in range(0, len(configContent)):

            line = configContent[i]

            for j in range(0, len(line)):

                if line[j] == 'C':
                    seatNum += 1
                    seat = QPushButton()
                    seat.setIcon(QtGui.QIcon(self.svg2pixmap(
                        computericon, QtCore.QSize(128, 128))))
                    seat.setText(f'{seatNum:02d}')
                    seat.setFont(QtGui.QFont('微軟正黑體', 10))
                    seat.setToolTip('空位')
                    seat.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                    seatTableLayout.addWidget(seat, i, j)
                elif line[j] == 'S':
                    seatNum += 1
                    scanners = QPushButton()
                    scanners.setIcon(QtGui.QIcon(self.svg2pixmap(
                        scannericon, QtCore.QSize(128, 128))))
                    scanners.setText(f'{seatNum:02d}')
                    scanners.setFont(QtGui.QFont('微軟正黑體', 10))
                    scanners.setToolTip('空位')
                    scanners.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                    seatTableLayout.addWidget(scanners, i, j)
                elif line[j] == 'P':
                    printers = QtWidgets.QPushButton()
                    printers.setIcon(QtGui.QIcon(self.svg2pixmap(
                        printericon, QtCore.QSize(128, 128))))
                    printers.setToolTip('印表機')
                    printers.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                    seatTableLayout.addWidget(printers, i, j)

        for i in range(0, seatTableLayout.columnCount()):
            seatTableLayout.setColumnStretch(i, 1)

        for i in range(0, seatTableLayout.rowCount()):
            seatTableLayout.setRowStretch(i, 1)

    def svg2pixmap(self, img, size):
        render = QtSvg.QSvgRenderer(img)
        image = QtGui.QImage(size.width(), size.height(),
                             QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(image)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)
        image.fill(Qt.Qt.transparent)
        render.render(painter)
        img = QtGui.QPixmap.fromImage(image)
        del painter
        return img
