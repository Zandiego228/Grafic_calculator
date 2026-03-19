import sys
import time
from math import *
from math import e as ee

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
        self.equation = ["x ** 2","x"]
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.y, self.x = y, x
        self.length = length

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(0,0,60,20)
        self.input_field2 = QLineEdit(self)
        self.input_field2.setGeometry(85, 0, 60, 20)
        self.button = QPushButton("Create", self)
        self.button.setGeometry(0,20,60,20)
        self.button.clicked.connect(self.plot_graph)
        self.zoom = 100
        # self.pen = pen
    def plot_graph(self):

        self.equation = [self.input_field.text().strip(), self.input_field2.text().strip()]

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(),Qt.black)
        font = QFont('Arial', 15,)
        axis_pen = QPen(Qt.blue)
        painter.setPen(axis_pen)
        painter.drawLine(0,450,900,450)
        axis_pen = QPen(Qt.green)
        painter.setPen(axis_pen)
        painter.drawLine(450, 0, 450, 900)
        porabula_pen = QPen(Qt.red, 3)
        porabula_pen.setWidth(3)
        painter.setPen(porabula_pen)
        painter.drawText(60,0,"=")
        error = []
        #def parabula_print():

        def error_text():
            for i in range(1, len(error) + 1):
                if error[i - 1] != error[i - 2] or i == 1:
                    painter.drawText(900 - len(error[i - 1]) * 9 - 5, 900 - i * 20, error[i - 1])
        for i, eq in enumerate(self.equation):
            if i == 0:
                porabula_pen = QPen(Qt.red, 3)
            if i == 1:
                porabula_pen = QPen(QColor(200,200, 10), 3)
            prev_x = None
            prev_y = None
            for x1 in range(-450, 450):
                #if self.equation != "":
                x = x1 / self.zoom
                try:
                    y = eval(eq, {"__builtins__":None},{
                             "x":x,
                        'sin':sin,
                        "cos": cos,
                        "e":ee,
                        "pi": pi,
                        "log": log,
                        "sqrt":sqrt,
                        "tan": tan
                    })
                    if not isinstance(y, (int, float)):
                        prev_x = None
                        prev_y = None
                        continue

                    y = float(y)*self.zoom
                    screen_x = 450 + int(x * self.zoom)
                    screen_y = 450 - int(y)
                    if prev_x is not None and (-100 * 40) < y < (100 * 40):
                        painter.setPen(porabula_pen)
                        painter.drawLine(prev_x, prev_y, screen_x, screen_y)
                    prev_x = screen_x
                    prev_y = screen_y

                except Exception as e:
                    error.append(f"ошибка: {e}")
                    prev_x = None
                    prev_y = None


            painter.setPen(QColor(255,255, 200))
            painter.setFont(font)
        error_text()
        #painter.setPen(porabula_pen)

    def wheelEvent(self, event):
        # Получаем величину прокрутки
        delta = event.angleDelta().y()
        if delta > 0:
            self.zoom += 10
        else:
            self.zoom -= 10
        print(self.zoom)
        if self.zoom < 10:
            self.zoom = 10

        self.update()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())