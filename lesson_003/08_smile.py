# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def draw_smile(x, y, color):
    sd.ellipse(sd.get_point(y - 50, x - 50), sd.get_point(y + 50, x + 20), color, 2)
    sd.line(sd.get_point(y - 10, x - 30), sd.get_point(y + 10, x - 30), color, 2)
    sd.line(sd.get_point(y - 10, x - 30), sd.get_point(y - 20, x - 20), color, 2)
    sd.line(sd.get_point(y + 20, x - 20), sd.get_point(y + 10, x - 30), color, 2)
    sd.circle(sd.get_point(y + 15, x), 7, color, 1)
    sd.circle(sd.get_point(y - 15, x), 7, color, 1)

for _ in range(10):

    center_x = random.randrange(50, sd.resolution[1] - 50)
    center_y = random.randrange(50, sd.resolution[0] - 50)
    draw_smile(center_x, center_y, sd.random_color())

sd.pause()

# зачет!