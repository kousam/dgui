import sys
import os
import traceback
import threading

from PyQt5.QtGui import QFontDatabase, QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QFrame ,QLabel,QPushButton
from PyQt5.QtCore import Qt, QCoreApplication, QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
from asyncqt import asyncSlot

import asyncio
from asyncqt import QEventLoop

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import sys
import os
import subprocess


from dg.DExtra import DShadow
from dg.DLayout import DHBoxLayout, DVBoxLayout,DStackedLayout
from dg.DMaterials import DMaterialsContainer, DBuildMaterials, DBuildMaterials
from dg.DWidgets import DSideBarHomeButton, DSideBarButton



class DObject():
    def __init__(self):
        self.materials = DMaterialsContainer()

    def addMaterials(self, mats):
        self.materials.add(mats)
        
    def requireAttributes(self, required_attributes):
        for required_attribute in required_attributes:
            if required_attribute not in self.materials.__dict__:
                raise Exception('Missing required attribute "{}"'.format(required_attribute))

    def unpack(self):
        self.materials.unpack()

    def build(self):
        self.materials.unpack()
        print('unpacking')

        self.prepare()

    def prepare(self):
        print('super prepare')
        return

    def initUI(self):
        return


class DUIObject(DObject):
    def __init__(self):
        super().__init__()
    
    def build(self):
        super().build()

        #print('building: ' + self.materials.name)

        print('here')

        self.initUI()



class DWindow(QMainWindow, DUIObject):
    def __init__(self):
        super().__init__()
        
        self.isMaximized = False

    def prepare(self):
        
        super().prepare()
        #sidebar

        self.app = self.materials.app

        sidebar_mats = DBuildMaterials()
        sidebar_mats.name = 'side_bar'

        self.sidebar = DSideBar(self)
        self.sidebar.addMaterials(sidebar_mats)

        content_frame_mats = DBuildMaterials()
        content_frame_mats.name = 'content_frame'
        self.content_frame = DContentFrame(self)
        self.content_frame.addMaterials(content_frame_mats)

        inner_frame_mats = DBuildMaterials()
        inner_frame_mats.name = 'inner_frame'
        inner_frame_mats.sidebar = self.sidebar
        inner_frame_mats.content_frame = self.content_frame
        inner_frame = DInnerFrame(self)
        inner_frame.addMaterials(inner_frame_mats)

        #main frame
        main_frame_mats = DBuildMaterials()
        main_frame_mats.name = 'main_frame'
        main_frame_mats.title = self.materials.title
        main_frame_mats.inner_frame = inner_frame
        self.main_frame = DMainFrame(self)
        self.main_frame.addMaterials(main_frame_mats)
        

    def build(self):
        super().build()

        self.requireAttributes(['name', 'font', 'title', 'rect', 'style']);

        self.setObjectName(self.materials.name)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #add Roboto font
        QFontDatabase.addApplicationFont(self.materials.font)
        
        self.setStyleSheet(self.materials.style)

        self.setContentsMargins(10,10,10,10)
        self.setGraphicsEffect(DShadow())
        
        self.setWindowTitle(self.materials.title)
        x,y,w,h = self.materials.rect
        self.setGeometry(x,y,w,h)
        
        statusbar = DStatusBar(self)
        self.setStatusBar(statusbar)

        self.main_frame.build()

        self.setCentralWidget(self.main_frame)

        for tab in self.materials.tabs:
            self.addTab(tab)
        
        self.show()   

    def getGUI(self):
        return self

    def getApp(self):
        return self.app

    def showAlert(self, alert):
        self.main_frame.showAlert(alert)

    def removeAlert(self, alert):
        self.main_frame.removeAlert(alert)


    def setContent(self, content):
        print('yo')
        self.content_frame.setContent(content)


    def _maximize(self):
        try:
            if self.isMaximized:
                
                self.showNormal()
                self.statusBar().show()
                
                self.setContentsMargins(20,20,20,20)

                self.setGraphicsEffect(DShadow)

                
            else:
                self.showMaximized()
                self.statusBar().hide()
                self.setContentsMargins(0,0,0,0)
                self.setGraphicsEffect(None)
        except Exception as e:
            print(e)
            
            
        self.isMaximized = self.isMaximized == False
        
    def _minimize(self):
        self.showMinimized()


    def _quit(self):
        self.app.quit()

    def setLogger(self, logger):
        self.logger = logger
        
    def addTab(self, title):
        self.sidebar.addTab(title)

class DStatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName('statusbar')
        self.setSizeGripEnabled(True)
        self.setFixedHeight(14)
        

class DFrame(QFrame, DUIObject):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        DObject.__init__(self)

        self.parent = parent

    def build(self):
        super().build()
        self.setObjectName(self.materials.name)

    def getGUI(self):
        return self.parent.getGUI()

    def getParent(self):
        return self.parent

    def getApp(self):
        return self.parent.getApp()
        
    def highlight(self):
        self.setStyleSheet("background-color: rgb(200, 100, 100)")
        


