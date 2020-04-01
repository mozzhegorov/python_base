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
for number, color_info in dict_of_colors.items():
    print(f'{number}: {color_info[0]}')

while True:
    global_color = input('Выберите желаемый цвет > ')
    if 0 < int(global_color) < 6:
        break
    else:
        print('Вы ввели некорретный номер!')

draw_triangle(color=dict_of_colors[global_color][1])
draw_square(color=dict_of_colors[global_color][1])
draw_pentagon(color=dict_of_colors[global_color][1])
draw_hexagon(color=dict_of_colors[global_color][1])

sd.pause()
