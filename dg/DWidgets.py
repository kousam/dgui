
from PyQt5.QtWidgets import QFrame ,QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QFont


class DHomePageButton(QPushButton):
    WIDTH = 100
    HEIGHT = 60

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('homepage_button')
        self.setFont(QFont("Roboto", 14))
        self.setFixedSize(self.WIDTH, self.HEIGHT)


class DSideBarButton(QPushButton):
    WIDTH = 40
    HEIGHT = 40

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('sidebar_button')
        self.setFont(QFont("Roboto", 12))
        self.setFixedSize(self.WIDTH, self.HEIGHT)

class DSideBarHomeButton(QPushButton):
    WIDTH = 40
    HEIGHT = 40

    def __init__(self, text):
        super().__init__(text)
        self.setObjectName('sidebar_home_button')
        self.setFont(QFont("Roboto", 12))
        self.setFixedSize(self.WIDTH, self.HEIGHT)


class DInputField(QLineEdit):
    HEIGHT = 26
    def __init__(self):
        super().__init__()
        self.setObjectName('input_field')
        self.setFont(QFont("Roboto", 12))
        self.setFixedHeight(self.HEIGHT)


