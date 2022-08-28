from dg.gui.DCore import DFrame, DNavPage
from dg.gui.DLayout import DHBoxLayout
from dg.gui.DMaterials import DBuildMaterials
from dg.gui.DWidgets import DButton




class VagrantPage(DNavPage):
    
    title = 'Vagrant'
    sidebar_title = 'Vagrant'
    
    def __init__(self, parent):
        super().__init__(parent)

        materials = DBuildMaterials()
        materials.name = 'page'

        self.addMaterials(materials)
        
        self.model = self.getApp().getModel('VagrantModel')
        
    def prepare(self):
        super().prepare()
        
        self.layout = DHBoxLayout()
        
        self.buttons_frame = ButtonsFrame(self)
        
    def build(self):
        super().build()
        
        self.setLayout(self.layout)
        
        self.buttons_frame.build()
        self.layout.addWidget(self.buttons_frame)



class ButtonsFrame(DFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
    def prepare(self):
        super().prepare()
        
        self.layout = DHBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(10,10,10,10)
        
        self.up_button = DCommandsButton('Vagrant Up')
        self.up_button.setOnClick(self.parent.model.vagrantUp)
        
        self.halt_button = DCommandsButton('Vagrant Halt')
        self.halt_button.setOnClick(self.parent.model.vagrantHalt)
        
        
    def build(self):
        super().build()
        
        self.setLayout(self.layout)
        
        self.layout.addWidget(self.up_button)
        self.layout.addWidget(self.halt_button)
        
        
        
class DCommandsButton(DButton):
    WIDTH = 200
    HEIGHT = 60

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('page_button')
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        
    def setOnClick(self, func, args=None):
        
        if args:
            self.clicked.connect(lambda: func(args))
            
        else:
            self.clicked.connect(func)
