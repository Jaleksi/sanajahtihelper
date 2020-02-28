from PyQt5 import QtWidgets, QtGui, QtCore


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
        grid = QtWidgets.QGridLayout()
        self.button_widgets = [LetterButton(i, j) for i in range(4) for j in range(4)]
        
        for button in self.button_widgets:
            grid.addWidget(button, button.x, button.y)

        self.setLayout(grid)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            print("OK")
        elif event.key() == QtCore.Qt.Key_Delete:
            self.clear_grid()

        elif self.listening_buttons():
            for button in self.listening_buttons():
                try:
                    button.set_letter(chr(event.key()))
                except ValueError:
                    pass

    def clear_grid(self):
        for button in self.button_widgets:
            button.clear_text()

    def listening_buttons(self):
        return [button for button in self.button_widgets if button.listening]

    def all_buttons_set(self):
        return all(button.text() for button in self.button_widgets)

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

    def set_letter(self, letter):
        self.setText(letter)
        self.listening = False
        self.setStyleSheet("background-color: #FFCC99;")
        
    def clear_text(self):
        self.setText(None)
        self.listening = False
