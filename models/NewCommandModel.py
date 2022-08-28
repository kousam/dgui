

class NewCommandModel():
    def __init__(self, app):
        self.app = app
        
        self.commands_model = self.app.getModel('CommandsModel')
        
        self.types = ['Shell', 'Script']
        
        self.routing = {'Shell': self.openNewShellCommand, 'Script': self.openNewScriptSelect}
        
        
    def getCommandTypes(self):
        return self.commands_model.TYPES
    
    def route(self, key):
        self.routing[key]()
    
        
    def openNewShellCommand(self):
        self.app.setPage('NewShellCommandPage')
        
    def openNewScriptSelect(self):
        self.app.setPage('NewScriptCommandSelectPage')
    
    def openNewScriptCommand(self):
        self.app.setPage('NewScriptCommandPage')
        
        
    def saveNewShellCommand(self, title, data):
        self.commands_model.addCommandAndSave(title, data)
        
    def saveNewScriptCommand(self, title, data):
        self.commands_model.addCommandAndSave(title, data)
        
    def loadScripts(self):
        self.commands_model.loadScripts()
        
    def getScriptNames(self):
        return self.commands_model.getScriptNames()
    
    def newChildScript(self, script_name):
        self.script_name = script_name
        self.openNewScriptCommand()
        
    def getScript(self):
        return self.script_name
    
    def getScriptArgs(self):
        return self.commands_model.getScriptArgs(self.script_name)
        

        
    