# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\桌面\TEST\TEST\uiFile\UseTimeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_UseTimeDialog(object):
    def setupUi(self, UseTimeDialog):

        UseTimeDialog.setObjectName("UseTimeDialog")
        UseTimeDialog.resize(480, 320)
        UseTimeDialog.setFixedSize(480,320)
        UseTimeDialog.setWindowTitle('淡江大學 實習上機系統')
        UseTimeDialog.setWindowFlags(Qt.Qt.FramelessWindowHint)
        UseTimeDialog.setWindowIcon(QtGui.QIcon('./icon/tku.svg'))

        self.frame = QtWidgets.QFrame(UseTimeDialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet('#frame{background-color: white; border: 1px solid black; border-radius: 5px}')

        self.retranslateUi(UseTimeDialog)
        QtCore.QMetaObject.connectSlotsByName(UseTimeDialog)

        self.title = QtWidgets.QLabel(self.frame)
        self.title.setText('座位使用時間')
        self.title.setFont(QtGui.QFont('微軟正黑體',12, QtGui.QFont.Bold))
        self.title.adjustSize()
        self.title.setGeometry(QtCore.QRect(50,50,self.title.width(), self.title.height()))

        self.usetimearea = QtWidgets.QScrollArea(self.frame)
        self.usetimearea.setGeometry(QtCore.QRect(50,70, 380,200))
        self.usetimearea.setStyleSheet('QScrollArea{padding:5px; background-color: white; border-style: none;}')

        self.usetimeareaContent = QtWidgets.QWidget()
        self.usetimeareaContent.setStyleSheet('QWidget{background-color: white;}')
        self.usetimearea.setWidget(self.usetimeareaContent)
        self.usetimearea.setWidgetResizable(True)
        self.usetimeareaContentLayout = QtWidgets.QVBoxLayout()
        self.usetimeareaContentLayout.setAlignment(Qt.Qt.AlignTop)
        self.usetimeareaContent.setLayout(self.usetimeareaContentLayout)

        titleLayout = QtWidgets.QHBoxLayout()
        self.usetimeareaContentLayout.addLayout(titleLayout)

        stuID = QtWidgets.QLabel('學號')
        stuID.setAlignment(Qt.Qt.AlignCenter)
        stuID.setFont(QtGui.QFont('微軟正黑體',10))
        titleLayout.addWidget(stuID)

        seatNum = QtWidgets.QLabel('座號')
        seatNum.setAlignment(Qt.Qt.AlignCenter)
        seatNum.setFont(QtGui.QFont('微軟正黑體',10))
        titleLayout.addWidget(seatNum)

        useTime = QtWidgets.QLabel('上機時間')
        useTime.setAlignment(Qt.Qt.AlignCenter)
        useTime.setFont(QtGui.QFont('微軟正黑體',10))
        titleLayout.addWidget(useTime)



        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setIcon(QtGui.QIcon('./icon/close.svg'))
        self.close.setGeometry(QtCore.QRect(410,30,25,25))
        self.close.setStyleSheet('QPushButton{background-color: transparent; border-style:none;} QPushButton:hover{background-color: #eeeeee; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #999999; border-style:none; border-radius:5px;}')

        

    def retranslateUi(self, UseTimeDialog):
        _translate = QtCore.QCoreApplication.translate
        UseTimeDialog.setWindowTitle(_translate("UseTimeDialog", "Form"))
