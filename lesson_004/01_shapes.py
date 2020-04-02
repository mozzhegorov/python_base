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


def draw_triangle(start_point=sd.get_point(100, 100), angle=0, length=50):
    vector_start_point = start_point
    for figure_angle in range(0, 360, 120):
        # TODO: только вместо "v1" дайте какое-нибудь нейтральное имя. Или уточните, когда появится v_2 или v_0)
        v1 = sd.get_vector(start_point=vector_start_point,
                           angle=angle + figure_angle,
                           length=length,
                           width=1)
        v1.draw()
        vector_start_point = v1.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_WHITE)


def draw_square(start_point=sd.get_point(400, 100), angle=100, length=100):
    vector_start_point = start_point
    for figure_angle in range(0, 270, 90):
        v1 = sd.get_vector(start_point=vector_start_point,
                           angle=angle + figure_angle,
                           length=length,
                           width=1)
        v1.draw()
        vector_start_point = v1.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_WHITE)


def draw_pentagon(start_point=sd.get_point(100, 400), angle=60, length=50):
    vector_start_point = start_point
    for figure_angle in range(0, 288, 72):
        v1 = sd.get_vector(start_point=vector_start_point,
                           angle=angle + figure_angle,
                           length=length,
                           width=1)
        v1.draw()
        vector_start_point = v1.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_WHITE)


def draw_hexagon(start_point=sd.get_point(400, 400), angle=12, length=70):
    vector_start_point = start_point
    for figure_angle in range(0, 300, 60):
        v1 = sd.get_vector(start_point=vector_start_point,
                           angle=angle + figure_angle,
                           length=length,
                           width=1)
        v1.draw()
        vector_start_point = v1.end_point
    sd.line(start_point, vector_start_point, width=1, color=sd.COLOR_WHITE)


draw_triangle(length=400)
draw_square()
draw_pentagon()
draw_hexagon()

# TODO: Делая ребра векторами, обнаруживался лаг, когда фигура была не доведена до конца.
#  заключительное ребро ресуется с помощью line

# TODO: Ответ. Мысль верная) Но есть баг. В каждой фигуре добавил "последнюю грань рисовать белым". У треугольника
#  грань осталось желтой. Как думаете почему?
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


sd.pause()
