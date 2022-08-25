import sys
import os
import traceback
import threading

from PyQt5.QtGui import QFontDatabase, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from asyncqt import asyncSlot

from gui.MainFrame import MainFrame




class GUI(QMainWindow):

    title = 'Bert the Bard'

    #Window dimentions
    _x = 150
    _y = 150
    w = 1200
    h = 800

    _gripSize = 4

    def __init__(self, app):
        super().__init__()

        self.app = app

        self.setObjectName('GUI')

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        statusbar = QStatusBar(self)
        statusbar.setSizeGripEnabled(True)
        statusbar.setFixedHeight(14)
        self.setStatusBar(statusbar)
        statusbar.setObjectName('statusbar')
        

        #add Roboto font
        QFontDatabase.addApplicationFont('Roboto-Regular.ttf')
        

        #Load stylesheet from qss
        qss="style.qss"
        with open(qss,"r") as fh:
            self.style = fh.read()
            self.setStyleSheet(self.style)


        self.maxim = False

        self.setContentsMargins(10,10,10,10)
        
        shadow = QGraphicsDropShadowEffect()
  
        shadow.setBlurRadius(20)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,100))
        self.setGraphicsEffect(shadow)


        
        self.initUI()


        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self._x, self._y, self.w, self.h)

        #set MainFrame as central widget
        self.main_frame = MainFrame(self)
        self.setCentralWidget(self.main_frame)
        
        self.show()
        

    def getGUI(self):
        return self

    def getApp(self):
        return self.app

    def showAlert(self, alert):
        self.main_frame.showAlert(alert)

    def removeAlert(self, alert):
        self.main_frame.removeAlert(alert)

    

    def setContent(self, title):
        
        self.main_frame.setContent(title)



    def _maximize(self):
        try:
            if self.maxim:
                
                self.showNormal()
                self.statusBar().show()
                
                self.setContentsMargins(20,20,20,20)

                shadow = QGraphicsDropShadowEffect()
  
                shadow.setBlurRadius(20)
                shadow.setOffset(2,2)
                shadow.setColor(QColor(10,10,10,100))
                self.setGraphicsEffect(shadow)

                
            else:
                self.showMaximized()
                self.statusBar().hide()
                self.setContentsMargins(0,0,0,0)
                self.setGraphicsEffect(None)
        except Exception as e:
            print(e)
            
            
        self.maxim = self.maxim == False
        
    def _minimize(self):
        self.showMinimized()


    def _quit(self):
        self.app.quit()

    def setLogger(self, logger):
        self.logger = logger
        

        

        



