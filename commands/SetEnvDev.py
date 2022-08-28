from lib.SetEnvironmentCommand import SetEnvironmentCommand


class SetEnvDev(SetEnvironmentCommand):
    ENVIRONMENT = 'development'
    
    def __init__(self):
        super().__init__(self.ENVIRONMENT)
        
        self.name = 'set development'
        
        
    def run(self, logger):
        super().run(logger)
                
                    
                    
                    
