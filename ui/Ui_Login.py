# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\下載\TEST\teste\uiFile\Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtSvg
from io import BytesIO
from PIL import Image, ImageQt

import base64

from imageResource.png import *
from imageResource.svg import *


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        Login.setFixedSize(800, 600)
        Login.setWindowFlags(Qt.Qt.FramelessWindowHint)
        Login.setWindowTitle('淡江大學 實習上機系統')
        img = base64.b64decode(tku)
        Login.setWindowIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(512,512))))

        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")

        # -- left

        self.left = QtWidgets.QFrame(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 300, 800))
        self.left.setStyleSheet("QFrame{background-color: rgb(207, 49, 49)}")
        self.left.setObjectName("left")
        
        self.logo = QtWidgets.QLabel(self.left)
        self.logo.setFixedSize(110,110)

        img = base64.b64decode(logopng)
        img = BytesIO(img)
        img = Image.open(img)
        img = ImageQt.ImageQt(img)
        self.logo.setPixmap(QtGui.QPixmap.fromImage(img))
        self.logo.setScaledContents(True)
        self.logo.setGeometry(QtCore.QRect(int(150-self.logo.width()/2), 120, 110, 110))

        self.school = QtWidgets.QLabel(self.left)
        self.school.setText('<font color=#FFFFFF>淡江大學</font>')
        self.school.setFont(QtGui.QFont('微軟正黑體',15))
        self.school.adjustSize()
        self.school.setGeometry(QtCore.QRect(int(150-self.school.width()/2), 250, int(self.school.width()), int(self.school.height())))

        self.slogan = QtWidgets.QLabel(self.left)
        self.slogan.setText('<font color=#ffffff>國際化｜資訊化｜未來化</font>')
        self.slogan.setFont(QtGui.QFont('微軟正黑體',10))
        self.slogan.adjustSize()
        self.slogan.setGeometry(QtCore.QRect(int(150-self.slogan.width()/2),285, int(self.slogan.width()), int(self.slogan.height())))

        self.title = QtWidgets.QLabel(self.left)
        self.title.setText('<font color=#ffffff>實習上機系統</font>')
        self.title.setFont(QtGui.QFont('微軟正黑體',18, QtGui.QFont.Bold))
        self.title.adjustSize()
        self.title.setGeometry(QtCore.QRect(int(150-self.title.width()/2),400, int(self.title.width()), int(self.title.height())))

        # --

        # -- right

        self.right = QtWidgets.QFrame(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(300, 0, 500, 800))
        self.right.setStyleSheet('QFrame{background-color: #ffffff}')
        self.right.setObjectName("right")
        Login.setCentralWidget(self.centralwidget)

        self.logintitle = QtWidgets.QLabel(self.right)
        self.logintitle.setText('<font color=#5A5858>登入LOGIN</font>')
        self.logintitle.setFont(QtGui.QFont('微軟正黑體',20))
        self.logintitle.adjustSize()
        self.logintitle.setGeometry(Qt.QRect(40, 150, int(self.logintitle.width()), int(self.logintitle.height())))


        self.usernameicon = QtSvg.QSvgWidget(self.right)
        img = base64.b64decode(user)
        self.usernameicon.load(img)
        self.usernameicon.setGeometry(Qt.QRect(90,250,30,30))

        self.username = QtWidgets.QLineEdit(self.right)
        self.username.setGeometry(Qt.QRect(130, 250, 260, 30))
        self.username.setStyleSheet('QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')
        self.username.setFont(QtGui.QFont('微軟正黑體', 12))
        self.username.setValidator(Qt.QIntValidator())


        self.passwordicon = QtSvg.QSvgWidget(self.right)
        img = base64.b64decode(lock)
        self.passwordicon.load(img)
        self.passwordicon.setGeometry(Qt.QRect(90, 300, 30, 30))


        reg = QtCore.QRegExp('[A-Za-z0-9!@#*.]+$')
        passwordVaildator = Qt.QRegExpValidator()
        passwordVaildator.setRegExp(reg)
        self.password = QtWidgets.QLineEdit(self.right)
        self.password.setGeometry(Qt.QRect(130, 300, 260, 30))
        self.password.setStyleSheet('QLineEdit{border-style:none;padding:6px;border-radius:5px;border:2px solid #5A5858;}QLineEdit:focus{border-style:none;padding:6px;border-radius:5px;border:2px solid #CF3131;}')
        self.password.setFont(QtGui.QFont('微軟正黑體', 12))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setValidator(passwordVaildator)
    

        self.login = QtWidgets.QPushButton(self.right)
        self.login.setGeometry(Qt.QRect(int(250-self.login.width()/2), 380, 80, 35))
        self.login.setText('登入')
        self.login.setFont(QtGui.QFont('微軟正黑體',12))
        self.login.setStyleSheet('QPushButton{border-style:none; padding:6px; border-radius:5px; border:2px solid #CF3131; color: white; background-color: #CF3131} QPushButton:hover{border-style:none; padding:6px; border:2px solid #CF3131; background-color:#CF3131; color:white; font-weight: 700;} QPushButton:pressed{border-style:none; padding:6px; border:2px solid #A20C0C; background-color:#A20C0C; color:white;}')

        self.status = QtWidgets.QLabel(self.right)
        self.status.setFont(QtGui.QFont('微軟正黑體', 10))
        self.status.setStyleSheet('QLabel{color: red;}')
        self.status.adjustSize()
        self.status.setGeometry(Qt.QRect(int(250-self.status.width()/2), 350, int(self.status.width()), int(self.status.height())))

        self.close = QtWidgets.QPushButton(self.right)
        img = base64.b64decode(close)
        self.close.setIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(25,25))))
        self.close.setIconSize(QtCore.QSize(25,25))
        self.close.setGeometry(Qt.QRect(430, 35, 25, 25))
        self.close.setStyleSheet('QPushButton{background-color: transparent; border-style:none;} QPushButton:hover{background-color: #eeeeee; border-style:none; border-radius:5px;} QPushButton:pressed{background-color: #999999; border-style:none; border-radius:5px;}')

        self.contact = QtWidgets.QLabel(self.right)
        self.contact.setText('淡江大學資訊處 教學支援組 (02)2621-5656 #2628')
        self.contact.setFont(QtGui.QFont('微軟正黑體',8))
        self.contact.setStyleSheet('QLabel{color: #5A5858;}')
        self.contact.adjustSize()
        self.contact.setGeometry(Qt.QRect(int(250-self.contact.width()/2), 550, int(self.contact.width()), int(self.contact.height())))

        self.copyright = QtWidgets.QLabel(self.right)
        self.copyright.setText('Copyright © 2020 CHANG CHIH HSIANG. All rights reserved')
        self.copyright.setFont(QtGui.QFont('微軟正黑體',8))
        self.copyright.setStyleSheet('QLabel{color: #5A5858;}')
        self.copyright.adjustSize()
        self.copyright.setGeometry(Qt.QRect(int(250-self.copyright.width()/2), 565, int(self.copyright.width()), int(self.copyright.height())))

        # --

        # -- loading

        loadingOpacity = QtWidgets.QGraphicsOpacityEffect()
        loadingOpacity.setOpacity(0.5)

        self.loading = QtWidgets.QFrame(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(0,0,800,600))
        self.loading.setStyleSheet('QFrame{background-color: black;}')
        self.loading.setAutoFillBackground(True)
        self.loading.setGraphicsEffect(loadingOpacity)
        self.loading.setVisible(False)
        
        self.loadingLabel = QtWidgets.QLabel(self.loading)
        self.loadingLabel.setText('登入中，請稍後')
        self.loadingLabel.setFont(QtGui.QFont('微軟正黑體', 15 ,QtGui.QFont.Bold))
        self.loadingLabel.setStyleSheet('QLabel{color: white;}')
        self.loadingLabel.adjustSize()
        self.loadingLabel.setGeometry(QtCore.QRect(int(400-self.loadingLabel.width()/2),int(300-self.loadingLabel.height()/2),self.loadingLabel.width(),self.loadingLabel.height()))

        # --

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))

    def svg2pixmap(self, img, size):
        render = QtSvg.QSvgRenderer(img)
        image = QtGui.QImage(size.width(),size.height(),QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(image)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)
        image.fill(Qt.Qt.transparent)
        render.render(painter)
        img = QtGui.QPixmap.fromImage(image)
        del painter
        return img
