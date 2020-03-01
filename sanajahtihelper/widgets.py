from PyQt5 import QtWidgets, QtGui


class LetterButton(QtWidgets.QPushButton):
    def __init__(self, x, y, parent): 
        super().__init__()
        self.parent = parent
        font = QtGui.QFont()
        font.setPointSize(24)
        self.setFont(font)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.setStyleSheet("background-color: #FFCC99;")
        self.clicked.connect(lambda: self.listen())
        self.x = x 
        self.y = y 
        self.listening = False

    def listen(self):
        if not self.parent.edit_mode:
            return
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


class FoundWord(QtWidgets.QListWidgetItem):
    def __init__(self, word, indexes):
        super().__init__()
        self.indexes = indexes
        self.word = word
        self.setText(self.word)
