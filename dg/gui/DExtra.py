
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor


class DShadow(QGraphicsDropShadowEffect):
    def __init__(self):
        super().__init__()
        self.setBlurRadius(16)
        self.setOffset(2,2)
        self.setColor(QColor(10,10,10,180))
        
class DShadowDark(QGraphicsDropShadowEffect):
    def __init__(self):
        super().__init__()
        self.setBlurRadius(14)
        self.setOffset(2,2)
        self.setColor(QColor(0,0,0,180))
        
    