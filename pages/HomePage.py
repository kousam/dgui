from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from dg.gui.DCore import DHomePage
from dg.gui.DLayout import DGridLayout
from dg.gui.DMaterials import DBuildMaterials



class HomePage(DHomePage):
    title = 'Home'
    sidebar_title = 'Home'
    
    def __init__(self, parent):
        super().__init__(parent)

        materials = DBuildMaterials()
        materials.name = 'home'

        self.addMaterials(materials)

    def build(self):
        super().build()

        self.layout = DHomeLayout()
        self.layout.addWidget(DHomePageButton('Test'), 0, 0)

        self.setLayout(self.layout)


class DHomeLayout(DGridLayout):
    def __init__(self):
        super().__init__()

        self.setSpacing(20)
        self.setAlignment(Qt.AlignCenter)
        self.setContentsMargins(0,0,20,0)

     
class DHomePageButton(QPushButton):
    WIDTH = 100
    HEIGHT = 60

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('page_button')
        self.setFont(QFont("Roboto", 14))
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        

