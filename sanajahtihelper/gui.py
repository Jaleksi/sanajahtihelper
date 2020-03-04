from PyQt5 import QtWidgets, QtCore

from .utils import GridFinder
from .widgets import LetterButton, FoundWord

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.word_list = WordList(self)
        self.letter_grid = LetterGrid(self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.word_list)
        layout.addWidget(self.letter_grid)
        self.setLayout(layout)


class WordList(QtWidgets.QListWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.itemClicked.connect(self.clicked)

    def load_found_to_list(self, words):
        self.clear()
        for word in words:
            self.addItem(word)

    def clicked(self, item):
        self.parent.letter_grid.highlight_indexes(item.indexes)


class LetterGrid(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        grid = QtWidgets.QGridLayout()
        self.grid_finder = GridFinder()
        self.edit_mode = True
        self.button_widgets = [LetterButton(i, j, self) for i in range(4) for j in range(4)]
        
        for button in self.button_widgets:
            grid.addWidget(button, button.x, button.y)

        self.setLayout(grid)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.start_search()
        elif event.key() == QtCore.Qt.Key_Delete:
            self.clear_grid()

        elif self.edit_mode and self.listening_buttons():
            for button in self.listening_buttons():
                try:
                    button.set_letter(chr(event.key()))
                except ValueError:
                    pass

    def clear_grid(self):
        for button in self.button_widgets:
            button.clear_text()
            button.dont_listen()
        self.parent.word_list.clear()
        self.edit_mode = True

    def listening_buttons(self):
        return [button for button in self.button_widgets if button.listening]
    
    def all_buttons_set(self):
        return all(button.text() for button in self.button_widgets)

    def start_search(self):
        self.edit_mode = False
        if not self.all_buttons_set():
            return

        grid = [[None for _ in range(4)] for _ in range(4)]

        for button in self.button_widgets:
            grid[button.x][button.y] = button.text().lower()

        found = self.grid_finder.search(grid)
        # Sort found words by length
        found.sort(key=lambda x: len(x.word), reverse=True)
        self.parent.word_list.load_found_to_list(found)

    def highlight_indexes(self, indexes):
        for button in self.button_widgets:
            button.setStyleSheet('background-color: #FFCC99;')
            if (button.x, button.y) in indexes:
                button.setStyleSheet('background-color: #FF9157;')

