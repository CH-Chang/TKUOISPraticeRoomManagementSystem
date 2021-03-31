from PyQt5 import QtWidgets, QtGui, QtCore


class QLineEdit(QtWidgets.QLineEdit):

    focused = QtCore.pyqtSignal()
    unfocused = QtCore.pyqtSignal()
    keyDownPressed = QtCore.pyqtSignal()
    keyUpPressed = QtCore.pyqtSignal()
    keyRightPressed = QtCore.pyqtSignal()
    keyLeftPressed = QtCore.pyqtSignal()
    keyDeletePressed = QtCore.pyqtSignal()

    def __init__(self):
        super(QLineEdit, self).__init__()

    def focusInEvent(self, e):
        self.focused.emit()
        return super().focusInEvent(e)

    def focusOutEvent(self, e):
        self.unfocused.emit()
        return super().focusOutEvent(e)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Down:
            self.keyDownPressed.emit()
        elif e.key() == QtCore.Qt.Key_Up:
            self.keyUpPressed.emit()
        elif e.key() == QtCore.Qt.Key_Left:
            self.keyLeftPressed.emit()
        elif e.key() == QtCore.Qt.Key_Right:
            self.keyRightPressed.emit()
        elif e.key() == QtCore.Qt.Key_Delete:
            self.keyDeletePressed.emit()
        else:
            super().keyPressEvent(e)
