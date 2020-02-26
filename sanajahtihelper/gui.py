from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.word_grid = WordGrid(self)
        self.word_list = WordList(self)

    def master_layout(self):
        self.master_layou
        self.master_layout.addWidget(self.word_list)
        self.master_layout.addWidget(self.word_grid)
        self.setCentralWidget(self.word_grid)


class WordGrid(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.controls()
        self.layout()

    def controls(self):
        self.button = QtWidgets.QPushButton("Button")

    def layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


class WordList(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.controls()
        self.layout()

    def controls(self):
        self.label = QtWidgets.QLabel("BuAtatAon")

    def layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
