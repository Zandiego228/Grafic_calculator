import sys
import time
from math import *
from random import *
randint(1,10)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRectF
#from pygame.examples.headless_no_windows_needed import screen
WIDTH, HEIGHT = 900, 900
y = 400
x = 400
length = 100
equation = ["x ** 2","10"]


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.equation = 'x**x'
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.y, self.x = y, x
        self.length = length

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(0,0,60,20)

        self.button = QPushButton("Create", self)
        self.button.setGeometry(0,20,60,20)
        self.button.clicked.connect(self.plot_graph)
        self.zoom = 100
        # self.pen = pen
    def plot_graph(self):

        self.equation = self.input_field.text().strip()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        font = QFont('Arial', 15)
        axis_pen = QPen(Qt.blue)
        painter.setPen(axis_pen)
        painter.drawLine(0,450,900,450)
        axis_pen = QPen(Qt.green)
        painter.setPen(axis_pen)
        painter.drawLine(450, 0, 450, 900)
        porabula_pen = QPen(Qt.yellow, 3)
        porabula_pen.setWidth(3)
        painter.setPen(porabula_pen)
        prev_x = None
        prev_y = None
        error = []
        #def parabula_print():

        def error_text():
            for i in range(1, len(error) + 1):
                if error[i - 1] != error[i - 2] or i == 1:
                    painter.drawText(900 - len(error[i - 1]) * 9 - 5, 900 - i * 20, error[i - 1])

        for x1 in range(-450, 450):
            #if self.equation != "":
            x = x1 / self.zoom
            try:
                y = eval(self.equation.lower())*self.zoom
                y = float(f"{y:.5f}")
            except Exception as e:
                error.append(f"ошибка: {e}")

            else:
                screen_x = 450+int(x*self.zoom)
                screen_y = 450-int(y)
                if prev_x is not None and (-100*40) < y < (100*40):
                    painter.setPen(porabula_pen)
                    painter.drawLine(prev_x, prev_y, screen_x, screen_y)
                prev_x = screen_x
                prev_y = screen_y
            painter.setPen(QColor(0, 0, 0))
            painter.setFont(font)
        error_text()
        #painter.setPen(porabula_pen)

        '''    def wheelEvent(self, event):
        # Получаем величину прокрутки
        delta = event.angleDelta().y()
        if delta > 0:
            self.zoom += 2
        else:
            self.zoom -= 2'''





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())