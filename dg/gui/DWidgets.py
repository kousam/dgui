
from ctypes import alignment
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QLineEdit, QTextEdit, QStatusBar
from PyQt5.QtGui import QFontDatabase, QFont, QTextCursor, QIcon
from PyQt5.QtCore import Qt, QTimer, QPoint

import time
import datetime
import re


from dg.gui.DCore import DFrame, DUIObject, DAlign
from dg.gui.DExtra import DShadow, DShadowDark
from dg.gui.DLayout import DHBoxLayout, DVBoxLayout,DStackedLayout


from dg.gui.DMaterials import DBuildMaterials
from dg.lib.DUtils import DColor


class DWindow(QMainWindow, DUIObject):
    MARGINS = 10,10,10,10

    def __init__(self):
        super().__init__()
        
        self.isMaximized = False

    def prepare(self):
        
        super().prepare()
        #sidebar

        self.app = self.materials.app

        topbar_mats = DBuildMaterials()
        topbar_mats.name = 'top_bar'
        topbar_mats.title = self.materials.title
        self.topbar = DTopbar(self)
        self.topbar.addMaterials(topbar_mats)

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

        logger_mats = DBuildMaterials()
        logger_mats.name = 'logger'
        self.logger = DLogger(self)
        self.logger.addMaterials(logger_mats)

        #main frame
        main_frame_mats = DBuildMaterials()
        main_frame_mats.name = 'main_frame'
        main_frame_mats.title = self.materials.title
        main_frame_mats.inner_frame = inner_frame
        main_frame_mats.logger = self.logger
        main_frame_mats.topbar = self.topbar
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

        left,right,up,down = self.MARGINS
        self.setContentsMargins(left,right,up,down)
        self.setGraphicsEffect(DShadow())
        
        self.setWindowTitle(self.materials.title)
        x,y,w,h = self.materials.rect
        self.setGeometry(x,y,w,h)
        
        statusbar = DStatusBar(self)
        self.setStatusBar(statusbar)

        self.main_frame.build()

        self.setCentralWidget(self.main_frame)
        
        self.sidebar.addHomeButton(self.materials.home_page)

        for page in self.materials.pages:
            self.sidebar.addPageButton(page)
            
        self.logger.log('App', 'Hello')
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
        self.content_frame.setContent(content)


    def _maximize(self):
        try:
            if self.isMaximized:
                
                self.showNormal()
                self.statusBar().show()
                
                left,right,up,down = self.MARGINS
                self.setContentsMargins(left,right,up,down)

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
        

    def width(self):
        w = super().width()

        if self.isMaximized:
            return w
        else:
            left,right,up,down = self.MARGINS
            return w - (left + right) - 2 # minus border im too lazy to not hardcode it

    def height(self):
        h = super().height()

        if not self.isMaximized:
            return h
        else:
            left,right,up,down = self.MARGINS
            return h - (up + down)
    
    def getLogger(self):
        return self.logger
    
class DStatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName('statusbar')
        self.setSizeGripEnabled(True)
        self.setFixedHeight(14)
        



class DSideBar(DFrame):
    WIDTH = 100

    def __init__(self, parent):
        super().__init__(parent)

    def build(self):
        super().build()

        self.requireAttributes(['name'])

        self.setFixedWidth(self.WIDTH)
        self.setObjectName(self.materials.name)


        self.layout = DVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        
        self.setGraphicsEffect(DShadowDark())

        self.setLayout(self.layout)
        
        
    def addHomeButton(self, page_key):
        title = self.getApp().getPageSideBarTitle(page_key)
        
        home_button = DSideBarHomeButton(title)
        self.layout.addWidget(home_button)
        func = self.getApp().setPage
        home_button.clicked.connect(lambda: func(page_key))


    def addPageButton(self, page_key):
        title = self.getApp().getPageSideBarTitle(page_key)
        button = DSideBarButton(title)
        self.layout.addWidget(button)
        func = self.getApp().setPage
        button.clicked.connect(lambda: func(page_key))



class DSideBarButton(QPushButton):
    WIDTH = 100
    HEIGHT = 40

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('sidebar_button')
        self.setFont(QFont("Roboto", 12))
        self.setFixedSize(self.WIDTH, self.HEIGHT)

class DSideBarHomeButton(DSideBarButton):
    WIDTH = 100
    HEIGHT = 40

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('sidebar_home_button')

        
        
class DMainFrame(DFrame):

    def __init__(self, parent):
        super().__init__(parent)

    def prepare(self):
        super().prepare()


    def build(self):
        super().build()
        
        
        self.layout = DVBoxLayout()

        self.materials.topbar.build()

        self.materials.logger.build()

        self.materials.inner_frame.build()

        self.layout.addWidget(self.materials.topbar)
        self.layout.addWidget(self.materials.inner_frame)
        self.layout.addWidget(self.materials.logger)


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

        self.pages = []
        self.count = 0

    def build(self):
        super().build()
    

        self.layout = DStackedLayout()
        self.setLayout(self.layout)


    def setContent(self, page):
        if page not in self.pages:
            self.pages.append(page)
            page.build()
            self.layout.insertWidget(self.count, page)
            self.count += 1     

        self.layout.setCurrentWidget(page)
        page.onShow()
        


