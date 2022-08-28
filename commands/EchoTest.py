from lib.ShellCommand import ShellCommand


class EchoTest(ShellCommand):
    
    def __init__(self):
        super().__init__('echo', ['test'])
        self.name = 'Echo test'
        