

from dg.gui.DCore import DHomePage
from dg.gui.DLayout import DVBoxLayout
from dg.gui.DMaterials import DBuildMaterials
from dg.gui.DWidgets import DLabel, DButton




class HomePage(DHomePage):
    title = 'Home'
    sidebar_title = 'Home'
    
    def __init__(self, parent):
        super().__init__(parent)

        materials = DBuildMaterials()
        materials.name = 'home'

        self.addMaterials(materials)
        
        self.label = DHomePageLabel()
        self.label.setText('Hello')

    def build(self):
        super().build()

        self.layout = DVBoxLayout()
        self.layout.alignCenter()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)




     
class DHomePageLabel(DLabel):
    WIDTH = 100
    HEIGHT = 60

    def __init__(self):
        super().__init__()
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setFontSize(26)

        

