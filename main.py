from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui.Ui_Splash import *
from ui.Ui_Login import *
from ui.Ui_ManagementSystem import *
from ui.Ui_MessageDialog import *
from ui.Ui_UseTimeDialog import *
from utils.ServerDB import *

from imageResource.svg import *

import sys
import os
import datetime
import numpy
import requests
import json

# UseTimeDialog


class UseTimeDialog(QDialog):
    def __init__(self, data):
        super(UseTimeDialog, self).__init__()
        self.data = data
        self.init()
        self.loading()

    def init(self):
        self.initUI()
        self.initInteraction()

    def initUI(self):
        self.ui = Ui_UseTimeDialog()
        self.ui.setupUi(self)

    def initInteraction(self):
        self.ui.close.clicked.connect(self.reject)

    def loading(self):
        self.loadingData()

    def loadingData(self):
        for i in range(0, len(self.data)):
            horizentalLayout = QHBoxLayout()
            stuID = QLabel(self.data[i][0])
            stuID.setFont(QFont('微軟正黑體', 10))
            stuID.setAlignment(QtCore.Qt.AlignCenter)
            horizentalLayout.addWidget(stuID)
            seatNum = QLabel(self.data[i][1])
            seatNum.setFont(QFont('微軟正黑體', 10))
            seatNum.setAlignment(QtCore.Qt.AlignCenter)
            horizentalLayout.addWidget(seatNum)
            useTime = QLabel(self.data[i][2])
            useTime.setFont(QFont('微軟正黑體', 10))
            useTime.setAlignment(QtCore.Qt.AlignCenter)
            horizentalLayout.addWidget(useTime)
            self.ui.usetimeareaContentLayout.addLayout(horizentalLayout)

    # 重載方法
    def mousePressEvent(self, event):
        self.pressX = event.x()
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        moveX = x-self.pressX
        moveY = y-self.pressY
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY
        self.move(positionX, positionY)

# Dialog


class MessageDialog(QDialog):
    def __init__(self):
        super(MessageDialog, self).__init__()
        self.init()

    def init(self):
        self.initUI()
        self.initInteraction()

    def initUI(self):
        self.ui = Ui_MessageDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('提示訊息')

    def initInteraction(self):
        self.ui.resultComfirm.clicked.connect(self.accept)
        self.ui.resultCancel.clicked.connect(self.reject)
        self.ui.close.clicked.connect(self.reject)

    def setTitle(self, title):
        self.ui.title.setText(title)
        self.ui.title.adjustSize()
        self.ui.title.setGeometry(
            QRect(50, 50, self.ui.title.width(), self.ui.title.height()))
        return

    def setMessage(self, message):
        self.ui.message.setText(message)
        return

    # 重載方法

    def mousePressEvent(self, event):
        self.pressX = event.x()
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        moveX = x-self.pressX
        moveY = y-self.pressY
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY
        self.move(positionX, positionY)

# 主系統頁面


