# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\桌面\TEST\TEST\uiFile\MessageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):

        MessageDialog.setObjectName("MessageDialog")
        MessageDialog.resize(480, 320)
        MessageDialog.setFixedSize(480,320)
        MessageDialog.setWindowTitle('淡江大學 實習上機系統')
        MessageDialog.setWindowFlags(Qt.Qt.FramelessWindowHint)
        MessageDialog.setWindowIcon(QtGui.QIcon('./icon/tku.svg'))

        self.frame = QtWidgets.QFrame(MessageDialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet('#frame{background-color: white; border: 1px solid black; border-radius: 5px}')

        self.retranslateUi(MessageDialog)
        QtCore.QMetaObject.connectSlotsByName(MessageDialog)

        self.title = QtWidgets.QLabel(self.frame)
        self.title.setText('請輸入標題')
        self.title.setFont(QtGui.QFont('微軟正黑體',12, QtGui.QFont.Bold))
        self.title.adjustSize()
        self.title.setGeometry(QtCore.QRect(50,50,self.title.width(), self.title.height()))

        self.message = QtWidgets.QLabel(self.frame)
        self.message.setText('請輸入訊息內容')
        self.message.setWordWrap(True)
        self.message.setAlignment(Qt.Qt.AlignTop|Qt.Qt.AlignLeft)
        self.message.setFont(QtGui.QFont('微軟正黑體',10))
        self.message.setGeometry(QtCore.QRect(50,90, 380,150))
        self.message.setStyleSheet('QLabel{padding:5px}')

        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setIcon(QtGui.QIcon('./icon/close.svg'))
        self.close.setGeometry(QtCore.QRect(410,30,25,25))
        self.close.setStyleSheet('QPushButton{background-color: transparent; border-style:none;} QPushButton:hover{background-color: #eeeeee; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #999999; border-style:none; border-radius:5px;}')

        self.resultFrame = QtWidgets.QFrame(MessageDialog)
        self.resultFrame.setGeometry(QtCore.QRect(50,250,380,50))
        self.resultLayout = QtWidgets.QHBoxLayout()
        self.resultLayout.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignVCenter)
        self.resultFrame.setLayout(self.resultLayout)
        self.resultLayout.setContentsMargins(10,10,10,10)
        self.resultLayout.setSpacing(10)
        self.resultLayout.addStretch()

        self.resultComfirm = QtWidgets.QPushButton()
        self.resultComfirm.setText('確定')
        self.resultComfirm.setFont(QtGui.QFont('微軟正黑體', 10))
        self.resultComfirm.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
        self.resultLayout.addWidget(self.resultComfirm)

        self.resultCancel = QtWidgets.QPushButton()
        self.resultCancel.setText('取消')
        self.resultCancel.setFont(QtGui.QFont('微軟正黑體', 10))
        self.resultCancel.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
        self.resultLayout.addWidget(self.resultCancel)

    def retranslateUi(self, MessageDialog):
        _translate = QtCore.QCoreApplication.translate
        MessageDialog.setWindowTitle(_translate("MessageDialog", "Form"))
