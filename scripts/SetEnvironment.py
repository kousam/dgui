
from dg.lib.DCommand import DScript


class SetEnvironment(DScript):
    LOG_TITLE = 'SCRIPT'
    ARGS = ['environment']
    
    def __init__(self, args):
        super().__init__()
        #self.file = r'C:\dev\Sites\tehden\environment.php'
        self.file = r'C:\Users\xdwes\Documents\Python\dwopgui\dgui\test\environment.php'
        
        self.environments = {}
        self.environments['unit_testing'] = "define('ENVIRONMENT', 'unit_testing');"
        self.environments['development'] = "define('ENVIRONMENT', 'development');"
        self.environments['development2'] = "define('ENVIRONMENT', 'development2');"
        
        self.environment = args['environment']
        
    def run(self, logger):
        order = {}
        lines = []
        
        with open(self.file, 'r') as file:
            lines = []        
            for line in file:
                lines.append(line)
        
        for key, env in self.environments.items():
            for i in range(len(lines)):
                if lines[i].find(env) != -1:
                    order[key] = i

        for env, i in order.items():
            if env == self.environment:
                lines[i] = '{}\n'.format(self.environments[env])
            
            else:
                lines[i] = '//{}\n'.format(self.environments[env])
        
        with open(self.file, 'w') as file:
            for line in lines:
                file.write(line)
                
        logger.log(self.LOG_TITLE, 'Environment set to "{}"'.format(self.environment))
            