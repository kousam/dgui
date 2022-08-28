from subprocess import run, Popen, PIPE, STDOUT, CalledProcessError


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
        
    def run(self, logger):
        with Popen(self.cmd, cwd=self.cwd, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                logger.log(self.LOG_TITLE, line)


class DScript():
    def __init__(self):
        pass