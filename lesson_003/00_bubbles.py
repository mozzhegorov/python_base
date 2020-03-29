# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 450)

radius = 50
for num_of_circle in range(3):
    radius = radius + 5
    sd.circle(point, radius, sd.COLOR_RED, 1)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubble(center_point, radius_step, color):
#     radius_fun = 30
#     for num_of_circle_fun in range(3):
#         radius_fun = radius_fun + radius_step
#         sd.circle(center_point, radius_fun, color, 1)
#
# bubble(sd.get_point(500, 500), 7, sd.COLOR_CYAN)

# Нарисовать 10 пузырьков в ряд
# for bubles_x in range(100, 1001, 100):
#     bubble(sd.get_point(bubles_x, 100), 4)

# Нарисовать три ряда по 10 пузырьков
# for bubles_y in range(100, 301, 100):
#     for bubles_x in range(100, 1001, 100):
#         bubble(sd.get_point(bubles_x, bubles_y), 4)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# for _ in range(100):
#     bubble(sd.random_point(), 4, (random.randrange(255), random.randrange(255), random.randrange(255)))

sd.pause()

# TODO: закомментировал все выводы пузырьков на экран, кроме первого вывода.
