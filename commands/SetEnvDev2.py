from lib.SetEnvironmentCommand import SetEnvironmentCommand


class SetEnvDev2(SetEnvironmentCommand):
    ENVIRONMENT = 'development2'
    
    def __init__(self):
        super().__init__(self.ENVIRONMENT)
        
        self.name = 'set development2'
        
        
    def run(self, logger):
        super().run(logger)
                