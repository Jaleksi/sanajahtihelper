import time

from PyQt5 import QtWidgets, QtCore

from .utils import GridFinder
from .widgets import LetterButton


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 400)
        self.setWindowTitle('sanajahtihelper')
        self.setCentralWidget(MainWidget(self))
        self.statusBar().showMessage('')


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.word_list = WordList(self)
        self.letter_grid = LetterGrid(self)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.word_list)
        layout.addWidget(self.letter_grid)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.letter_grid.start_search()
        elif event.key() == QtCore.Qt.Key_Delete:
            self.letter_grid.clear_grid()
        elif self.letter_grid.edit_mode and self.letter_grid.listening_buttons():
            self.letter_grid.broadcast_input(event.text().upper())

    def set_status_message(self, msg):
        self.parent.statusBar().showMessage(msg)


class WordList(QtWidgets.QListWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.itemSelectionChanged.connect(self.activated_event)

    def load_found_to_list(self, words):
        self.clear()
        for word in words:
            self.addItem(word)

    def activated_event(self):
        items = self.selectedItems()
        if not items:
            return
        self.parent.letter_grid.highlight_indexes(items[0].indexes)


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

    def clear_grid(self):
        for button in self.button_widgets:
            button.clear_text()
            button.dont_listen()
        self.parent.word_list.clear()
        self.edit_mode = True

    def listening_buttons(self):
        return [button for button in self.button_widgets if button.listening]

    def broadcast_input(self, key):
        for button in self.listening_buttons():
            button.set_letter(key)

    def all_buttons_set(self):
        return all(button.text() for button in self.button_widgets)

    def start_search(self):
        if not self.all_buttons_set():
            self.parent.set_status_message('Fill grid completely before search!')
            return
        self.parent.set_status_message('Search started...')
        start_time = time.time()
        self.edit_mode = False
        grid = [[None for _ in range(4)] for _ in range(4)]

        for button in self.button_widgets:
            grid[button.x][button.y] = button.text().lower()

        found = self.grid_finder.search(grid)
        # Sort found words by length
        found.sort(key=lambda x: len(x.word), reverse=True)
        self.parent.word_list.load_found_to_list(found)
        longest_word = max(len(w.word) for w in found) if found else 0
        search_time = '{0:.2f}'.format(time.time() - start_time)
        self.parent.set_status_message(f'Search-time: {search_time}s | ' +
                                       f'Found words: {len(found)} | ' +
                                       f'Longest word: {longest_word} letters')

    def highlight_indexes(self, indexes):
        for button in self.button_widgets:
            button.setStyleSheet('background-color: #FFCC99;')
            if (button.x, button.y) in indexes:
                button.setStyleSheet('background-color: #FF9157;')
