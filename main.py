from dg.DApp import DApp
from dg.DCore import DWindow
from PyQt5.QtWidgets import QApplication

from dg.DMaterials import DWindowBuildMaterials, DAppBuildMaterials
import os
import sys



TITLE = 'Code buddy'
RECT = (150,150,1200,800)

#Load stylesheet from qss
qss="style.qss"
with open(qss,"r") as fh:
    style = fh.read()



app_mats = DAppBuildMaterials()
app_mats.title = TITLE
app_mats.rect = RECT
app_mats.style = style
app_mats.font = 'Roboto-Regular.ttf'


if __name__ == '__main__':
    app = DApp()
    app.addMaterials(app_mats)
    print('1')
    app.build()
    
    app.run()
