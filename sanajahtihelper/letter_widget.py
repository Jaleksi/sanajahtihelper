from PyQt5 import QtWidgets, QtGui


class LetterButton(QtWidgets.QPushButton):
    def __init__(self, x, y): 
        # QPushButton methods
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(24)
        self.setFont(font)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.setStyleSheet("background-color: #FFCC99;")
        self.clicked.connect(lambda: self.listen())
        # Custom attributes
        self.x = x 
        self.y = y 
        self.listening = False

    def listen(self):
        self.listening = True
        self.setStyleSheet("background-color: #FF9157;")

    def dont_listen(self):
        self.listening = False
        self.setStyleSheet("background-color: #FFCC99;")
    
    def set_letter(self, letter):
        self.setText(letter)
        self.dont_listen()

    def clear_text(self):
        self.setText(None)
        self.listening = False
