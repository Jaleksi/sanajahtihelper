from PyQt5 import QtWidgets, QtCore

from .utils import GridFinder
from .letter_widget import LetterButton
from .word_widget import FoundWord

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.word_list = WordList()
        self.letter_grid = LetterGrid(self.word_list)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.word_list)
        layout.addWidget(self.letter_grid)
        self.setLayout(layout)

class WordList(QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
    
    def load_found_to_list(self, words):
        self.clear()
        for word in words:
            self.addItem(word.word)



class LetterGrid(QtWidgets.QWidget):
    def __init__(self, word_list):
        super().__init__()
        self.word_list = word_list
        grid = QtWidgets.QGridLayout()
        self.grid_finder = GridFinder()
        self.button_widgets = [LetterButton(i, j) for i in range(4) for j in range(4)]
        
        for button in self.button_widgets:
            grid.addWidget(button, button.x, button.y)

        self.setLayout(grid)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.start_search()
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
            button.dont_listen()

    def listening_buttons(self):
        return [button for button in self.button_widgets if button.listening]
    
    def all_buttons_set(self):
        return all(button.text() for button in self.button_widgets)

    def start_search(self):
        if not self.all_buttons_set():
            return

        grid = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]

        for button in self.button_widgets:
            grid[button.x][button.y] = button.text().lower()

        found = self.grid_finder.search(grid)
        self.word_list.load_found_to_list(found)
