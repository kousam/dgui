
from dg.lib.Vagrant import VagrantHaltCommand, VagrantUpCommand


class VagrantModel():
    def __init__(self, app):
        self.app = app

        self.commands_model = self.app.getModel('CommandsModel')
        
        self.upCommand = VagrantUpCommand()
        self.haltCommand = VagrantHaltCommand()
        
        self.logger = self.app.getGUI().getLogger()
        
    def vagrantUp(self):
        try:
            self.upCommand.run(self.logger)
            
        except Exception as e:
            self.logger.log('VAGRANT', repr(e))
            
    def vagrantHalt(self):
        try:
            self.haltCommand.run(self.logger)
            
        except Exception as e:
            self.logger.log('VAGRANT', repr(e))
