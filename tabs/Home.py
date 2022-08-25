from dg.DCore import DFrame
from dg.DLayout import DHBoxLayout, DHomeLayout
from dg.DMaterials import DBuildMaterials
from dg.DWidgets import DHomePageButton



class Home(DFrame):

    def __init__(self, parent):
        super().__init__(parent)

        materials = DBuildMaterials()
        materials.name = 'home'

        self.addMaterials(materials)


    def build(self):
        super().build()

        print('1')
        self.layout = DHomeLayout()

        self.layout.addWidget(DHomePageButton('Test'), 0,0)

        self.setLayout(self.layout)


        


        

