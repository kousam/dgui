
import json 
import os
import importlib

class FileMgr():
    PATHS_FILE = 'paths.json'
    MODELS_PATH = 'models'
    TABS_PATH = 'tabs'


    def __init__(self):
        self.base_path = os.getcwd() + '\\';

    def joinPath(self, a, b):
        return '{}\\{}'.format(a,b)

    def joinModule(self, parent, child):
        return '{}.{}'.format(parent, child)

    def loadPaths(self):
        with open(self.joinPath(self.base_path, self.PATHS_FILE)) as file:
            paths = json.load(file)

        return paths


    def loadModels(self):
        models = {}

        files = os.listdir(self.joinPath(self.base_path, self.MODELS_PATH))

        for file in files:
            filename = file.split('.')[0]
            module = importlib.import_module(self.joinModule(self.MODELS_PATH, filename))
            module_class = getattr(module, filename)
            models[filename] = module_class

        return models

    def loadTabs(self):
        models = {}

        
        files = os.listdir(self.joinPath(self.base_path, self.TABS_PATH))

        print(files)

        for file in files:
            filename = file.split('.')[0]
            if not file.startswith('__'):
                module = importlib.import_module(self.joinModule(self.TABS_PATH, filename))
                module_class = getattr(module, filename)
                models[filename] = module_class

        return models