from PyQt5 import QtWidgets


class WordGrid(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QtWidgets.QVBoxLayout(self)
        teksti = QtWidgets.QLabel(self)
        teksti.setText('asd')
        layout.addWidget(teksti)

class WordList(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(self.main_widget)

        self.word_grid = WordGrid(self)
        self.word_list = WordList(self)

        layout.addWidget(self.word_grid)
        layout.addWidget(self.word_list)
