from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtCore import Qt


from dg.gui.DCore import DAlign
    

class DLayout():
    
    def clear(self):
        while self.count():
            child = self.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

class DHBoxLayout(QHBoxLayout, DLayout, DAlign):
    def __init__(self):
        super().__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class DVBoxLayout(QVBoxLayout, DLayout, DAlign):
    def __init__(self):
        super().__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class DGridLayout(QGridLayout, DLayout, DAlign):
    def __init__(self):
        super().__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class DStackedLayout(QStackedLayout, DLayout, DAlign):
    def __init__(self):
        super().__init__()


class DFastGridLayout(QGridLayout, DLayout, DAlign):
    def __init__(self, cols):
        super().__init__()
        self.cols = cols
        
        self.count_row = 0
        self.count_column = 0

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)
        
    def addWidget(self, widget):
        super().addWidget(widget, self.count_row, self.count_column)
        self.shift()

    def shift(self):
        self.count_column += 1
        if self.count_column >= self.cols:
            self.count_column = 0
            self.count_row += 1
            
    def clear(self):
        super().clear()
        
        self.count_row = 0
        self.count_column = 0
        
        
            











