import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.timer = self.startTimer(1000)  # 1秒启动一次计时器
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

    def timerEvent(self, event):
        if event.timerId() == self.timer:
            self.my_values += 1
            if self.my_values % 2 == 0:
                pixmap = QPixmap('auto_player/t/p1.png')
            else:
                pixmap = QPixmap('auto_player/t/zidane.jpg')
            self.label.setPixmap(pixmap)
        else:
            super().timerEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec())