class DTopbar(DFrame):
    HEIGHT = 32
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.maximized = False
    
    def build(self):
        super().build()
        

        self.requireAttributes(['name', 'title'])

        self.setFixedHeight(self.HEIGHT)


        self.layout = DHBoxLayout()
        self.layout.setContentsMargins(10,0,0,0)
        self.layout.setAlignment(Qt.AlignRight)
        
 
        self.title_label = QLabel(self.materials.title)
        self.title_label.setFixedHeight(self.HEIGHT)
        self.title_label.setFixedWidth(300)
        self.title_label.setFont(QFont("Roboto", 12))
        

        
        
    
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
        
        self.layout.addWidget(self.title_label, alignment=Qt.AlignLeft)
        self.layout.addStretch()
        self.layout.addWidget(self.minimize_button, alignment=Qt.AlignRight)
        self.layout.addWidget(self.maximize_button, alignment=Qt.AlignRight)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignRight)
        
        self.setLayout(self.layout)


        


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


        


class DInputField(QLineEdit, DAlign):
    HEIGHT = 40
    def __init__(self):
        super().__init__()
        self.setObjectName('input_field')
        self.setFont(QFont("Roboto", 12))
        self.setFixedHeight(self.HEIGHT)
        self.setGraphicsEffect(DShadow())
        
class DRoundInputField(QLineEdit, DAlign):
    HEIGHT = 40
    def __init__(self):
        super().__init__()
        self.setObjectName('round_input_field')
        self.setFont(QFont("Roboto", 12))
        self.setFixedHeight(self.HEIGHT)


class DLogger(DFrame):
    HEIGHT = 226
    LOGGER_HEIGHT = 200
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.log_queue = []
        
    def build(self):
        super().build()
        
        self.setObjectName('logger_frame')
        
        self.layout = DVBoxLayout()
        self.layout.setAlignment(Qt.AlignBottom)
        
        self.setLayout(self.layout)
        self.setFixedHeight(self.HEIGHT)
        
        self.topbar = DLoggerTopbar(self)
        self.topbar.build()
        self.layout.addWidget(self.topbar)
        
        self.log_textEdit = QTextEdit()
        self.log_textEdit.setReadOnly(True)
        self.log_textEdit.setFont(QFont("Roboto", 12))
        self.log_textEdit.setFixedHeight(self.LOGGER_HEIGHT)
        #self.log_textEdit.setFixedWidth(self.parent.width())
        self.log_textEdit.setObjectName('logger')
        
        self.layout.addWidget(self.topbar)
        self.layout.addWidget(self.log_textEdit)
        
        self._update_timer = QTimer()
        self._update_timer.timeout.connect(self.loop)
        self._update_timer.start(100) # milliseconds
        
        #self.setGraphicsEffect(DShadowDark())
        

        
    def log(self, sender, text):
        self.log_queue.append((sender, text.rstrip('\n')))
        
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
        
        
class DLoggerTopbar(DFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.isMinimized = False
        
    def prepare(self):
        super().prepare()
        
        
        
        self.layout = DHBoxLayout()
        self.layout.alignCenter()
        self.layout.setContentsMargins(10,0,0,0)
        self.label = DLabel()
        self.label.setText('Output')
        self.label.setFontSize(12)
        self.label.setObjectName('logger_label')
        self.label.setFixedHeight(26)

        
    def build(self):
        super().build()
        
        self.setFixedHeight(26)
        
        self.setLayout(self.layout)
        self.layout.addStretch()
        self.layout.addWidget(self.label, alignment=self.layout.LEFT)
        self.layout.addStretch()


        
        
    


class DButton(QPushButton, DAlign):
    def __init__(self, text):
        QPushButton.__init__(self,text)
        DAlign.__init__(self)
        self.setObjectName('page_button')
        self.setFont(QFont("Roboto", 14))
        self.setGraphicsEffect(DShadowDark())
        
    def setFontSize(self, size):
        self.setFont(QFont("Roboto", size))
        
        
class DLabel(QLabel, DAlign):
    def __init__(self):
        super().__init__()
        
        self.setObjectName('page_Label_normal')
        self.setFont(QFont("Roboto", 14))
    
    def setFontSize(self, size):
        self.setFont(QFont("Roboto", size))      


class DTopMenu(DFrame):
    
    def __init__(self, parent):
        super().__init__(parent)
        
    def prepare(self):
        super().prepare()
        
        self.layout = DHBoxLayout()
        self.layout.setSpacing(10)
        
    def build(self):
        super().build()
        
        self.setLayout(self.layout)
        
    def addButton(self, text):
        button = DTopMenuButton(text)
        self.layout.addWidget(button)
        
        return button

class DTopMenuButton(DButton):
    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('top_menu_button')
        self.setFont(QFont("Roboto", 12))
        self.setFixedSize(120,40)
        self.setGraphicsEffect(DShadow())
        
    def setFontSize(self, size):
        self.setFont(QFont("Roboto", size))
        


class DColorPicker(DFrame, DAlign):
    def __init__(self, parent):
        super().__init__(parent)
        
    def prepare(self):
        super().prepare()
        
        
        self.setFixedSize(300, 60)
        
        self.layout = DHBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10,10,10,10)
        self.layout.alignCenter()
        
        self.label = DLabel()
        self.label.setFixedSize(100,40)
        self.label.setObjectName('color_label')
        self.label.alignCenter()
        
        self.random_button = DButton('Randomize')
        self.random_button.setFixedSize(140,40)
        self.random_button.clicked.connect(self.randomize)
        
        
    def build(self):
        super().build()
        
        self.setLayout(self.layout)
        

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.random_button)
        

        
    def setBackgroundColor(self):
        
        r,g,b = self.color
        
        color = 'background-color: rgba({},{},{},255);'.format(r,g,b)
        
        style_str = '''
        QLabel{
            color: rgba(20,20,20,255);
            ''' + color + '''
            border: none;
            border-radius: 3px;
        }
        '''

            
        self.label.setStyleSheet(style_str)
        
    def randomize(self):
        self.color = color = DColor.randomPastel()
        
        self.label.setText(DColor.toHex(color))
        self.setBackgroundColor()
        
    def getColor(self):
        return self.color
        