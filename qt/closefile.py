import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('quit', self)

        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('quit button')
        self.show()

    def closeEvent(self, a0):
        reply = QMessageBox.question(self, 'message', "are you sure to quit",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