class ManagementSystem(QMainWindow):

    # variable
    interval = 1
    lock = 0

    useTimes = []
    onlineStuIDs = []
    onlineSeats = []
    offlineSeats = []
    runningThread = []

    def __init__(self):
        super(ManagementSystem, self).__init__()
        self.init()
        self.loading()

    def init(self):
        self.initUI()
        self.initInteraction()
        self.initUseTimes()

    # 初始化區
    def initUI(self):
        self.ui = Ui_ManagementSystem()
        self.ui.setupUi(self)
        self.setWindowTitle('淡江大學 實習上機系統')
        img = base64.b64decode(tku)
        self.setWindowIcon(QtGui.QIcon(self.svg2pixmap(img, QSize(512, 512))))

    def initInteraction(self):
        self.ui.close.clicked.connect(self.clickedClose)
        self.ui.minimal.clicked.connect(self.clickedMinimal)

        self.ui.autoOnlineStuID.focused.connect(self.cancelAutoOnlineStuID)
        self.ui.autoOnlineStuID.unfocused.connect(self.cancelAutoOnlineStuID)
        self.ui.autoOnlineStuID.keyDeletePressed.connect(
            self.cancelAutoOnlineStuID)
        self.ui.autoOnlineStuID.returnPressed.connect(
            self.commitAutoOnlineStuID)
        self.ui.autoOnlineStuID.keyRightPressed.connect(
            self.keyRightPressedAutoOnlineStuID)
        self.ui.autoOnlineStuID.keyLeftPressed.connect(
            self.keyLeftPressedAutoOnlineStuID)
        self.ui.autoOnlineStuIDCommit.clicked.connect(
            self.commitAutoOnlineStuID)

        self.ui.singleOnlineStuID.focused.connect(
            self.focusedSingleOnlineStuID)
        self.ui.singleOnlineStuID.returnPressed.connect(
            self.commitSingleOnlineStuID)
        self.ui.singleOnlineStuID.keyRightPressed.connect(
            self.keyRightPressedSingleOnlineStuID)
        self.ui.singleOnlineStuID.keyLeftPressed.connect(
            self.keyLeftPressedSingleOnlineStuID)
        self.ui.singleOnlineStuID.keyDownPressed.connect(
            self.keyDownPressedSingleOnlineStuID)
        self.ui.singleOnlineStuIDCommit.clicked.connect(
            self.commitSingleOnlineStuID)

        self.ui.singleOnlineSeat.focused.connect(self.focusedSingleOnlineSeat)
        self.ui.singleOnlineSeat.returnPressed.connect(
            self.commitSingleOnlineSeat)
        self.ui.singleOnlineSeat.keyLeftPressed.connect(
            self.keyLeftPressedSingleOnlineSeat)
        self.ui.singleOnlineSeat.keyRightPressed.connect(
            self.keyRightPressedSingleOnlineSeat)
        self.ui.singleOnlineSeat.keyDownPressed.connect(
            self.keyDownPressedSingleOnlineSeat)
        self.ui.singleOnlineSeatCommit.clicked.connect(
            self.commitSingleOnlineSeat)

        self.ui.singleOfflineSeat.focused.connect(
            self.focusedSingleOfflineSeat)
        self.ui.singleOfflineSeat.returnPressed.connect(
            self.commitSingleOfflineSeat)
        self.ui.singleOfflineSeat.keyLeftPressed.connect(
            self.keyLeftPressedSingleOfflineSeat)
        self.ui.singleOfflineSeat.keyRightPressed.connect(
            self.keyRightPressedSingleOfflineSeat)
        self.ui.singleOfflineSeat.keyDownPressed.connect(
            self.keyDownPressedSingleOfflineSeat)
        self.ui.singleOfflineSeatCommit.clicked.connect(
            self.commitSingleOfflineSeat)

        self.ui.manyOnlineStuID.focused.connect(self.cancelManyOnlineStuID)
        self.ui.manyOnlineStuID.keyDeletePressed.connect(
            self.cancelManyOnlineStuID)
        self.ui.manyOnlineStuID.returnPressed.connect(
            self.commitManyOnlineStuID)
        self.ui.manyOnlineStuID.keyLeftPressed.connect(
            self.keyLeftPressedManyOnlineStuID)
        self.ui.manyOnlineStuID.keyUpPressed.connect(
            self.keyUpPressedManyOnlineStuID)
        self.ui.manyOnlineStuID.keyRightPressed.connect(
            self.keyRightPressedManyOnlineStuID)
        self.ui.manyOnlineStuIDCommit.clicked.connect(
            self.commitManyOnlineStuID)

        self.ui.manyOnlineSeatStart.focused.connect(
            self.focusedManyOnlineSeatStart)
        self.ui.manyOnlineSeatEnd.focused.connect(
            self.focusedManyOnlineSeatEnd)
        self.ui.manyOnlineSeatStart.returnPressed.connect(
            self.returnPressedManyOnlineSeatStart)
        self.ui.manyOnlineSeatStart.keyUpPressed.connect(
            self.keyUpPressedManyOnlineSeatStart)
        self.ui.manyOnlineSeatStart.keyLeftPressed.connect(
            self.keyLeftPressedManyOnlineSeatStart)
        self.ui.manyOnlineSeatStart.keyRightPressed.connect(
            self.keyRightPressedManyOnlineSeatStart)
        self.ui.manyOnlineSeatEnd.returnPressed.connect(
            self.commitManyOnlineSeat)
        self.ui.manyOnlineSeatEnd.keyUpPressed.connect(
            self.keyUpPressedManyOnlineSeatEnd)
        self.ui.manyOnlineSeatEnd.keyLeftPressed.connect(
            self.keyLeftPressedManyOnlineSeatEnd)
        self.ui.manyOnlineSeatEnd.keyRightPressed.connect(
            self.keyRightPressedManyOnlineSeatEnd)
        self.ui.manyOnlineSeatCommit.clicked.connect(self.commitManyOnlineSeat)

        self.ui.manyOfflineSeatStart.focused.connect(
            self.focusedManyOfflineSeatStart)
        self.ui.manyOfflineSeatEnd.focused.connect(
            self.focusedManyOfflineSeatEnd)
        self.ui.manyOfflineSeatEnd.keyUpPressed.connect(
            self.keyUpPressedManyOfflineSeatEnd)
        self.ui.manyOfflineSeatEnd.keyLeftPressed.connect(
            self.keyLeftPressedManyOfflineSeatEnd)
        self.ui.manyOfflineSeatEnd.keyRightPressed.connect(
            self.keyRightPressedManyOfflineSeatEnd)
        self.ui.manyOfflineSeatStart.returnPressed.connect(
            self.returnPressedManyOfflineSeatStart)
        self.ui.manyOfflineSeatStart.keyUpPressed.connect(
            self.keyUpPressedManyOfflineSeatStart)
        self.ui.manyOfflineSeatStart.keyLeftPressed.connect(
            self.keyLeftPressedManyOfflineSeatStart)
        self.ui.manyOfflineSeatStart.keyRightPressed.connect(
            self.keyRightPressedManyOfflineSeatStart)
        self.ui.manyOfflineSeatEnd.returnPressed.connect(
            self.commitManyOfflineSeat)
        self.ui.manyOfflineSeatCommit.clicked.connect(
            self.commitManyOfflineSeat)

        self.ui.logout.clicked.connect(self.clickedLogout)
        self.ui.seatTime.clicked.connect(self.clickedSeatTime)
        self.ui.classSeat.clicked.connect(self.clickedClassSeat)
        self.ui.clear.clicked.connect(self.clickedClear)
        self.ui.clean.clicked.connect(self.clickedClean)

        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '':
                        seat.dropped.connect(self.exchangeSeat)

    def initUseTimes(self):
        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '':
                        self.useTimes.append(None)

    # 載入資料區
    def loading(self):
        self.loadingSetting()
        self.loadingInformation()
        self.loadingSeatStatus()
        self.loadingUseTime()

    def loadingInformation(self):
        self.loadingDateTime()
        self.loadingWeather()
        self.loadingRoom()
        self.loadingMood()

    def loadingDateTime(self):
        self.TimerDatetime = QTimer()
        self.TimerDatetime.timeout.connect(self.updateDateTime)
        self.TimerDatetime.start(1000)

    def loadingWeather(self):

        self.TimerWeather = QTimer()
        self.TimerWeather.timeout.connect(self.updateWeather)
        self.TimerWeather.singleShot(0, self.updateWeather)
        self.TimerWeather.start(3600000)

    def loadingRoom(self):
        self.threadRoomName = ThreadGetRoomName()
        self.threadRoomName.res.connect(self.updateRoomName)
        self.threadRoomName.start()

    def loadingMood(self):
        self.TimerMood = QTimer()
        self.TimerMood.timeout.connect(self.updateMood)
        self.TimerMood.singleShot(0, self.updateMood)
        self.TimerMood.start(3600)

    def loadingSeatStatus(self):
        self.threadGetSeatStatus = ThreadGetSeatStatus()
        self.threadGetSeatStatus.res.connect(self.updateSeatStatus)
        self.threadGetSeatStatus.start()
        return

    def loadingUseTime(self):
        self.TimerUseTime = QTimer()
        self.TimerUseTime.timeout.connect(self.updateUseTime)
        self.TimerUseTime.start(1000)

    def loadingSetting(self):
        return

    # 導航控制
    def clickedClose(self):
        app = QApplication.instance()
        app.quit()

    def clickedMinimal(self):
        self.showMinimized()

    # 畫面更新
    def updateDateTime(self):
        now = datetime.datetime.now()
        self.ui.date.setText(now.strftime('%Y/%m/%d %A'))
        self.ui.time.setText(now.strftime('%H:%M:%S'))

    def updateWeather(self):
        self.threadUpdateWeather = ThreadGetWeather()
        self.threadUpdateWeather.res.connect(self.updateWeatherShow)
        self.threadUpdateWeather.start()

    def updateWeatherShow(self, res):
        self.ui.weather.setText(res)

    def updateRoomName(self, res):
        self.ui.location.setText(res+'實習室')

    def updateMood(self):
        now = datetime.datetime.now()
        hour = now.hour
        if hour == 8:
            self.ui.mood.setText('早八上班辛苦了，喝杯咖啡吧')
        elif hour == 9:
            self.ui.mood.setText('')
        elif hour == 10:
            self.ui.mood.setText('')
        elif hour == 11:
            self.ui.mood.setText('終於過了上班時間的一半了！')
        elif hour == 12:
            self.ui.mood.setText('')
        elif hour == 13:
            self.ui.mood.setText('快要下班了呦！再堅持一下！')
        elif hour == 14:
            self.ui.mood.setText('嗨，上班快樂')
        elif hour == 15:
            self.ui.mood.setText('')
        elif hour == 16:
            self.ui.mood.setText('')
        elif hour == 17:
            self.ui.mood.setText('')
        elif hour == 18:
            self.ui.mood.setText('')
        elif hour == 19:
            self.ui.mood.setText('')
        elif hour == 20:
            self.ui.mood.setText('')
        elif hour == 21:
            self.ui.mood.setText('')
        elif hour == 22:
            self.ui.mood.setText('大夜班很漫長，對吧？')
        elif hour == 23:
            self.ui.mood.setText('')
        elif hour == 24:
            self.ui.mood.setText('來數數現在天上有幾顆星星吧')
        elif hour == 1:
            self.ui.mood.setText('')
        elif hour == 2:
            self.ui.mood.setText('')
        elif hour == 3:
            self.ui.mood.setText('')
        elif hour == 4:
            self.ui.mood.setText('')
        elif hour == 5:
            self.ui.mood.setText('')
        elif hour == 6:
            self.ui.mood.setText('')
        elif hour == 7:
            self.ui.mood.setText('')

    def updateSeatStatus(self, res):

        date = datetime.datetime.now().strftime('%Y%m%d ')

        row = self.ui.seatTableLayout.rowCount()
        col = self.ui.seatTableLayout.columnCount()

        for seatStatus in res:
            flag = False
            for i in range(0, row):
                for j in range(0, col):
                    seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                    if seat != None:
                        seat = seat.widget()
                        if seat.text() != '':
                            seatNum = int(seat.text())
                            if seatNum == seatStatus[1]:
                                seat.setToolTip(seatStatus[2].strip())
                                flag = True
                    if flag == True:
                        break
                if flag == True:
                    break
            self.useTimes[seatStatus[1]-1] = datetime.datetime.strptime(
                date+seatStatus[3], '%Y%m%d %H:%M:%S')

        if self.isClassSeat():
            self.lock = 2
        elif self.isCleanTime():
            self.lock = 1

    def updateUseTime(self):
        now = datetime.datetime.now()

        if self.lock == 0:
            for i in range(0, self.ui.seatTableLayout.rowCount()):
                for j in range(0, self.ui.seatTableLayout.columnCount()):
                    seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                    if seat != None:
                        seat = seat.widget()
                        seatNum = seat.text()
                        if seatNum != '':
                            seatNum = int(seatNum)
                            if self.useTimes[seatNum-1] == None:
                                seat.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                            else:
                                diff = (
                                    now-self.useTimes[seatNum-1]).total_seconds()
                                if diff >= 7200:
                                    seat.setStyleSheet('QPushButton{border-style:none; background-color: red; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                                elif diff >= 3600:
                                    seat.setStyleSheet('QPushButton{border-style:none; background-color: orange; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                                else:
                                    seat.setStyleSheet('QPushButton{border-style:none; background-color: green; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')

    # 輸入區
    def commitAutoOnlineStuID(self):
        stuID = self.ui.autoOnlineStuID.text()

        if stuID == '' and len(self.onlineStuIDs) == 0:
            self.ui.singleOfflineSeat.setFocus(True)
        elif stuID == '':
            self.online()
        else:
            stuID = stuID.zfill(9)
            if stuID not in self.onlineStuIDs:
                self.onlineStuIDs.append(stuID)
            self.ui.autoOnlineStuID.setText('')
            self.ui.autoOnlineStatus.setText(f'您已輸入{len(self.onlineStuIDs)}人')

    def commitManyOnlineStuID(self):
        stuID = self.ui.manyOnlineStuID.text()

        if stuID == '' and len(self.onlineStuIDs) == 0:
            self.ui.manyOfflineSeatStart.setFocus(True)
        elif stuID == '':
            self.ui.manyOnlineSeatStart.setFocus(True)
        else:
            stuID = stuID.zfill(9)
            if stuID not in self.onlineStuIDs:
                self.onlineStuIDs.append(stuID)
            self.ui.manyOnlineStuID.setText('')
            self.ui.manyOnlineStuIDStatus.setText(
                f'您已輸入{len(self.onlineStuIDs)}人')

    def commitSingleOnlineStuID(self):
        stuID = self.ui.singleOnlineStuID.text()

        if stuID == '':
            self.ui.singleOfflineSeat.setFocus(True)
        else:
            stuID = stuID.zfill(9)
            self.ui.singleOnlineStuID.setText(stuID)
            self.onlineStuIDs.append(stuID)
            self.ui.singleOnlineSeat.setFocus(True)

    def commitSingleOnlineSeat(self):
        seatNum = self.ui.singleOnlineSeat.text()

        if seatNum == '':
            self.ui.singleOfflineSeat.setFocus(True)
        else:
            self.onlineSeats.append(seatNum.zfill(2))

        if len(self.onlineSeats) == len(self.onlineStuIDs):
            self.online()
            self.ui.singleOnlineStuID.setText('')
            self.ui.singleOnlineSeat.setText('')
            self.ui.singleOnlineStuID.setFocus(True)

    def commitSingleOfflineSeat(self):
        seatNum = self.ui.singleOfflineSeat.text()

        if seatNum == '':
            self.ui.autoOnlineStuID.setFocus(True)
        else:
            self.ui.singleOfflineSeat.setText('')
            seatNum = seatNum.zfill(2)
            self.offlineSeats.append(seatNum)
            self.offline()

    def commitManyOfflineSeat(self):
        if self.ui.manyOfflineSeatStart.text() != '' and self.ui.manyOfflineSeatEnd.text() != '':

            seatNumStart = int(self.ui.manyOfflineSeatStart.text())
            seatNumEnd = int(self.ui.manyOfflineSeatEnd.text())

            if self.isSeatNumValid(seatNumStart) and self.isSeatNumValid(seatNumEnd) and seatNumStart <= seatNumEnd:
                for i in range(seatNumStart, seatNumEnd+1):
                    self.offlineSeats.append(str(i).zfill(2))

                self.offline()
            else:
                print('下機失敗')

            self.ui.manyOfflineSeatStart.setText('')
            self.ui.manyOfflineSeatEnd.setText('')
            self.ui.manyOfflineSeatStart.setFocus(True)

    def commitManyOnlineSeat(self):
        if self.ui.manyOnlineSeatStart.text() != '' and self.ui.manyOnlineSeatEnd.text() != '':

            seatNumStart = int(self.ui.manyOnlineSeatStart.text())
            seatNumEnd = int(self.ui.manyOnlineSeatEnd.text())

            if self.isSeatNumValid(seatNumStart) and self.isSeatNumValid(seatNumEnd) and seatNumStart <= seatNumEnd:
                for i in range(seatNumStart, seatNumEnd+1):
                    self.onlineSeats.append(str(i).zfill(2))

                if len(self.onlineStuIDs) == len(self.onlineSeats):
                    self.online()
                else:
                    dialog = MessageDialog()
                    dialog.setTitle('錯誤訊息')
                    dialog.setMessage('請確認輸入人數與座位數量一致')
                    dialog.exec()
            else:
                dialog = MessageDialog()
                dialog.setTitle('錯誤訊息')
                dialog.setMessage('請確認輸入的座位區間合法且正確')
                dialog.exec()

            self.ui.manyOnlineSeatStart.setText('')
            self.ui.manyOnlineSeatEnd.setText('')
            self.ui.manyOnlineStuID.setFocus(True)

    # 布林判斷系列
    def isRepeat(self, stuID):
        row = self.ui.seatTableLayout.rowCount()
        col = self.ui.seatTableLayout.columnCount()

        for i in range(0, row):
            for j in range(0, col):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.toolTip() == stuID:
                        return True

        return False

    def isLeftBorder(self, i, j):
        if j == 0:
            return True
        elif self.ui.seatTableLayout.itemAtPosition(i, j-1) == None:
            return True
        elif self.ui.seatTableLayout.itemAtPosition(i, j-1).widget().text() == '':
            return True

        return False

    def isRightBorder(self, i, j):
        if j == self.ui.seatTableLayout.columnCount():
            return True
        elif self.ui.seatTableLayout.itemAtPosition(i, j+1) == None:
            return True
        elif self.ui.seatTableLayout.itemAtPosition(i, j+1).widget().text() == '':
            return True

        return False

    def isSeatNumValid(self, seatNum):
        seatMax = len(self.useTimes)
        seatNum = int(seatNum)
        if seatNum >= 1 and seatNum <= seatMax:
            return True
        return False

    def isAllSeatEmpty(self):
        for seat in self.useTimes:
            if seat != None:
                return False
        return True

    def isCleanTime(self):
        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '' and seat.toolTip() != '維修時間':
                        return False
        return True

    def isClassSeat(self):
        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '' and seat.toolTip() != '班級上機':
                        return False
        return True

    # 排位演算法
    def autoArrangeSeats(self):

        row = self.ui.seatTableLayout.rowCount()
        col = self.ui.seatTableLayout.columnCount()

        resArrange = []
        resRepeat = self.checkRepeat()

        for i in range(0, row):

            for j in range(0, col):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.toolTip() == '空位':
                        if not self.isLeftBorder(i, j):
                            flag = False
                            for l in range(0, self.interval):
                                seat = self.ui.seatTableLayout.itemAtPosition(
                                    i, j+l)
                                if seat == None:
                                    flag = True
                                    break
                                seat = seat.widget()
                                if seat.toolTip() != '空位':
                                    flag = True
                                    break
                            if flag == True:
                                continue
                            else:
                                j += self.interval

                        if self.isLeftBorder(i, j):
                            if j+len(self.onlineStuIDs) < col:
                                if not self.isRightBorder(i, j+len(self.onlineStuIDs)):
                                    flag = False
                                    for l in range(0, self.interval):
                                        seat = self.ui.seatTableLayout.itemAtPosition(
                                            i, j+len(self.onlineStuIDs)+l)
                                        if seat == None:
                                            flag = True
                                            break
                                        seat = seat.widget()
                                        if seat.toolTip() != '空位':
                                            flag = True
                                            break
                                    if flag == True:
                                        continue
                            else:
                                break
                        else:
                            if j+len(self.onlineStuIDs)-1 < col:

                                if not self.isRightBorder(i, j+len(self.onlineStuIDs)-1):
                                    flag = False
                                    for l in range(0, self.interval):
                                        seat = self.ui.seatTableLayout.itemAtPosition(
                                            i, j+len(self.onlineStuIDs)+l)
                                        if seat == None:
                                            flag = True
                                            break
                                        seat = seat.widget()
                                        if seat.toolTip() != '空位':
                                            flag = True
                                            break

                                    if flag == True:
                                        continue
                            else:
                                break

                        for l in range(0, len(self.onlineStuIDs)):

                            seat = self.ui.seatTableLayout.itemAtPosition(
                                i, j+l)
                            if seat == None:
                                resArrange.clear()
                                break
                            seat = seat.widget()
                            if seat.toolTip() != '空位':
                                resArrange.clear()
                                break
                            else:
                                resArrange.append(
                                    ['N', self.onlineStuIDs[l], seat.text(), i, j+l])

                if len(resArrange) == len(self.onlineStuIDs):
                    break
            if len(resArrange) == len(self.onlineStuIDs):
                break

        if len(resArrange) == 0:
            for stuID in self.onlineStuIDs:
                resArrange.append(['F', stuID, '', -1, -1])

        self.onlineStuIDs.clear()
        self.ui.autoOnlineStatus.setText(f'您已輸入{len(self.onlineStuIDs)}人')

        return resRepeat+resArrange

    def manualArrangeSeats(self):
        resArrange = []
        resRepeat = self.checkRepeat()

        for i in range(0, len(self.onlineStuIDs)):
            position = self.getPositionBySeatNum(self.onlineSeats[i])
            seat = self.ui.seatTableLayout.itemAtPosition(
                position[0], position[1]).widget()
            if seat.toolTip() == '空位':
                resArrange.append(
                    ['N', self.onlineStuIDs[i], seat.text(), position[0], position[1]])
            else:
                resArrange.append(
                    ['P', self.onlineStuIDs[i], seat.text(), position[0], position[1]])

        self.onlineStuIDs.clear()
        self.onlineSeats.clear()

        return resRepeat+resArrange
    # 上機下機

    def online(self):
        if self.lock == 0:
            if len(self.onlineSeats) == 0:
                arrangements = self.autoArrangeSeats()
            else:
                arrangements = self.manualArrangeSeats()

            print(arrangements)

            for arrangement in arrangements:
                if arrangement[0] == 'R' or arrangement[0] == 'P' or arrangement[0] == 'F':
                    continue
                seat = self.ui.seatTableLayout.itemAtPosition(
                    arrangement[3], arrangement[4]).widget()
                seat.setToolTip(arrangement[1])
                seat.setStyleSheet('QPushButton{border-style:none; background-color: green; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                self.useTimes[int(arrangement[2])-1] = datetime.datetime.now()

                self.runningThread.append(ThreadOnlineComputer(
                    arrangement[1], int(arrangement[2])))
                self.runningThread[-1].finished.connect(
                    self.threadFinishedOnlineComputer)
                self.runningThread[-1].start()

            res = numpy.delete(arrangements, [3, 4], axis=1)
            self.showOnlineResult(res)
        elif self.lock == 1:
            dialog = MessageDialog()
            dialog.setTitle('錯誤訊息')
            dialog.setMessage('請先解除維修時間')
            self.onlineSeats.clear()
            self.onlineStuIDs.clear()
            dialog.exec()

        elif self.lock == 2:
            dialog = MessageDialog()
            dialog.setTitle('錯誤訊息')
            dialog.setMessage('請先解除班級上機')
            self.onlineSeats.clear()
            self.onlineStuIDs.clear()
            dialog.exec()

    def offline(self):
        if self.lock == 0:
            for seatNum in self.offlineSeats:
                if self.isSeatNumValid(seatNum):
                    for i in range(0, self.ui.seatTableLayout.rowCount()):
                        for j in range(0, self.ui.seatTableLayout.columnCount()):
                            seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                            if seat != None:
                                seat = seat.widget()
                                if seat.text() == seatNum:

                                    self.runningThread.append(
                                        ThreadOfflineComputer(seat.toolTip(), int(seatNum)))
                                    self.runningThread[-1].finished.connect(
                                        self.threadFinishedOfflineComputer)
                                    self.runningThread[-1].start()

                                    seat.setToolTip('空位')
                                    seat.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                                    self.useTimes[int(seatNum)-1] = None
            self.offlineSeats.clear()
        elif self.lock == 1:
            dialog = MessageDialog()
            dialog.setTitle('錯誤訊息')
            dialog.setMessage('請先解除維修時間')
            self.offlineSeats.clear()
            dialog.exec()
        elif self.lock == 2:
            dialog = MessageDialog()
            dialog.setTitle('錯誤訊息')
            dialog.setMessage('請先解除班級上機')
            self.offlineSeats.clear()
            dialog.exec()

    def showOnlineResult(self, res):
        output = ''

        for item in res:
            if item[0] == 'N':
                output += item[1]+"：排位結果座號為"+item[2]+"號"
            elif item[0] == 'R':
                output += item[1]+"：重複排位，該名學生目前上機座號為"+item[2]+"號"
            elif item[0] == 'P':
                output += item[1]+"：指定位置"+item[2]+"號目前非空位，請查核"
            elif item[0] == 'F':
                output += item[1]+"：排位失敗，目前並無符合設定之空位"
            output += '\n'
        dialog = MessageDialog()
        dialog.setTitle('座位分配結果')
        dialog.setMessage('下列為本次上機分發結果：\n\n'+output)
        dialog.exec()

    def classOnline(self):
        return

    def classOffline(self):
        return

    def cleanOnline(self):
        self.runningThread.append(
            ThreadCleanOnlineComputer(len(self.useTimes)))
        self.runningThread[-1].finished.connect(
            self.threadFinishedCleanOnlineComputer)
        self.runningThread[-1].start()

        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '':
                        seat.setToolTip('維修時間')
                        seat.setStyleSheet('QPushButton{border-style:none; background-color: red; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                        self.useTimes[int(seat.text()) -
                                      1] = datetime.datetime.now()

    def cleanOffline(self):

        # 這裡要補維修時間下機程式碼

        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '':
                        seat.setToolTip('空位')
                        seat.setStyleSheet('QPushButton{border-style:none; background-color: white; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:hover{border-style:none; background-color: #EEEEEE; border-radius: 5px; border: 1px solid black; padding: 5px;} QPushButton:pressed{border-style:none; background-color: #999999; border-radius: 5px; border: 1px solid black; padding: 5px;}')
                        self.useTimes[int(seat.text()) -
                                      1] = None

        return

    def allOffline(self):
        self.offlineSeats.clear()
        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.toolTip() != '空位' and seat.text() != '':
                        self.offlineSeats.append(seat.text())
        self.offline()

    def exchangeSeat(self, fromSeatNum):
        toSeatNum = self.sender().text()

        if toSeatNum != fromSeatNum:
            fromSeatPosition = self.getPositionBySeatNum(fromSeatNum)
            toSeatPosition = self.getPositionBySeatNum(toSeatNum)

            fromSeat = self.ui.seatTableLayout.itemAtPosition(
                fromSeatPosition[0], fromSeatPosition[1]).widget()
            toSeat = self.ui.seatTableLayout.itemAtPosition(
                toSeatPosition[0], toSeatPosition[1]).widget()

            self.offlineSeats.clear()
            self.onlineSeats.clear()
            self.onlineStuIDs.clear()

            if fromSeat.toolTip() == '空位' and toSeat.toolTip() == '空位':
                return
            elif fromSeat.toolTip() == '空位' and toSeat.toolTip() != '空位':
                self.offlineSeats.append(toSeatNum)
                self.onlineSeats.append(fromSeatNum)
                self.onlineStuIDs.append(toSeat.toolTip())
                self.offline()
                self.online()
            elif fromSeat.toolTip() != '空位' and toSeat.toolTip() == '空位':
                self.offlineSeats.append(fromSeatNum)
                self.onlineSeats.append(toSeatNum)
                self.onlineStuIDs.append(fromSeat.toolTip())
                self.offline()
                self.online()
            elif fromSeat.toolTip() != '空位' and toSeat.toolTip() != '空位':

                stuID1 = fromSeat.toolTip()
                stuID2 = toSeat.toolTip()

                self.offlineSeats.append(fromSeatNum)
                self.offlineSeats.append(toSeatNum)
                self.offline()

                self.onlineStuIDs.append(stuID1)
                self.onlineSeats.append(toSeatNum)
                self.onlineStuIDs.append(stuID2)
                self.onlineSeats.append(fromSeatNum)
                self.online()

    # 網路線程結束區

    def threadFinishedOnlineComputer(self):
        sender = self.sender()
        self.runningThread.remove(sender)

    def threadFinishedOfflineComputer(self):
        sender = self.sender()
        self.runningThread.remove(sender)

    def threadFinishedCleanOnlineComputer(self):
        sender = self.sender()
        self.runningThread.remove(sender)

    # UI用戶交互介面區 - 特定按鍵點擊
    def keyRightPressedAutoOnlineStuID(self):
        self.ui.singleOnlineStuID.setFocus(True)

    def keyLeftPressedAutoOnlineStuID(self):
        self.ui.singleOfflineSeat.setFocus(True)

    def keyRightPressedSingleOnlineStuID(self):
        self.ui.singleOnlineSeat.setFocus(True)

    def keyLeftPressedSingleOnlineStuID(self):
        self.ui.autoOnlineStuID.setFocus(True)

    def keyDownPressedSingleOnlineStuID(self):
        self.ui.manyOnlineStuID.setFocus(True)

    def keyLeftPressedSingleOnlineSeat(self):
        self.ui.singleOnlineStuID.setFocus(True)

    def keyRightPressedSingleOnlineSeat(self):
        self.ui.singleOfflineSeat.setFocus(True)

    def keyLeftPressedSingleOfflineSeat(self):
        self.ui.singleOnlineSeat.setFocus(True)

    def keyRightPressedSingleOfflineSeat(self):
        self.ui.autoOnlineStuID.setFocus(True)

    def keyDownPressedSingleOfflineSeat(self):
        self.ui.manyOfflineSeatStart.setFocus(True)

    def keyDownPressedSingleOnlineSeat(self):
        self.ui.manyOnlineSeatStart.setFocus(True)

    def keyLeftPressedManyOnlineStuID(self):
        self.ui.manyOfflineSeatEnd.setFocus(True)

    def keyUpPressedManyOnlineStuID(self):
        self.ui.singleOnlineStuID.setFocus(True)

    def keyRightPressedManyOnlineStuID(self):
        self.ui.manyOnlineSeatStart.setFocus(True)

    def keyUpPressedManyOnlineSeatStart(self):
        self.ui.singleOnlineSeat.setFocus(True)

    def keyRightPressedManyOnlineSeatStart(self):
        self.ui.manyOnlineSeatEnd.setFocus(True)

    def keyLeftPressedManyOnlineSeatStart(self):
        self.ui.manyOnlineStuID.setFocus(True)

    def keyRightPressedManyOnlineSeatEnd(self):
        self.ui.manyOfflineSeatStart.setFocus(True)

    def keyLeftPressedManyOnlineSeatEnd(self):
        self.ui.manyOnlineSeatStart.setFocus(True)

    def keyUpPressedManyOnlineSeatEnd(self):
        self.ui.singleOnlineSeat.setFocus(True)

    def keyUpPressedManyOfflineSeatEnd(self):
        self.ui.singleOfflineSeat.setFocus(True)

    def keyLeftPressedManyOfflineSeatEnd(self):
        self.ui.manyOfflineSeatStart.setFocus(True)

    def keyRightPressedManyOfflineSeatEnd(self):
        self.ui.manyOnlineStuID.setFocus(True)

    def keyUpPressedManyOfflineSeatStart(self):
        self.ui.singleOfflineSeat.setFocus(True)

    def keyRightPressedManyOfflineSeatStart(self):
        self.ui.manyOfflineSeatEnd.setFocus(True)

    def keyLeftPressedManyOfflineSeatStart(self):
        self.ui.manyOnlineSeatEnd.setFocus(True)

    # UI用戶交互介面區 - cancel
    def cancelAutoOnlineStuID(self):
        self.onlineStuIDs.clear()
        self.ui.autoOnlineStatus.setText(f'您已輸入{len(self.onlineStuIDs)}人')

    def cancelManyOnlineStuID(self):
        self.onlineStuIDs.clear()
        self.ui.manyOnlineStuIDStatus.setText(f'您已輸入{len(self.onlineStuIDs)}人')

    # UI用戶交互介面區 - focused

    def focusedSingleOnlineStuID(self):
        self.onlineStuIDs.clear()
        self.onlineSeats.clear()

    def focusedSingleOnlineSeat(self):
        self.onlineSeats.clear()

    def focusedSingleOfflineSeat(self):
        self.offlineSeats.clear()

    def focusedManyOnlineSeatStart(self):
        self.onlineSeats.clear()

    def focusedManyOnlineSeatEnd(self):
        self.onlineSeats.clear()

    def focusedManyOfflineSeatStart(self):
        self.offlineSeats.clear()

    def focusedManyOfflineSeatEnd(self):
        self.offlineSeats.clear()

    # UI用戶交互介面區 - clicked

    def clickedLogout(self):
        dialog = MessageDialog()
        dialog.setMessage('請確認是否登出')
        dialog.setTitle('提示訊息')
        if dialog.exec():
            global window
            window.hide()
            window = Login()
            window.show()

    def clickedSeatTime(self):
        data = []
        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() != '' and seat.toolTip() != '空位':
                        time = datetime.datetime.now(
                        )-self.useTimes[int(seat.text())-1]
                        strTime = f'{time.days:02d}天{time.seconds//3600:02d}時{(time.seconds//60)%60:02d}分'
                        data.append((seat.toolTip(), seat.text(), strTime))

        dialog = UseTimeDialog(data)
        dialog.exec()

    def clickedClassSeat(self):
        if self.lock == 0:
            dialog = MessageDialog()
            dialog.setTitle('提示訊息')
            dialog.setMessage('請問確認是否班級上機')
            if dialog.exec():
                if self.isAllSeatEmpty():
                    self.classOnline()
                    self.lock = 2
                    self.ui.classSeat.setToolTip('班級下機')
                else:
                    dialog = MessageDialog()
                    dialog.setTitle('錯誤訊息')
                    dialog.setMessage('請確認所有座位為空')
                    dialog.exec()
        elif self.lock == 2:
            dialog = MessageDialog()
            dialog.setTitle('提示訊息')
            dialog.setMessage('請問是否班級下機')
            if dialog.exec():
                self.classOffline()
                self.lock = 0
                self.ui.classSeat.setToolTip('班級上機')
        elif self.lock == 1:
            dialog = MessageDialog()
            dialog.setTitle('錯誤訊息')
            dialog.setMessage('請先關閉維修時間')
            dialog.exec()

    def clickedClear(self):
        dialog = MessageDialog()
        dialog.setTitle('提示訊息')
        dialog.setMessage('請問是否確認清空所有上機狀況')
        if dialog.exec():
            self.allOffline()

    def clickedClean(self):
        if self.lock == 0:
            dialog = MessageDialog()
            dialog.setTitle('提示訊息')
            dialog.setMessage('請問是否進入維修時間')
            if dialog.exec():
                if self.isAllSeatEmpty():
                    res = self.cleanOnline()
                    self.lock = 1
                    self.ui.clean.setToolTip('關閉維修')
                else:
                    dialog = MessageDialog()
                    dialog.setTitle('錯誤訊息')
                    dialog.setMessage('請確認所有位置為空')
                    dialog.exec()
        elif self.lock == 1:
            dialog = MessageDialog()
            dialog.setTitle('提示訊息')
            dialog.setMessage('請問是否關閉維修時間')
            if dialog.exec():
                self.cleanOffline()
                self.lock = 0
                self.ui.clean.setToolTip('維修時間')
        elif self.lock == 2:
            dialog = MessageDialog()
            dialog.setTitle('錯誤訊息')
            dialog.setMessage('請先解除班級上機')
            dialog.exec()
    # UI用戶交互介面區 - returnPressed

    def returnPressedManyOnlineSeatStart(self):
        self.ui.manyOnlineSeatEnd.setFocus(True)

    def returnPressedManyOfflineSeatStart(self):
        if self.ui.manyOfflineSeatStart.text() == '':
            self.ui.manyOnlineStuID.setFocus(True)
        else:
            self.ui.manyOfflineSeatEnd.setFocus(True)

    # 其他

    def getRepeatSeat(self, stuID):
        row = self.ui.seatTableLayout.rowCount()
        col = self.ui.seatTableLayout.columnCount()

        for i in range(0, row):
            for j in range(0, col):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.toolTip() == stuID:
                        return [i, j]

        return [-1, -1]

    def getPositionBySeatNum(self, num):
        for i in range(0, self.ui.seatTableLayout.rowCount()):
            for j in range(0, self.ui.seatTableLayout.columnCount()):
                seat = self.ui.seatTableLayout.itemAtPosition(i, j)
                if seat != None:
                    seat = seat.widget()
                    if seat.text() == num:
                        return [i, j]

    def checkRepeat(self):
        res = []

        for stuID in self.onlineStuIDs:
            if self.isRepeat(stuID):
                repeatSeat = self.getRepeatSeat(stuID)
                repeatSeatNum = self.ui.seatTableLayout.itemAtPosition(
                    repeatSeat[0], repeatSeat[1]).widget().text()
                res.append(['R', stuID, repeatSeatNum]+repeatSeat)

        for repeatStuID in res:
            if repeatStuID[1] in self.onlineStuIDs:
                self.onlineStuIDs.remove(repeatStuID[1])

        return res

    # 重載方法

    def mousePressEvent(self, event):
        self.pressX = event.x()
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        moveX = x-self.pressX
        moveY = y-self.pressY
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY
        self.move(positionX, positionY)

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

# 登入頁面


class Login(QMainWindow):

    def __init__(self):
        super(Login, self).__init__()
        self.initUI()
        self.initInteraction()

    def initUI(self):
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle('淡江大學 實習上機系統')
        img = base64.b64decode(tku)
        self.setWindowIcon(QtGui.QIcon(self.svg2pixmap(img, QSize(512, 512))))

    def initInteraction(self):
        self.ui.close.clicked.connect(self.clickedClose)
        self.ui.login.clicked.connect(self.clickedLogin)

    def clickedClose(self):
        app = QApplication.instance()
        app.quit()

    def clickedLogin(self):

        self.ui.loading.setVisible(True)

        stuID = self.ui.username.text()
        stuPWD = self.ui.password.text()

        if stuID == '' and stuPWD == '':
            self.statusSet(5)
        elif stuID == '':
            self.statusSet(6)
        elif stuPWD == '':
            self.statusSet(7)
        else:
            self.threadLogin = ThreadLogin(stuID, stuPWD)
            self.threadLogin.res.connect(self.statusSet)
            self.threadLogin.start()

    def statusSet(self, code):
        if code == 0:
            self.ui.status.setText('登入成功，請等候跳轉')
            global window
            window.hide()
            window = ManagementSystem()
            window.show()
        elif code == 1:
            self.ui.status.setText('資料未成功傳遞至伺服器，請重試')
        elif code == 2:
            self.ui.status.setText('帳號或密碼錯誤，請重試')
        elif code == 3:
            self.ui.status.setText('帳號或密碼錯誤，請重試')
        elif code == 4:
            self.ui.status.setText('發生未知錯誤，請聯絡開發人員')
        elif code == 5:
            self.ui.status.setText('請輸入帳號及密碼')
        elif code == 6:
            self.ui.status.setText('請輸入帳號')
        elif code == 7:
            self.ui.status.setText('請輸入密碼')

        self.ui.status.adjustSize()
        self.ui.status.setGeometry(QRect(int(250-self.ui.status.width()/2),
                                         350, int(self.ui.status.width()), int(self.ui.status.height())))

        self.ui.loading.setVisible(False)

    def mousePressEvent(self, event):
        self.pressX = event.x()
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        moveX = x-self.pressX
        moveY = y-self.pressY
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY
        self.move(positionX, positionY)

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

# 閃屏頁面


class Splash(QWidget):

    def __init__(self):
        super(Splash, self).__init__()
        self.initUI()
        self.initSplash()

    def initUI(self):
        self.ui = Ui_Splash()
        self.ui.setupUi(self)
        self.setWindowTitle('淡江大學 實習上機系統')
        img = base64.b64decode(tku)
        self.setWindowIcon(QtGui.QIcon(self.svg2pixmap(img, QSize(512, 512))))

    def initSplash(self):
        QTimer.singleShot(5000, self.splash)

    def splash(self):
        global window
        window.hide()
        window = Login()
        window.show()

    def mousePressEvent(self, event):
        self.pressX = event.x()
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        moveX = x-self.pressX
        moveY = y-self.pressY
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY
        self.move(positionX, positionY)

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


# QThread線程區
class ThreadLogin(QThread):

    res = pyqtSignal(int)

    def __init__(self, stuID, stuPWD):
        super(ThreadLogin, self).__init__()
        self.stuID = stuID
        self.stuPWD = stuPWD

    def run(self):
        db = ServerDB()
        code = db.checkAccount(self.stuID, self.stuPWD)
        self.res.emit(code)


class ThreadOnlineComputer(QThread):

    res = pyqtSignal(int)

    def __init__(self, stuID, seatNum):
        super(ThreadOnlineComputer, self).__init__()
        self.stuID = stuID
        self.seatNum = seatNum

    def run(self):

        print('online結束')
        #db = ServerDB()
        #resultCode = db.onlineComputer(self.stuID, self.seatNum)
        # self.res.emit(resultCode)


class ThreadOfflineComputer(QThread):

    res = pyqtSignal(int)

    def __init__(self, stuID, seatNum):
        super(ThreadOfflineComputer, self).__init__()
        self.stuID = stuID
        self.seatNum = seatNum

    def run(self):

        print('offline結束')
        #db = ServerDB()
        #resultCode = db.offlineComputer(self.stuID, self.seatNum)
        # self.res.emit(resultCode)


class ThreadCleanOnlineComputer(QThread):

    res = pyqtSignal(int)

    def __init__(self, total):
        super(ThreadCleanOnlineComputer, self).__init__()
        self.total = total

    def run(self):
        resultCode = 0
        #db = ServerDB()
        # for i in range(1, self.total+1):
        #    resultcode = db.onlineComputer('維修時間', i)
        # self.res.emit(resultcode)


class ThreadGetSeatStatus(QThread):

    res = pyqtSignal(list)

    def __init__(self):
        super(ThreadGetSeatStatus, self).__init__()

    def run(self):
        db = ServerDB()
        seatStatus = db.getSeatStatus()
        self.res.emit(seatStatus)


class ThreadGetRoomName(QThread):
    res = pyqtSignal(str)

    def __init__(self):
        super(ThreadGetRoomName, self).__init__()

    def run(self):
        db = ServerDB()
        roomName = db.getClassroomName()
        self.res.emit(roomName)


class ThreadGetWeather(QThread):

    res = pyqtSignal(str)

    def __init__(self):
        super(ThreadGetWeather, self).__init__()

    def run(self):
        apiKey = 'CWB-21FCA0DA-65E9-484E-AAE1-1F03A2D66022'

        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-071' + '?Authorization=' + apiKey + '&limit=' + \
            '1' + '&offset=' + '0' + '&locationName=' + '%E6%B7%A1%E6%B0%B4%E5%8D%80' + \
            '&elementName=' + 'Wx' + '&sort=' + 'time'
        response = requests.get(url)

        if response.status_code == 200:
            response = response.json()
            weatherDesc = response['records']['locations'][0]['location'][0][
                'weatherElement'][0]['time'][0]['elementValue'][0]['value']
            self.res.emit(weatherDesc)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./icon/tku.svg'))
    window = Splash()
    window.show()

    exit(app.exec_())
