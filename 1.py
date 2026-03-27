import sys
import time
from math import *
from math import e as ee

from random import *
randint(1, 10)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRectF

WIDTH, HEIGHT = 900, 900
y = 400
x = 400
length = 100
equation = ["x ** 2", "10"]

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.equation = ["x ** 2", "x"]
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.y, self.x = y, x
        self.length = length

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(0, 0, 60, 20)
        self.input_field2 = QLineEdit(self)
        self.input_field2.setGeometry(85, 0, 60, 20)
        self.button = QPushButton("Create", self)
        self.button.setGeometry(0, 20, 60, 20)
        self.button.clicked.connect(self.plot_graph)
        self.zoom = 10
        self.input_field.setStyleSheet("background-color: #2e3852;border: 2px solid #61afef; color: white;")
        self.input_field2.setStyleSheet("background-color: #2e3852;border: 2px solid #61afef; color: white;")

    def plot_graph(self):
        self.equation = [self.input_field.text().strip(), self.input_field2.text().strip()]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(26, 30, 36))
        font = QFont('Arial', 20)
        axis_pen = QPen(Qt.blue)
        painter.setPen(axis_pen)
        painter.drawLine(0, 450, 900, 450)
        axis_pen = QPen(Qt.green)
        painter.setPen(axis_pen)
        painter.drawLine(450, 0, 450, 900)

        painter.setPen(QColor(180, 180, 180))
        font_small = QFont('Arial', 8)
        painter.setFont(font_small)

        center_x = 450
        center_y = 450

        def nice_step(raw_step):
            if raw_step <= 0:
                return 1
            power = floor(log10(raw_step))
            fraction = raw_step / (10 ** power)
            if fraction <= 1:
                nice_fraction = 1
            elif fraction <= 2:
                nice_fraction = 2
            elif fraction <= 5:
                nice_fraction = 5
            else:
                nice_fraction = 10
            return nice_fraction * (10 ** power)

        def format_number(value):
            if abs(value) < 1e-10:
                value = 0
            if abs(value - round(value)) < 1e-10:
                return str(int(round(value)))
            text = f"{value:.6f}".rstrip("0").rstrip(".")
            return text

        target_px = 70
        step_units = nice_step(target_px / self.zoom)
        step_px = step_units * self.zoom

        x_right_units = (self.WIDTH - center_x) / self.zoom
        x_left_units = -center_x / self.zoom
        y_top_units = center_y / self.zoom
        y_bottom_units = -(self.HEIGHT - center_y) / self.zoom

        start_x = ceil(x_left_units / step_units) * step_units
        current_x = start_x
        while current_x <= x_right_units:
            if abs(current_x) > 1e-10:
                px = int(center_x + current_x * self.zoom)
                painter.drawLine(px, center_y - 4, px, center_y + 4)
                painter.drawText(px - 12, center_y + 18, format_number(current_x))
            current_x += step_units

        start_y = ceil(y_bottom_units / step_units) * step_units
        current_y = start_y
        while current_y <= y_top_units:
            if abs(current_y) > 1e-10:
                py = int(center_y - current_y * self.zoom)
                painter.drawLine(center_x - 4, py, center_x + 4, py)
                painter.drawText(center_x + 8, py + 4, format_number(current_y))
            current_y += step_units

        porabula_pen = QPen(QColor(193, 67, 67), 3)
        porabula_pen.setWidth(3)


        painter.setPen(QColor(20, 20, 200))
        painter.setFont(font)
        painter.drawText(65, 20, "=")
        font = QFont('Arial', 15)
        if self.zoom < 1:
            painter.drawText(20, self.WIDTH - 10, f"zoom: {self.zoom:.2f}")
        else:
            painter.drawText(20, self.WIDTH - 10, f"zoom: {int(self.zoom)}")
        painter.setFont(font)
        if self.zoom < 0.01:
            self.zoom *= 1.1

        eer = ["", ""]
        error = []

        def error_text():
            for i in range(1, len(error) + 1):
                if error[i - 1] != error[i - 2] or i == 1:
                    painter.drawText(900 - len(error[i - 1]) * 9 - 5, 900 - i * 20, error[i - 1])

        for i, eq in enumerate(self.equation):
            if i == 0:
                porabula_pen = QPen(QColor(193, 67, 67), 3)
            if i == 1:
                porabula_pen = QPen(QColor(200, 200, 10), 3)
            prev_x = None
            prev_y = None
            for x1 in range(-450, 450):
                if self.equation[i] != '':
                    print(self.equation)
                    x = x1 / self.zoom
                    try:
                        y = eval(eq, {"__builtins__": None}, {
                            "x": x,
                            'sin': sin,
                            "cos": cos,
                            "e": ee,
                            "pi": pi,
                            "log": log,
                            "sqrt": sqrt,
                            "tan": tan,
                            "tanh": tanh,
                        })
                        if not isinstance(y, (int, float)):
                            prev_x = None
                            prev_y = None
                            continue
                        eer[i] += f"{i}\n"
                        y = float(y) * self.zoom
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

            painter.setPen(QColor(255, 255, 200))
            painter.setFont(font)
        error_text()
        if self.equation[0] != '' and self.equation[1] != '':
            print(self.equation)

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if delta > 0:
            self.zoom *= 1.1
        else:
            self.zoom /= 1.1
        print(self.zoom)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
