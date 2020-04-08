# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_triangle(start_point=sd.get_point(100, 100), angle=0, length=50, color=sd.COLOR_YELLOW):
    vector_start_point = start_point
    for figure_angle in range(0, 360, 120):
        v1 = sd.vector(start=vector_start_point,
                       angle=angle + figure_angle,
                       length=length,
                       width=1,
                       color=color)
        vector_start_point = v1
    sd.line(start_point, vector_start_point, width=1, color=color)


def draw_square(start_point=sd.get_point(400, 100), angle=100, length=100, color=sd.COLOR_YELLOW):
    vector_start_point = start_point
    for figure_angle in range(0, 270, 90):
        v1 = sd.vector(start=vector_start_point,
                       angle=angle + figure_angle,
                       length=length,
                       width=1,
                       color=color)
        vector_start_point = v1
    sd.line(start_point, vector_start_point, width=1, color=color)


def draw_pentagon(start_point=sd.get_point(100, 400), angle=60, length=50, color=sd.COLOR_YELLOW):
    vector_start_point = start_point
    for figure_angle in range(0, 288, 72):
        v1 = sd.vector(start=vector_start_point,
                       angle=angle + figure_angle,
                       length=length,
                       width=1,
                       color=color)
        vector_start_point = v1
    sd.line(start_point, vector_start_point, width=1, color=color)


def draw_hexagon(start_point=sd.get_point(400, 400), angle=12, length=70, color=sd.COLOR_YELLOW):
    vector_start_point = start_point
    for figure_angle in range(0, 300, 60):
        v1 = sd.vector(start=vector_start_point,
                       angle=angle + figure_angle,
                       length=length,
                       width=1,
                       color=color)
        vector_start_point = v1
    sd.line(start_point, vector_start_point, width=1, color=color)

# TODO: в этой задаче пусть останется словарь словарей.
#  Попробуем разные подходы)
dict_of_figure = {
    '0':
        {'shape_name': 'треугольник', 'draw': draw_triangle},
    '1':
        {'shape_name': 'квадрат', 'draw': draw_square},
    '2':
        {'shape_name': 'пятиугольник', 'draw': draw_pentagon},
    '3':
        {'shape_name': 'шестиугольник', 'draw': draw_hexagon},
}

print('Возможные фигуры')
for number, figure_info in dict_of_figure.items():
    print(number, ': ', figure_info['shape_name'])




while True:
    global_color = input('Какую фигуру рисуем > ')

    print(global_color.isdecimal())     # TODO: что-то полезное?)
    if global_color.isdecimal() and 0 < int(global_color) < len(dict_of_figure):
        start_point = sd.get_point(sd.resolution[0] // 2, sd.resolution[1] // 2)
        #  перед вызовом функции, ее лучше конечно сохранить в переменную с понятным именем. Иначе этот кусок
        #  кода становится очень крутые, но малопонятным сходу.
        draw_function = dict_of_figure[global_color]['draw']
        draw_function(start_point=start_point)
        break
    else:
        print('Вы ввели некорретный номер!')

sd.pause()

# TODO: Сделал пока так, но не понятно, фигура должна быть строго в центре экрана?
#  из-за того. что указываем точку старта отрисовки, происход некоторый перекос.

# TODO: Ответ. Можно оставить так, если не очень любите геометрию) Если интерес есть, можете посчитать центр фигуры
#  (программно разумеется). Мне кажется самый простой способ: определить в какую окружность может быть списана фигура
#  использовать радиус это фигуры в качестве отступов по осям X, Y