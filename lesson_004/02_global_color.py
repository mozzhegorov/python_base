# -*- coding: utf-8 -*-
# from curses.ascii import isdigit

import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


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


# TODO: идея хорошая. Давайте улучшим: сейчас у нас словарь, который в качестве значений имеет списки. И чтобы достать
#  значение 1го цвета на нужно выполнить:
#           dict_of_colors['0'][1]    # трудно догадаться, что мы тут вытащили. Это сам цвет.
#           dict_of_colors['0'][0]    # а это имя цвета
#  .
#  Можно сделать список, который будет хранить словари. При этом каждый словарь будет иметь 2 ключа: color_name и color.
#  .
#  Слова "каждый словарь будет иметь 2 ключа: color_name и color" - имеют решающее значения.
#  У нас может быть список из 7 словарей (по числу цветов), и каждый из словарей имеет ровно 2 ключа:
#  'color_name' - выдает имя цвета и 'color' - выдает объект. Пример использования:
#      all_color[0]['color_name']       # выдаст имя 1го цвета
#      all_color[1]['color_name']       # имя 2го цвета
#      all_color[1]['color']            # сам 2ой цвет
dict_of_colors = {
    '0':
        {'color_name': 'red', 'color': sd.COLOR_RED},
    '1':
        {'color_name': 'orange', 'color': sd.COLOR_ORANGE},
    '2':
        {'color_name': 'yellow', 'color': sd.COLOR_YELLOW},
    '3':
        {'color_name': 'green', 'color': sd.COLOR_GREEN},
    '4':
        {'color_name': 'cyan', 'color': sd.COLOR_CYAN},
    '5':
        {'color_name': 'blue', 'color': sd.COLOR_BLUE},
    '6':
        {'color_name': 'purple', 'color': sd.COLOR_PURPLE},
}

print('Возможные цвета')
for number, color_info in dict_of_colors.items():  # в задаче про радугу я упоминал enumerate().
    print(number, ': ', color_info['color_name'])

#  выше вы сможете использовать "enumerate()", если сделаете замену "словарь списков" на "список словарей". Пример:
#       seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#       for season_id, season_name in enumerate(seasons):
# 	        print(season_id, ' - ', season_name)
#   .
#   В результате будет выведено:
#       0 - 'Spring'
#       1 - 'Summer'
#       2 - 'Fall'
#       3 - 'Winter'
#   .
#   TODO: Надо стараться не спользовать "for i in range(len(...))".
#     Хорошо, я передалал, но я же не использовал range() =((


while True:
    global_color = input('Выберите желаемый цвет > ')
    # print(isdigit(global_color))
    if 0 < int(global_color) < len(dict_of_colors):
        break
    else:
        print('Вы ввели некорретный номер!')

draw_triangle(color=dict_of_colors[global_color]['color'])
draw_square(color=dict_of_colors[global_color]['color'])
draw_pentagon(color=dict_of_colors[global_color]['color'])
draw_hexagon(color=dict_of_colors[global_color]['color'])

sd.pause()

# TODO: нужны функции с общей частью.
#  Задача может быть зачтена только с функциями из 2ой части 1ой задачи. Т.е. сначала лучше добить 1ую задачу.
