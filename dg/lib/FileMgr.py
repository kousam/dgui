
import json 
import os
import importlib

class FileMgr():
    PATHS_FILE = 'paths.json'
    MODELS_PATH = 'models'
    PAGES_PATH = 'pages'


    def __init__(self):
        self.base_path = os.getcwd() + '\\';

    def joinPath(self, a, b):
        return '{}\\{}'.format(a,b)

    def joinModule(self, parent, child):
        return '{}.{}'.format(parent, child)

    def loadJson(self, path):
        try:
            with open(path, 'r') as json_file:
                json_data = json.load(json_file)

            return json_data
        
        except Exception as e:
            print('[ERROR] ' + repr(e))

            return {}


    def loadModuleClass(self, import_path, class_name):
        try:
            print('Loading ' + class_name)
            module = importlib.import_module(self.joinModule(import_path, class_name))
            module_class = getattr(module, class_name)

            return module_class

        except Exception as e:
            print('[ERROR] ' + repr(e))

            return False

    def loadPathModuleClasses(self, path):
        modules = {}

        files = os.listdir(self.joinPath(self.base_path, path))
        import_path = path.replace('\\', '.').replace('/', '.')

        for file in files:
            filename = file.split('.')[0]
            if not filename.startswith('__'):
                module_class = self.loadModuleClass(import_path, filename)
                if module_class:
                    modules[filename] = module_class
                    
        return modules

    def loadModels(self):
        return self.loadPathModuleClasses(self.MODELS_PATH)

    def loadPages(self):
        return self.loadPathModuleClasses(self.PAGES_PATH)
    
    
    def saveJson(self, path, json_data):
        with open(path, 'w') as json_file:
            json.dump(json_data, json_file)
    

        