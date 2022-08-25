from PyQt5.QtWidgets import QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QTextCursor


import time
import datetime


from gui.RootFrame import RootFrame


class Logger(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName('loggerFrame')

        self.log_queue = []

        self.initUI()

        


        self._update_timer = QTimer()
        self._update_timer.timeout.connect(self.loop)
        self._update_timer.start(100) # milliseconds

    def initUI(self):
        self.initLayout()
        self.initWidgets()

        self.layout.addWidget(self.log_textEdit)
        self.setLayout(self.layout)

    def initLayout(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(0)

    def initWidgets(self):
        font = QFont("Roboto", 12)

        self.log_textEdit = QTextEdit(self)
        self.log_textEdit.setReadOnly(True)
        #self.log_textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.log_textEdit.setFont(font)

        self.log_textEdit.setObjectName('logger')

    def log(self, sender, text):
        self.log_queue.append((sender,text))


    def loop(self):
        while len(self.log_queue) > 0:
            sender, txt = self.log_queue.pop(0)
            self.addLog(sender, txt)

    def getTimeStamp(self):
        time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
        return time_stamp

    def addLog(self, sender, text):

        log_str = '[{}] [{}] {}\n'.format(self.getTimeStamp(), sender, text)


        self.log_textEdit.moveCursor(QTextCursor.End)
        self.log_textEdit.insertPlainText(log_str)

        sb = self.log_textEdit.verticalScrollBar()
        sb.setValue(sb.maximum())

    def rawLog(self, text):
        log_str = '{}\n'.format(text)

        self.log_textEdit.moveCursor(QTextCursor.End)
        self.log_textEdit.insertPlainText(log_str)

        sb = self.log_textEdit.verticalScrollBar()
        sb.setValue(sb.maximum())