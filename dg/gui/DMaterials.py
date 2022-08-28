


class DMaterialsContainer():
    def __init__(self):
        self.materials_unpack_queue = []

    def unpack(self):
        while len(self.materials_unpack_queue) > 0:
            materials = self.materials_unpack_queue.pop(0)
            for title, item in materials.__dict__.items():
                self.__setattr__(title, item)

    def validateMaterials(self):
        for mats in self.materials_unpack_queue:
            mats.validate()

    def add(self, build_mats):
        self.materials_unpack_queue.append(build_mats)



class DBuildMaterials():
    def __init__(self):
        pass



class DAppBuildMaterials(DBuildMaterials):
    def __init__(self):
        super().__init__()

        self.name = 'app'



class DWindowBuildMaterials(DBuildMaterials):
    def __init__(self):
        super().__init__()

        self.name = 'window'
        self.title = 'App title'
        self.rect = (150,150,1200,800)

        
        

        
    
   