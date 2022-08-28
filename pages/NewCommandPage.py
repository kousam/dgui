
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from dg.gui.DCore import DPage, DNavPage
from dg.gui.DWidgets import DButton
from dg.gui.DLayout import DFastGridLayout
from dg.gui.DExtra import DShadow

class NewCommandPage(DPage):
    TITLE = 'New Command'
    
    def __init__(self, parent):
        super().__init__(parent)
        self.count = 0
        
        self.model = self.getApp().getModel('NewCommandModel')
        
    def prepare(self):
        super().prepare()
        
        
    def build(self):
        super().build()
        
        self.layout = DFastGridLayout(3)
        self.layout.setSpacing(40)
        self.layout.alignCenter()
        self.setLayout(self.layout)
        
        for command_type in self.model.getCommandTypes():
            self.addButton(command_type)
        

        
    def addButton(self, command_type):
        button = DCommandsButton(command_type)
        self.layout.addWidget(button)
        func = self.model.route
        button.clicked.connect(lambda: func(command_type))
            

    
class DCommandsButton(DButton):
    WIDTH = 200
    HEIGHT = 60

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('page_button')
        self.setFont(QFont("Roboto", 14))
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setContentsMargins(10,10,10,10)
        