class DMainFrame(DFrame):

    def __init__(self, parent):
        super().__init__(parent)

    def build(self):
        super().build()
        
        
        self.layout = DVBoxLayout()

        
        self.topBar_frame = DTopbar(self)

        topbar_mats = DBuildMaterials()
        topbar_mats.name = 'top_bar'
        topbar_mats.title = self.materials.title

        self.topBar_frame.addMaterials(topbar_mats)
        self.topBar_frame.build()

        self.materials.inner_frame.build()
        

        #self.content_frame = QFrame()
        #self.content_layout = DStackedLayout()

        #self.content_frame.setLayout(self.content_layout)
        
        #self.layout2.addWidget(self.content_frame)

        self.layout.addWidget(self.topBar_frame)
        self.layout.addWidget(self.materials.inner_frame)


        self.setLayout(self.layout)


class DInnerFrame(DFrame):
    BUILD_REQUIREMENTS = ['sidebar']

    def __init__(self, parent):
        super().__init__(parent)
    
    def build(self):
        super().build()

        self.requireAttributes([])

        self.layout = DHBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)

        self.materials.sidebar.build()
        self.materials.content_frame.build()

        self.layout.addWidget(self.materials.sidebar)
        self.layout.addWidget(self.materials.content_frame)

        
          

class DContentFrame(DFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tabs = []
        self.count = 0

    def build(self):
        super().build()
    

        self.layout = DStackedLayout()
        self.setLayout(self.layout)
        print('conbfewsf')

        self.setObjectName('test')

    def setContent(self, tab):
        print('yo')
        if tab not in self.tabs:
            tab.build()
            print('tab')
            print(self.layout)
            self.layout.insertWidget(self.count, tab)
            self.count += 1

        self.layout.setCurrentWidget(tab)


class DTopbar(DFrame):
    HEIGHT = 32
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.maximized = False
    
    def build(self):
        super().build()
        

        self.requireAttributes(['name', 'title'])

        self.setFixedHeight(self.HEIGHT)
        self.setObjectName(self.materials.name)

        self.initLayout()
        self.initWidgets()
        
        self.layout.addWidget(self.title_label, alignment=Qt.AlignLeft)
        self.layout.addStretch()
        self.layout.addWidget(self.minimize_button, alignment=Qt.AlignRight)
        self.layout.addWidget(self.maximize_button, alignment=Qt.AlignRight)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignRight)
        
        self.setLayout(self.layout)

    def initLayout(self):
        # build main layout
        self.layout = DHBoxLayout()
        self.layout.setContentsMargins(10,0,0,0)
        self.layout.setAlignment(Qt.AlignRight)


    def initWidgets(self):
        font = QFont("Roboto", 12)
        self.title_label = QLabel(self.materials.title)
        self.title_label.setFixedHeight(self.HEIGHT)
        #self.title_label.setAlignment(Qt.Align)
        self.title_label.setFixedWidth(300)
        self.title_label.setFont(font)
        #self.title_label.setStyleSheet('background-color: #dddddd')
    
        self.exit_button = QPushButton('X')
        self.exit_button.setFixedSize(self.HEIGHT * 2, self.HEIGHT)
        self.exit_button.setObjectName('exit_button')
        self.exit_button.clicked.connect(self.exitButtonAction)
        
        self.maximize_button = QPushButton('[ ]')
        self.maximize_button.setFixedSize(self.HEIGHT*2, self.HEIGHT)
        self.maximize_button.setObjectName('topbar_button')
        self.maximize_button.clicked.connect(self.maximizeButtonAction)
        
        self.minimize_button = QPushButton('_')
        self.minimize_button.setFixedSize(self.HEIGHT*2, self.HEIGHT)
        self.minimize_button.setObjectName('topbar_button')
        self.minimize_button.clicked.connect(self.minimizeButtonAction)
        


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        

    def mouseMoveEvent(self, event):
        gui = self.getGUI()
        
        if not gui.isMaximized:
        
            delta = QPoint(event.globalPos() - self.oldPos)
            
            gui.move(gui.x() + delta.x(), gui.y() + delta.y())
            
            self.oldPos = event.globalPos()
    
    def exitButtonAction(self):
        self.getGUI()._quit()
        
    def maximizeButtonAction(self):
        self.getGUI()._maximize()
        
    def minimizeButtonAction(self):
        self.getGUI()._minimize()


        
class DSideBar(DFrame):
    WIDTH = 40

    def __init__(self, parent):
        super().__init__(parent)

    def build(self):
        super().build()

        self.requireAttributes(['name'])

        self.setFixedWidth(self.WIDTH)
        self.setObjectName(self.materials.name)


        self.layout = DVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)



        home_button = DSideBarHomeButton('H')
        self.layout.addWidget(home_button)

        self.setLayout(self.layout)

      


    def addTab(self, title):
        button = DSideBarButton(title)
        self.layout.addWidget(button)

        func = self.getApp().setTab

        button.clicked.connect(lambda: func(title))

