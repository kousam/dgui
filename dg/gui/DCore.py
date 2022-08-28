from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt


from dg.gui.DMaterials import DMaterialsContainer, DBuildMaterials, DBuildMaterials




class DObject():
    def __init__(self):
        self.materials = DMaterialsContainer()

    def addMaterials(self, mats):
        self.materials.add(mats)
        
    def requireAttributes(self, required_attributes):
        for required_attribute in required_attributes:
            if required_attribute not in self.materials.__dict__:
                raise Exception('Missing required attribute "{}"'.format(required_attribute))

    def unpack(self):
        self.materials.unpack()

    def build(self):
        self.materials.unpack()
        print('Unpacking ' + self.materials.name)

        self.prepare()

    def prepare(self):
        return

    def initUI(self):
        return


class DAlign():
    LEFT = Qt.AlignLeft
    RIGHT = Qt.AlignRight
    TOP = Qt.AlignTop
    BOTTOM = Qt.AlignBottom
    CENTER = Qt.AlignCenter
    
    def alignLeft(self):
        self.setAlignment(Qt.AlignLeft)
        
    def alignRight(self):
        self.setAlignment(Qt.AlignRight)
        
    def alignTop(self):
        self.setAlignment(Qt.AlignTop)
        
    def alignBottom(self):
        self.setAlignment(Qt.AlignBottom)
        
    def alignCenter(self):
        self.setAlignment(Qt.AlignCenter)


class DUIObject(DObject):
    def __init__(self):
        super().__init__()
    
    def build(self):
        super().build()

        if hasattr(self.materials, 'name'):
            self.setObjectName(self.materials.name)
        
        self.initUI()

    def hl(self):
        self.setObjectName('test')



class DFrame(QFrame, DUIObject):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        DObject.__init__(self)

        self.parent = parent
        
        mats = DBuildMaterials()
        mats.name = 'DFrame'
        mats.obj_name = 'DFrame'
        self.addMaterials(mats)

    def build(self):
        super().build()
        
    def onShow(self):
        return

    def getGUI(self):
        return self.parent.getGUI()

    def getParent(self):
        return self.parent

    def getApp(self):
        return self.parent.getApp()
        
    def hl(self):
        self.setStyleSheet("background-color: rgb(200, 100, 100)")
        
    def clearLayout(self):
        self.layout.clear()
                
                
        

class DPage(DFrame):
    title = 'Page'

    def __init__(self, parent):
        super().__init__(parent)
            
    def build(self):
        super().build()

        

class DNavPage(DPage):
    title = 'Page'
    sidebar_title = 'Page'
    
    def __init__(self, parent):
        super().__init__(parent)
        
    def build(self):
        super().build()

        
        
class DHomePage(DPage):
    title = 'Home Page'
    sidebar_title = 'Home Page'
    
    def __init__(self, parent):
        super().__init__(parent)
        
    def build(self):
        super().build()


