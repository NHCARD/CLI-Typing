from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QVBoxLayout
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 300)
        self.center()

        btn_word = QPushButton('단어 연습', self)

        btn_short = QPushButton('짧은글 연습', self)

        btn_long = QPushButton('긴글 연습', self)

        vbox = QVBoxLayout()
        vbox.addWidget(btn_word)
        vbox.addWidget(btn_short)
        vbox.addWidget(btn_long)

        self.setLayout(vbox)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cr = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cr)
        self.move(qr.topLeft())


class Word(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.show()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
