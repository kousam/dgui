from dg.gui.DApp import DApp
from dg.gui.DMaterials import DWindowBuildMaterials, DAppBuildMaterials




TITLE = 'Code buddy'
RECT = (150,150,1200,900)

#Load stylesheet from qss
qss="dg//style.qss"
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
    app.build()
    
    app.run()
