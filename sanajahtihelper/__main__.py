from PyQt5.QtWidgets import QApplication

from .gui import MainWidget


def main():
    app = QApplication([])
    gui = MainWidget()
    gui.setFixedSize(400, 800)
    gui.setWindowTitle('sanajahtihelper')
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
