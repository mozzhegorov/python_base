# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_triangle_v1(start_point=sd.get_point(100, 100), angle=0, length=50):
    vector_start_point = start_point
    for figure_angle in range(0, 240, 120):
        rib = sd.get_vector(start_point=vector_start_point,
                            angle=angle + figure_angle,
                            length=length,
                            width=1)
        print(figure_angle)
        rib.draw()
        vector_start_point = rib.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_YELLOW)


def draw_square_v1(start_point=sd.get_point(400, 100), angle=100, length=100):
    vector_start_point = start_point
    for figure_angle in range(0, 270, 90):
        rib = sd.get_vector(start_point=vector_start_point,
                            angle=angle + figure_angle,
                            length=length,
                            width=1)
        rib.draw()
        vector_start_point = rib.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_YELLOW)


def draw_pentagon_v1(start_point=sd.get_point(100, 400), angle=60, length=50):
    vector_start_point = start_point
    for figure_angle in range(0, 288, 72):
        rib = sd.get_vector(start_point=vector_start_point,
                            angle=angle + figure_angle,
                            length=length,
                            width=1)
        rib.draw()
        vector_start_point = rib.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_YELLOW)


def draw_hexagon_v1(start_point=sd.get_point(400, 400), angle=12, length=70):
    vector_start_point = start_point
    for figure_angle in range(0, 300, 60):
        rib = sd.get_vector(start_point=vector_start_point,
                            angle=angle + figure_angle,
                            length=length,
                            width=1)
        rib.draw()
        vector_start_point = rib.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_YELLOW)


# draw_triangle(length=400)
# draw_square()
# draw_pentagon()
# draw_hexagon()

#  Баг с ребром убран. Имя дано "нейтральное" (в целом, было достаточно убрать у "v1" единичку - "v").


#  .
#  Пофиксите баг, можете приступать ко 2ой части.
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

#  сюда должен войти еще и цикл и рассчет угла.
#  по факту, draw_triangle будет делать только 2 вещи: определять число сторон и вызывать draw_figure.
def draw_figure(num_ribs, start_point=sd.get_point(400, 400), angle=12, length=70, color=sd.COLOR_YELLOW):
    step_angle = int(360 / num_ribs)  # предлагаю выполнить round() здесь
    end_angle = int(360 - step_angle)  # и здесь. Не будем приводить к int() внутри range()

    rib_end = start_point
    for figure_angle in range(0, end_angle, step_angle):
        rib_end = sd.vector(start=rib_end,
                            angle=angle + figure_angle,  # отличный выход!
                            length=length,
                            width=1,
                            color=color)
    sd.line(start_point, rib_end, width=1, color=sd.COLOR_YELLOW)


def draw_triangle(start_point=sd.get_point(100, 100), angle=0, length=50):
    draw_figure(3, start_point, angle=angle, length=length)
    # sd.line(start_point, end_line_point, width=1, color=sd.COLOR_YELLOW)  #  это эквивалетно


def draw_square(start_point=sd.get_point(100, 400), angle=0, length=50):
    draw_figure(4, start_point, angle=angle, length=length)
    # sd.line(start_point, end_line_point, width=1, color=sd.COLOR_YELLOW)  #  ... этому. Значит что?
    #  Значит вызов этой ф-ции тоже кусочек общей части.


def draw_pentagon(start_point=sd.get_point(400, 100), angle=0, length=50):
    draw_figure(5, start_point, angle=angle, length=length)


def draw_hexagon(start_point=sd.get_point(400, 400), angle=0, length=50):
    draw_figure(6, start_point, angle=angle, length=length)


#  почти закончили 2ую часть. Можно добавить 2 оставшиеся фигуры.
#  Давайте для ф-ций из 1ой части сделаем суфикс _v1, а для ф-ций из 2ой части, наоборот - уберем.
draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()

sd.pause()
