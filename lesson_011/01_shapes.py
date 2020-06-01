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


def get_polygon(angles):
    def draw_figure(n=angles, point=sd.get_point(200, 200), angle=12, length=70, color=sd.COLOR_YELLOW):
        step_angle = int(360 / n)
        end_angle = int(360 - step_angle)

        rib_end = point
        for figure_angle in range(0, end_angle, step_angle):
            rib_end = sd.vector(start=rib_end,
                                angle=angle + figure_angle,
                                length=length,
                                width=1,
                                color=color)
        sd.line(point, rib_end, width=1, color=color)

    return draw_figure


draw_triangle = get_polygon(angles=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


draw_square = get_polygon(angles=4)
draw_square(point=sd.get_point(400, 400), angle=0, length=100)

sd.pause()

# зачет!