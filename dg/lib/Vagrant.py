from dg.lib.DCommand import DShellCommand



class VagrantUpCommand(DShellCommand):
    LOG_TITLE = 'VAGRANT'
    VAGRANT_DIR = ''
    
    args = {'cmd':'vagrant', 'cmd_args': 'up', 'cwd':VAGRANT_DIR}
    
    def __init__(self):
        super().__init__(self.args)
        
    def run(self, logger):
        self.logger.log(self.LOG_TITLE, 'Running vagrant up')
        
        super().run(logger, self.callback)
        
    def callback(self):
        self.logger.log(self.LOG_TITLE, 'Vagrant is up!')
        
        
class VagrantHaltCommand(DShellCommand):
    LOG_TITLE = 'VAGRANT'
    VAGRANT_DIR = ''
    
    args = {'cmd':'vagrant', 'cmd_args': 'up', 'cwd':VAGRANT_DIR}
    
    def __init__(self):
        super().__init__(self.args)
        
    def run(self, logger):
        logger.log(self.LOG_TITLE, 'Running vagrant halt')
        
        super().run(logger, self.callback)
        
    def callback(self):
        self.logger.log(self.LOG_TITLE, 'Vagrant halted')
        
        

        
        

        