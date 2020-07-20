from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.q

class Status:

    def __init__(self):
        qfile_status = QFile("ui/status")
        qfile_status.open(QFile.ReadOnly )
        qfile_status.close()

        self.ui = QUiLoader()