from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QStackedLayout, QGridLayout
from PyQt5.QtCore import Qt


class Alignments():
    alignment = {'r': Qt.AlignRight, 'l': Qt.AlignLeft, 't': Qt.AlignTop, 'b': Qt.AlignBottom, 'c': Qt.AlignCenter, 'hc': Qt.AlignHCenter, 'vc': Qt.AlignVCenter}


class DHBoxLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class DVBoxLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class DGridLayout(QGridLayout):
    def __init__(self):
        super().__init__()

        self.setSpacing(0)
        self.setContentsMargins(0,0,0,0)


class DStackedLayout(QStackedLayout):
    def __init__(self):
        super().__init__()



class DHomeLayout(DGridLayout):
    def __init__(self):
        super().__init__()

        self.setSpacing(20)
        self.setAlignment(Qt.AlignCenter)
        self.setContentsMargins(0,0,20,0)
        











