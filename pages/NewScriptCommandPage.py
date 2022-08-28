from PyQt5.QtCore import Qt
from dg.gui.DCore import DFrame, DPage
from dg.gui.DLayout import DVBoxLayout
from dg.gui.DMaterials import DBuildMaterials
from dg.gui.DWidgets import DColorPicker, DInputField, DLabel, DButton


class NewScriptCommandPage(DPage):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.model = self.getApp().getModel('NewCommandModel')
        
    def prepare(self):
        super().prepare()
        
        self.script = self.model.getScript()
        self.args = self.model.getScriptArgs()
        
        self.layout = DVBoxLayout()
        self.layout.alignCenter()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10,10,10,10)
        
        self.title_frame = NewScriptInputFrame(self, 'Title')
        
        self.script_frame = NewScriptFrame(self)
        
        self.color_picker = DColorPicker(self)
        
        self.save_button = SaveButton('Save')
        self.save_button.clicked.connect(self.saveButtonAction)
        

        
    def build(self):
        super().build()
        
        
        self.setLayout(self.layout)
        
        self.script_frame.build()
        self.addArgs()
        
        self.title_frame.build()
        
        self.color_picker.build()
        self.color_picker.randomize()
        
        self.layout.addWidget(self.title_frame)
        
        self.layout.addWidget(self.script_frame)

        
        self.layout.addWidget(self.color_picker, alignment=self.layout.CENTER)
        
        self.layout.addWidget(self.save_button, alignment=self.layout.CENTER)
        
        
    def onShow(self):
        super().onShow()
        self.script_frame.clear()
        self.addArgs()
        
    def addArgs(self):
        for arg in self.args:
            self.script_frame.addArg(arg)
    
    def saveButtonAction(self):
        color = self.color_picker.getColor()
        
        title = self.title_frame.getText()
        
        data = {}
        data['type'] = 'Script'
        data['color'] = color
        data['script'] = self.script
        
        args = self.script_frame.getArgs()
        
        data['args'] = args
        
        self.model.saveNewScriptCommand(title, data)

        #self.getApp().setPage('CommandsPage')




class NewScriptFrame(DFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.frames = []

        
    def prepare(self):
        super().prepare()
        
        self.layout = DVBoxLayout()
        self.layout.alignCenter()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10,10,10,10)
        
    def build(self):
        super().build()
        
        self.setLayout(self.layout)
    
    def clear(self):
        self.frames = []
        self.layout.clear()
        
        
    def addArg(self, title):
        frame = NewScriptInputFrame(self, title)
        frame.build()
        self.layout.addWidget(frame)
        self.frames.append(frame)
        
    def getArgs(self):
        data = {}
        for frame in self.frames:
            data[frame.title] = frame.getText()
            
        return data
        
class NewScriptInputFrame(DFrame):
    def __init__(self, parent, title):
        super().__init__(parent)
        
        self.title = title
        
    def prepare(self):
        super().prepare()
        
        self.layout = DVBoxLayout()
        self.layout.alignCenter()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10,10,10,10)
        
        self.label = DLabel()
        self.label.setText(self.title)
        
        self.input = NewShellnputField()
        
        
    def build(self):
        super().build()
        
        self.setLayout(self.layout)
        
        self.layout.addWidget(self.label, alignment=self.layout.CENTER)
        self.layout.addWidget(self.input)
        
    def getText(self):
        return self.input.text()
    
    def clear(self):
        self.input.setText('')
        
        
        
        
        
class NewShellnputField(DInputField):
    def __init__(self):
        super().__init__()
        
        self.alignCenter()
        self.setFixedWidth(500)
        
        
class SaveButton(DButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(200,50)
        

