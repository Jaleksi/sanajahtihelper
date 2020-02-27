from PyQt5 import QtWidgets


class WordList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel("Label")
        self.letter_grid = LetterGrid()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.letter_grid)
        self.setLayout(layout)


class LetterGrid(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QtWidgets.QGridLayout()
        self.button_widgets = [LetterButton(i, j) for i in range(4) for j in range(4)]

        for button in self.button_widgets:
            self.grid.addWidget(button, button.x, button.y)

        self.setLayout(self.grid)
    
    def keyPressEvent(self, event):
        for button in self.button_widgets:
            if button.listening:
                button.set_letter(chr(event.key()))


class LetterButton(QtWidgets.QPushButton):
    def __init__(self, x, y):
        # QPushButton methods
        super().__init__()
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

    def set_letter(self, letter):
        self.setText(letter)
        self.listening = False
        self.setStyleSheet("background-color: #FFCC99;")
        

