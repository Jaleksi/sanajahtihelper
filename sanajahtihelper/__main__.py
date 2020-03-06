from PyQt5.QtWidgets import QApplication

from .gui import MainWindow


def main():
    app = QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
