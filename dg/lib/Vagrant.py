from dg.lib.DCommand import DShellCommand
import vagrant


class VagrantUpCommand(DShellCommand):
    LOG_TITLE = 'VAGRANT'
    VAGRANT_DIR = ''
    
    args = {'cmd':'vagrant', 'cmd_args': 'up', 'cwd':VAGRANT_DIR}
    
    def __init__(self):
        super().__init__(self.args)
        
        
class VagrantHaltCommand(DShellCommand):
    LOG_TITLE = 'VAGRANT'
    VAGRANT_DIR = ''
    
    args = {'cmd':'vagrant', 'cmd_args': 'up', 'cwd':VAGRANT_DIR}
    
    def __init__(self):
        super().__init__(self.args)
        
        

        
        

        