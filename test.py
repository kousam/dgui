
import importlib

module = importlib.import_module('dg.FileMgr')

myclass = getattr(module, 'FileMgr')

c = myclass()

print(c.loadModels())
