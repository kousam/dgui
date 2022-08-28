
from dg.lib.DCommand import DShellCommand, DScript



class CommandsModel():
    COMMANDS_JSON_FILE = 'commands.json'
    SCRIPTS_PATH = 'scripts'
    
    TYPES = ['Shell', 'Script']

    def __init__(self, app):
        self.app = app
        self.script_classes = {}
        self.commands = {}
        self.command_colors = {}
        
        self.commands_json = {}

        self.buildRoute = {}
        self.buildRoute['Script'] = self.buildScript
        self.buildRoute['Shell'] = self.buildShellCommand

    def reset(self):
        self.commands = {}
        
    def loadScripts(self):
        self.command_classes = {}
        
        for key, script_class in self.app.getFileMgr().loadPathModuleClasses(self.SCRIPTS_PATH).items():
            self.script_classes[key] = script_class
            
        
    def loadCommands(self):
        self.commands_json = {}
        self.commands_json = self.app.getFileMgr().loadJson(self.COMMANDS_JSON_FILE)

        for title, data in self.commands_json.items():
            self.command_colors[title] = data['color']
            self.commands[title] = self.buildCommand(data)
        

    def buildCommand(self, data):
        return self.buildRoute[data['type']](data)

    def buildScript(self, data):
        script_class = self.app.getFileMgr().loadModuleClass('scripts', data['script'])
        script_object = script_class(data['args'])
        
        return script_object

    def buildShellCommand(self, data):
        command = DShellCommand(data['args'])

        return command


    def getCommandNames(self):
        return list(self.commands.keys())
    
    def getCommandColor(self, key):
        return self.commands[key].getColor()
    
    def run(self, cmd):
        try:
            self.commands[cmd].run(self.logger)
        except Exception as e:
            self.logger.log('CMD MODEL', repr(e))
        
    def setLogger(self, logger):
        self.logger = logger
        
    def log(self):
        self.logger.log()
        
    def addCommandAndSave(self, title, data):
        self.loadCommands()
        self.commands_json[title] = data

        self.app.getFileMgr().saveJson(self.COMMANDS_JSON_FILE, self.commands_json)
        
    def getCommandColor(self, key):
        return self.command_colors[key]
    
    def getScriptNames(self):
        return self.script_classes.keys()
    
    def getScriptArgs(self, key):
        return self.script_classes[key].ARGS