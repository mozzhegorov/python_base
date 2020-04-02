# -*- coding: utf-8 -*-
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
        ['red', sd.COLOR_RED],
    '1':
        ['orange', sd.COLOR_ORANGE],
    '2':
        ['yellow', sd.COLOR_YELLOW],
    '3':
        ['green', sd.COLOR_GREEN],
    '4':
        ['cyan', sd.COLOR_CYAN],
    '5':
        ['blue', sd.COLOR_BLUE],
    '6':
        ['purple', sd.COLOR_PURPLE],
}

print('Возможные цвета')
for number, color_info in dict_of_colors.items():       # TODO: в задаче про радугу я упоминал enumerate().
    print(f'{number}: {color_info[0]}')

# TODO: выше вы сможете использовать "enumerate()", если сделаете замену "словарь списков" на "список словарей". Пример:
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
#   Надо стараться не спользовать "for i in range(len(...))".


while True:
    global_color = input('Выберите желаемый цвет > ')

    # TODO: добавьте проверку, что нам точно передали число. Используйте isdigit()

    if 0 < int(global_color) < 7:   # TODO: что будет если мы добавим цвет в список? придется менять. Используйте len()
        break
    else:
        print('Вы ввели некорретный номер!')

draw_triangle(color=dict_of_colors[global_color][1])
draw_square(color=dict_of_colors[global_color][1])
draw_pentagon(color=dict_of_colors[global_color][1])
draw_hexagon(color=dict_of_colors[global_color][1])

sd.pause()

# TODO: нужны функции с общей частью.
#  Задача может быть зачтена только с функциями из 2ой части 1ой задачи. Т.е. сначала лучше добить 1ую задачу.
