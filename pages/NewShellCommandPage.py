
from PyQt5.QtCore import Qt
from dg.gui.DCore import DFrame, DPage
from dg.gui.DLayout import DVBoxLayout
from dg.gui.DMaterials import DBuildMaterials
from dg.gui.DWidgets import DColorPicker, DInputField, DLabel, DButton


class NewShellCommandPage(DPage):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.model = self.getApp().getModel('NewCommandModel')
        
    def prepare(self):
        super().prepare()
        
        self.layout = DVBoxLayout()
        self.layout.alignCenter()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10,10,10,10)
        
        self.title_frame = NewShellInputFrame(self, 'Title')
        self.command_frame = NewShellInputFrame(self, 'Command')
        self.args_frame = NewShellInputFrame(self, 'Arguments')
        self.cwd_frame = NewShellInputFrame(self, 'Change working dir to')
        
        self.color_picker = DColorPicker(self)
        
        self.save_button = SaveButton('Save')
        self.save_button.clicked.connect(self.saveButtonAction)
        

        
    def build(self):
        super().build()
        
        
        self.setLayout(self.layout)
        
        self.title_frame.build()
        self.command_frame.build()
        self.args_frame.build()
        self.cwd_frame.build()
        
        self.color_picker.build()
        self.color_picker.randomize()
        
        self.layout.addWidget(self.title_frame)
        self.layout.addWidget(self.command_frame)
        self.layout.addWidget(self.args_frame)
        self.layout.addWidget(self.cwd_frame)
        
        self.layout.addWidget(self.color_picker, alignment=self.layout.CENTER)
        
        self.layout.addWidget(self.save_button, alignment=self.layout.CENTER)
        
    
    def saveButtonAction(self):
        title = self.title_frame.getText()
        cmd = self.command_frame.getText()
        cmd_args = self.args_frame.getText()
        cwd = self.cwd_frame.getText()
        color = self.color_picker.getColor()
        
        data = {}
        data['type'] = 'Shell'
        data['color'] = color
        
        args = {}
        args['cmd'] = cmd
        args['cmd_args'] = cmd_args.split(',')
        
        
        
        if cwd != '' and cwd != None:
            args['cwd'] = cwd
            
        data['args'] = args
        
        if title != '' and cmd != '':
            self.model.saveNewShellCommand(title, data)
            
        self.title_frame.clear()
        self.command_frame.clear()
        self.args_frame.clear()
        self.cwd_frame.clear()
            
        self.getApp().setPage('CommandsPage')

        
        
class NewShellInputFrame(DFrame):
    def __init__(self, parent, text):
        super().__init__(parent)
        
        self.text = text
        
    def prepare(self):
        super().prepare()
        
        self.layout = DVBoxLayout()
        self.layout.alignCenter()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10,10,10,10)
        
        self.label = DLabel()
        self.label.setText(self.text)
        
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
        


        
