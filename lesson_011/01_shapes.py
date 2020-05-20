# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(n=3, point=sd.get_point(200, 200), angle=12, length=70, color=sd.COLOR_YELLOW):
        step_angle = int(360 / n)  # предлагаю выполнить round() здесь
        end_angle = int(360 - step_angle)  # и здесь. Не будем приводить к int() внутри range()

        rib_end = point
        for figure_angle in range(0, end_angle, step_angle):
            rib_end = sd.vector(start=rib_end,
                                angle=angle + figure_angle,  # отличный выход!
                                length=length,
                                width=1,
                                color=color)
        sd.line(point, rib_end, width=1, color=color)

    return draw_figure


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


# TODO: есть баг. Почему вместо квадрата снова треугольника
draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(400, 400), angle=0, length=100)

sd.pause()
