# Grafic calculator
>**_Grafic calculator_** - проект для решение и показ рения уравнений

---
#### что это такое?

это проект который упрощает решение уравнений и показывает график левой и правой частей

#### главные команды
все вычисления
>x,sin,cos,e,pi,log,sqrt,tan,tanh,asin,acos,atan,sinh,cosh,exp,fabs,*,+,**,-,/,//

#### как пользоваться графическим  калькулятором

1.[зайдите на эту сcылку]()
2.скачайте `calculator.exe`
3.запустите `calculator.exe`

__!!!важно!!!__
`этот способ работает только для windows`
`для linux и macOS  другие способы`

```python
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    ex = Calculator()  
    ex.show()  
    sys.exit(app.exec_())
```
это запуск калькулятора
~~~python
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
  
    painter.setPen(QColor(20, 20, 200))  
    painter.setFont(font)  
    painter.drawText(65, 20, "=")  
  
    font = QFont('Arial', 15)  
    if self.zoom < 1:  
        painter.drawText(20, self.WIDTH - 10, f"zoom: {self.zoom:.2f}")  
    else:  
        painter.drawText(20, self.WIDTH - 10, f"zoom: {int(self.zoom)}")  
  
    painter.setPen(QColor(255, 255, 255))  
    painter.setFont(QFont('Arial', 10))  
    painter.drawText(250, 18, self.solution_text)  
  
    painter.setFont(font)  
    if self.zoom < 0.01:  
        self.zoom *= 1.1  
  
    error = []  
  
    def error_text():  
        for i in range(1, len(error) + 1):  
            if i == 1 or error[i - 1] != error[i - 2]:  
                painter.drawText(900 - len(error[i - 1]) * 9 - 5, 900 - i * 20, error[i - 1])  
  
    for i, eq in enumerate(self.equation):  
        if i == 0:  
            parabola_pen = QPen(QColor(193, 67, 67), 3)  
        else:  
            parabola_pen = QPen(QColor(200, 200, 10), 3)  
  
        prev_x = None  
        prev_y = None  
  
        for x1 in range(-450, 450):  
            if self.equation[i] != '':  
                x = x1 / self.zoom  
                try:  
                    y = eval(eq, {"__builtins__": None}, {  
                        "x": x,  
                        "sin": sin,  
                        "cos": cos,  
                        "e": ee,  
                        "pi": pi,  
                        "log": log,  
                        "sqrt": sqrt,  
                        "tan": tan,  
                        "tanh": tanh,  
                        "asin": asin,  
                        "acos": acos,  
                        "atan": atan,  
                        "sinh": sinh,  
                        "cosh": cosh,  
                        "exp": exp,  
                        "fabs": fabs,  
                    })  
  
                    if -0.0001 < abs(y) < 0.0001:  
                        y = 0  
  
                    y = y.real  
  
                    if not isinstance(y, (int, float)):  
                        prev_x = None  
                        prev_y = None  
                        continue  
                    y = float(y) * self.zoom  
                    screen_x = 450 + int(x * self.zoom)  
                    screen_y = 450 - int(round(y, 5))  
  
                    if prev_x is not None and (-100 * 40) < y < (100 * 40):  
                        painter.setPen(parabola_pen)  
                        painter.drawLine(prev_x, prev_y, screen_x, screen_y)  
  
                    prev_x = screen_x  
                    prev_y = screen_y  
  
                except Exception as e:  
                    error.append(f"ошибка: {e}")  
                    prev_x = None  
                    prev_y = None
~~~
Это основной код. Там происходят вычисления графика и его показ на экране
~~~python
        for x1 in range(-450, 450):  
            if self.equation[i] != '':  
                x = x1 / self.zoom  
                try:  
                    y = eval(eq, {"__builtins__": None}, {  
                        "x": x,  
                        "sin": sin,  
                        "cos": cos,  
                        "e": ee,  
                        "pi": pi,  
                        "log": log,  
                        "sqrt": sqrt,  
                        "tan": tan,  
                        "tanh": tanh,  
                        "asin": asin,  
                        "acos": acos,  
                        "atan": atan,  
                        "sinh": sinh,  
                        "cosh": cosh,  
                        "exp": exp,  
                        "fabs": fabs,  
                    })  
  
                    if -0.0001 < abs(y) < 0.0001:  
                        y = 0  
  
                    y = y.real  
~~~
эта часть кода решает где решается точки на графике
