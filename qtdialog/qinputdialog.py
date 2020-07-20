import sys
from PyQt5.QtWidgets import (QWidget, QLineEdit, QPushButton,
                             QInputDialog, QApplication, QFrame, QColorDialog)
from PyQt5.QtGui import QColor

class Example (QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def  initUI(self):

        COL = QColor(0,0,0)
        self.btn = QPushButton('dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showdialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % COL.name()
                               )
        self.frm.setGeometry(130,22,100,100)

        self.le = QLineEdit(self)
        self.le.move(130,22)
        self.setGeometry(500,500,590,550)
        self.setWindowTitle('input dialog')
        self.show()


    def showdialog(self ):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

        text , ok = QInputDialog.getText(self,'input dialog','enter your name'
                                         )
        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())