from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from dg.gui.DCore import DFrame, DNavPage
from dg.gui.DMaterials import DBuildMaterials
from dg.gui.DLayout import DGridLayout, DVBoxLayout, DFastGridLayout
from dg.gui.DExtra import DShadow
from dg.gui.DWidgets import DTopMenu,DButton
from dg.lib.DUtils import DColor








class CommandsPage(DNavPage):
    GRID_WIDTH = 4
    
    title = 'Commands'
    sidebar_title = 'CMD'
    
    def __init__(self, parent):
        super().__init__(parent)

        materials = DBuildMaterials()
        materials.name = 'page'

        self.addMaterials(materials)
        
        self.model = self.getApp().getModel('CommandsModel')
        
        
    def prepare(self):
        super().prepare()
        
        self.menu_frame = DTopMenu(self)
        

        
        buttons_frame_mats = DBuildMaterials()
        self.buttons_frame = DCommandsButtonFrame(self)
        self.buttons_frame.addMaterials(buttons_frame_mats)
        
        self.model.setLogger(self.getGUI().logger)

        
    def build(self):
        super().build()
        
        self.layout = DCommandsPageLayout()
        self.setLayout(self.layout)
        
        self.menu_frame.build()
        
        add_button = self.menu_frame.addButton('Add')
        add_button.clicked.connect(self.addNewCommand)
        
        edit_button = self.menu_frame.addButton('Edit')
        
        self.layout.addWidget(self.menu_frame, alignment=self.layout.CENTER)
        
        self.buttons_frame.build()
        self.layout.addWidget(self.buttons_frame)
        #self.layout.addStretch()
        
        
    def onShow(self):
        super().onShow()
        
        self.buttons_frame.clearLayout()
        
        self.model.loadCommands()
        
        self.addCommandButtons()
    

        
    def addCommandButtons(self):
        for cmd_name in self.model.getCommandNames():
            color = self.model.getCommandColor(cmd_name)
            self.addButton(cmd_name, color)
            
        
        
    def addButton(self, cmd_name, color):
        button = DCommandsButton(cmd_name)
        
        colors = DColor.colorsForButton(color)
        
        r1,g1,b1 = colors[0]
        r2,g2,b2 = colors[1]
        r3,g3,b3 = colors[2]
        
        default_color = 'background-color: rgba({},{},{},255);'.format(r1,g1,b1)
        hover_color = 'background-color: rgba({},{},{},255);'.format(r2,g2,b2)
        pressed_color = 'background-color: rgba({},{},{},255);'.format(r3,g3,b3)
        
        style = '''
            QPushButton{
                background-color: #BDC3C4;
                ''' + default_color + '''
                border: none;
                border-radius: 3px;
            }

            QPushButton:hover{
                ''' + hover_color + '''
                color: rgba(20,20,20,255);
            }

            QPushButton:pressed{
                ''' + pressed_color + '''
                border: 2px solid rgba(20,20,20,255);
            }
        '''
        
        button.setStyleSheet(style)
        func = self.model.run
        button.clicked.connect(lambda: func(cmd_name))
        
        self.buttons_frame.addButton(button)

    def addNewCommand(self):
        self.getApp().setPage('NewCommandPage')
        


class DCommandsPageLayout(DVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setSpacing(80)
        self.setContentsMargins(40,0,40,40)
        self.alignTop()



        
class DCommandsButtonLayout(DFastGridLayout):
    def __init__(self):
        super().__init__(4)

        self.setSpacing(40)
        self.alignCenter()

        
       
class DCommandsButtonFrame(DFrame):
    def __init__(self, parent):
        super().__init__(parent)
 
        
    def build(self):
        super().build()
        
        self.layout = DCommandsButtonLayout()
        self.setLayout(self.layout)
        
    def addButton(self, button):
        self.layout.addWidget(button)
            
        
class DCommandsButton(DButton):
    WIDTH = 200
    HEIGHT = 60

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('page_button')
        self.setFont(QFont("Roboto", 14))
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setContentsMargins(10,10,10,10)

       