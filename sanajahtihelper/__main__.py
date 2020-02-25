import sys
from PyQt5.QtWidgets import QApplication

from .gui import MainWindow


def main():
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.setFixedSize(400, 800)
    gui.setWindowTitle('sanajahtihelper')
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
