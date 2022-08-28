



from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import sys
import os
import subprocess


from dg.gui.DCore import DHomePage, DNavPage, DObject
from dg.gui.DWidgets import DWindow
from dg.gui.DMaterials import DWindowBuildMaterials
from dg.lib.FileMgr import FileMgr





class DApp(DObject):
    def __init__(self):
        super().__init__()

        self.fileMgr = FileMgr()

        self.models = {}
        self.loaded_models = {}

        self.pages = {}
        self.loaded_pages = {}
        

    def prepare(self):
        super().prepare()
        os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.qApp = QApplication(sys.argv)

        self.models = self.fileMgr.loadModels()
        self.pages = self.fileMgr.loadPages()


        window_mats = DWindowBuildMaterials()
        window_mats.title = self.materials.title
        window_mats.rect = self.materials.rect
        window_mats.style = self.materials.style
        window_mats.font = self.materials.font
        window_mats.app = self
        window_mats.pages = self.getNavPageKeys()
        window_mats.home_page = self.getHomePageKey()

        self.window = DWindow()
        self.window.addMaterials(window_mats)
    
        

    def run(self):
        self.requireAttributes(['name'])

        self.window.build()
        self.setPage(self.getHomePageKey())
            
        sys.exit(self.qApp.exec_())
        

    def quit(self):
        sys.exit(self.qApp.exec_())
    
    def getGUI(self):
        return self.window

    def getModel(self, name):
        if name not in self.loaded_models:
            print('Init Model ' + name)
            self.loaded_models[name] = self.models[name](self)

        return self.loaded_models[name]

    def getPage(self, name):
        if name not in self.loaded_pages:
            print('Building Page ' + name)
            page_class = self.pages[name]
            page_object = page_class(self.window)
            self.loaded_pages[name] = page_object

        return self.loaded_pages[name]

    def getModelKeys(self):
        return list(self.models.keys())

    def getPageKeys(self):
        return list(self.pages.keys())
    
    def getNavPageKeys(self):
        return [key for key, page in self.pages.items() if issubclass(page, DNavPage)]
    
    def getHomePageKey(self):
        return [key for key, page in self.pages.items() if issubclass(page, DHomePage)][0]
    
    def getPageTitle(self, key):
        return self.pages[key].title
    
    def getPageSideBarTitle(self, key):
        return self.pages[key].sidebar_title

    def setPage(self, name):
        self.window.setContent(self.getPage(name))

    def getFileMgr(self):
        return self.fileMgr


