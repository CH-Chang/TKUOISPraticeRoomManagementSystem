# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\桌面\teste\uiFile\Splash.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtSvg
from PIL import Image, ImageQt
from io import BytesIO

import base64

from imageResource.png import *
from imageResource.svg import *




class Ui_Splash(object):
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(600, 400)
        Splash.setFixedSize(600, 400)
        Splash.setWindowFlags(Qt.Qt.FramelessWindowHint)
        Splash.setWindowTitle('淡江大學 實習上機系統')
        img = base64.b64decode(tku)
        Splash.setWindowIcon(QtGui.QIcon(self.svg2pixmap(img, Qt.QSize(512,512))))
        self.top = QtWidgets.QFrame(Splash)
        self.top.setGeometry(QtCore.QRect(0, 0, 600, 250))
        self.top.setStyleSheet("QFrame{background-color: rgb(207, 49, 49)}")
        self.top.setObjectName("top")

        
        self.logo = QtWidgets.QLabel(Splash)
        self.logo.resize(85,85)
        self.logo.setFixedSize(85,85)
        self.logo.setScaledContents(True)
        img = base64.b64decode(logopng)
        img = BytesIO(img)
        img = Image.open(img)
        img = ImageQt.ImageQt(img)
        self.logo.setPixmap(QtGui.QPixmap.fromImage(img))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        self.tku = QtWidgets.QLabel(Splash)
        self.tku.resize(85,28)
        self.tku.setFixedSize(85,28)
        self.tku.setScaledContents(True)
        img = base64.b64decode(tkupng)
        img = BytesIO(img)
        img = Image.open(img)
        img = ImageQt.ImageQt(img)
        self.tku.setPixmap(QtGui.QPixmap.fromImage(img))
        self.tku.setAlignment(QtCore.Qt.AlignCenter)
        
        self.slogan = QtWidgets.QLabel(Splash)
        self.slogan.setText('<font color="white">國際化｜資訊化｜未來化</font>')
        self.slogan.setFont(QtGui.QFont('微軟正黑體', 8))
        self.slogan.setAlignment(QtCore.Qt.AlignCenter)

        self.topVerticalLayout = QtWidgets.QVBoxLayout(Splash)
        self.topVerticalLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.topVerticalLayout.addWidget(self.logo, alignment=QtCore.Qt.AlignCenter)
        self.topVerticalLayout.addWidget(self.tku, alignment=QtCore.Qt.AlignCenter)
        self.topVerticalLayout.addWidget(self.slogan, alignment=QtCore.Qt.AlignCenter)
        
        self.top.setLayout(self.topVerticalLayout)

        self.bottom = QtWidgets.QFrame(Splash)
        self.bottom.setGeometry(QtCore.QRect(0, 250, 600, 150))
        self.bottom.setStyleSheet("QFrame{background-color: #ffffff}")
        self.bottom.setObjectName("bottom")

        self.title = QtWidgets.QLabel(Splash)
        self.title.setText('實習室管制上機系統')
        self.title.setFont(QtGui.QFont('微軟正黑體', 14))
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.status = QtWidgets.QLabel(Splash)
        self.status.setText('加載中，請稍候')
        self.status.setFont(QtGui.QFont('微軟正黑體', 10))
        self.status.setAlignment(QtCore.Qt.AlignCenter)

        self.copyright = QtWidgets.QLabel(Splash)
        self.copyright.setText('<font color="#464040">Copyright © 2020 CHANG CHIH HSIANG. All rights reserved</font>')
        self.copyright.setFont(QtGui.QFont('微軟正黑體', 8))
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)

        self.bottomVerticalLayout = QtWidgets.QVBoxLayout(Splash)
        self.bottomVerticalLayout.addWidget(self.title, alignment=QtCore.Qt.AlignCenter)
        self.bottomVerticalLayout.addWidget(self.status, alignment=QtCore.Qt.AlignCenter)
        self.bottomVerticalLayout.addWidget(self.copyright, alignment=QtCore.Qt.AlignBottom)
        self.bottom.setLayout(self.bottomVerticalLayout)



        self.retranslateUi(Splash)
        QtCore.QMetaObject.connectSlotsByName(Splash)

    def retranslateUi(self, Splash):
        _translate = QtCore.QCoreApplication.translate
        Splash.setWindowTitle(_translate("Splash", "淡江大學 實習室上機系統"))

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
        

    
