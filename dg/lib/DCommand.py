from subprocess import run, Popen, PIPE, STDOUT, CalledProcessError
import threading


class DCommandMgr():
    def __init_(self):
        pass


class DCommand():
    title = 'DCommand'

    def __init__(self):
        pass


class DShellCommand(DCommand):
    LOG_TITLE = 'SHELL'
    
    def __init__(self, args):
        super().__init__()
        
        self.cmd = '{} {}'.format(args['cmd'], ' '.join(args['cmd_args']))
        self.cwd = args['cwd'] if 'cwd' in args else None
    
    def run(self, logger, callback=None):
        self.logger = logger
        t = threading.Thread(target=self.run_cmd, args=(callback,))
        t.start()
    
    def run_cmd(self, callback):
        with Popen(self.cmd, cwd=self.cwd, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in iter(p.stdout.readline, ''):
                if line != '' and line != '\n':
                    self.logger.log(self.LOG_TITLE, line)
                    
        if callback:
            callback()

class DScript():
    def run(self, logger, callback=None):
        self.logger = logger
        t = threading.Thread(target=self.run_cmd, args=(callback,))
        t.start()