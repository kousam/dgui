from lib.SetEnvironmentCommand import SetEnvironmentCommand


class SetEnvUnitTest(SetEnvironmentCommand):
    ENVIRONMENT = 'unit_testing'
    
    def __init__(self):
        super().__init__(self.ENVIRONMENT)
        
        self.name = 'set unit_testing'
        
    def run(self, logger):
        super().run(logger)
                