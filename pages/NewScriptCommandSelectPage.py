
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from dg.gui.DCore import DPage, DNavPage
from dg.gui.DWidgets import DButton
from dg.gui.DLayout import DFastGridLayout
from dg.gui.DExtra import DShadow

class NewScriptCommandSelectPage(DPage):
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
        
        self.model.loadScripts()

        
        for script_name in self.model.getScriptNames():
            self.addButton(script_name)
        

        
    def addButton(self, script_name):
        button = DCommandsButton(script_name)
        self.layout.addWidget(button)
        func = self.buttonActions
        button.clicked.connect(lambda: func(script_name))
        
    def buttonActions(self, script_name):
        self.model.newChildScript(script_name)
        
    
class DCommandsButton(DButton):
    WIDTH = 200
    HEIGHT = 60

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('page_button')
        self.setFont(QFont("Roboto", 14))
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setContentsMargins(10,10,10,10)
        
