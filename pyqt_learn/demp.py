import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QPixmap
import typing


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.my_values = 0
        self.initUI()



    def initUI(self):
        self.label = QLabel(self)
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('auto_player/t/p1.png')
        self.label.setPixmap(pixmap)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.setMouseTracking(True)
        self.setWindowTitle('Event object')
        self.show()

    def mousePressEvent(self, e):
        self.my_values += 1
        if self.my_values % 2 == 0:
            pixmap = QPixmap('auto_player/t/p1.png')
        else:
            pixmap = QPixmap('auto_player/t/zidane.jpg')
        self.label.setPixmap(pixmap)



def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
