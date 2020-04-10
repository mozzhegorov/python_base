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
    sd.line(start_point, rib_end, width=1, color=color)


def draw_triangle(start_point=sd.get_point(100, 100), angle=0, length=50, color=sd.COLOR_YELLOW):
    draw_figure(3, start_point, angle=angle, length=length, color=color)


def draw_square(start_point=sd.get_point(100, 400), angle=0, length=50, color=sd.COLOR_YELLOW):
    draw_figure(4, start_point, angle=angle, length=length, color=color)


def draw_pentagon(start_point=sd.get_point(400, 100), angle=0, length=50, color=sd.COLOR_YELLOW):
    draw_figure(5, start_point, angle=angle, length=length, color=color)


def draw_hexagon(start_point=sd.get_point(400, 400), angle=0, length=50, color=sd.COLOR_YELLOW):
    draw_figure(6, start_point, angle=angle, length=length, color=color)

#  идея хорошая. Давайте улучшим: сейчас у нас словарь, который в качестве значений имеет списки. И чтобы достать
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
list_of_colors = [
        {'color_name': 'red', 'color': sd.COLOR_RED},
        {'color_name': 'orange', 'color': sd.COLOR_ORANGE},
        {'color_name': 'yellow', 'color': sd.COLOR_YELLOW},
        {'color_name': 'green', 'color': sd.COLOR_GREEN},
        {'color_name': 'cyan', 'color': sd.COLOR_CYAN},
        {'color_name': 'blue', 'color': sd.COLOR_BLUE},
        {'color_name': 'purple', 'color': sd.COLOR_PURPLE},
]

#  знаете почему использовать список словарей удобнее, чем самому расставляь ключи в словаре словарей?
#  Удалите пожалуйста зеленый цвет из списка, при этом номера цветов изменяться, но порядок не должен (т.е. взять и
#  перенести цвет с конца в середину нельзя).
#  .
#  Сделайте это удаление.
#   Ответ: Я понял, тупанул ( не знаю зачем решил делать словарь словарей

print('Возможные цвета')
for number, color_info in enumerate(list_of_colors):  # в задаче про радугу я упоминал enumerate().
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
#    Надо стараться не спользовать "for i in range(len(...))".
#     Хорошо, я передалал, но я же не использовал range() =((
    # Ответ. Это предупреждение в общем плане (вы так не делали)


while True:
    global_color = input('Выберите желаемый цвет > ')
    #  здесь мы все равно проверяем "а число ли это" и "лежит ли число в диапазоне".
    #  Так зачем же нам словарь из словарей? Чем он удобнее списка словарей?

    #  Отлично сделано - компактно и понятно.
    if global_color.isdecimal() and 0 <= int(global_color) < len(list_of_colors):
        global_color = int(global_color)
        break
    else:
        print('Вы ввели некорретный номер!')

draw_triangle(color=list_of_colors[global_color]['color'])
draw_square(color=list_of_colors[global_color]['color'])
draw_pentagon(color=list_of_colors[global_color]['color'])
draw_hexagon(color=list_of_colors[global_color]['color'])

sd.pause()

#  нужны функции с общей частью.
#  Задача может быть зачтена только с функциями из 2ой части 1ой задачи. Т.е. сначала лучше добить 1ую задачу.

# зачет!