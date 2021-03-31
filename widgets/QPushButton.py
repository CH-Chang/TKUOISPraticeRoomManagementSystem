from PyQt5 import QtWidgets, QtGui, QtCore


class QPushButton(QtWidgets.QPushButton):

    dropped = QtCore.pyqtSignal(str)

    def __init__(self):
        super(QPushButton, self).__init__()
        self.setAcceptDrops(True)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            drag = QtGui.QDrag(self)

            mimeData = QtCore.QMimeData()
            mimeData.setText(self.text())
            drag.setMimeData(mimeData)

            dropAction = drag.exec_(QtCore.Qt.MoveAction)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        fromSeat = e.mimeData().text()
        self.dropped.emit(fromSeat)
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
