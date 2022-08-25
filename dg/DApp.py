


import asyncio
from asyncqt import QEventLoop

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import sys
import os
import subprocess


from dg.DCore import DObject, DWindow
from dg.DMaterials import DBuildMaterials, DWindowBuildMaterials
from dg.FileMgr import FileMgr




class DApp(DObject):
    def __init__(self):
        super().__init__()

        self.fileMgr = FileMgr()

        self.models = {}
        self.loaded_models = {}

        self.tabs = {}
        self.loaded_tabs = {}

    def prepare(self):
        super().prepare()
        os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.qApp = QApplication(sys.argv)

        self.loadTabs()


        window_mats = DWindowBuildMaterials()
        window_mats.title = self.materials.title
        window_mats.rect = self.materials.rect
        window_mats.style = self.materials.style
        window_mats.font = self.materials.font
        window_mats.app = self
        window_mats.tabs = self.getTabKeys()

        self.window = DWindow()
        self.window.addMaterials(window_mats)
        

    def run(self):
        self.requireAttributes(['name'])

        #asyncio.set_event_loop(self.loop)

        

        self.window.build()
            
        sys.exit(self.qApp.exec_())
        

    def quit(self):
        sys.exit(self.qApp.exec_())
        

    def loadModels(self):
        self.models = self.fileMgr.loadModels()

    def loadTabs(self):
        self.tabs = self.fileMgr.loadTabs()

    
    def getModel(self, name):
        if name not in self.loaded_models:
            self.loaded_models[name] = self.models[name]()

        return self.loaded_models[name]

    def getTab(self, name):
        if name not in self.loaded_tabs:
            tab_class = self.tabs[name]
            tab_object = tab_class(self.window)
            self.loaded_tabs[name] = tab_object

        return self.loaded_tabs[name]

    def getModelKeys(self):
        return list(self.models.keys())

    def getTabKeys(self):
        return list(self.tabs.keys())

    def setTab(self, name):
        self.window.setContent(self.getTab(name))





