# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


list_of_figure = [
    {'shape_name': 'треугольник', 'draw': draw_triangle},
    {'shape_name': 'квадрат', 'draw': draw_square},
    {'shape_name': 'пятиугольник', 'draw': draw_pentagon},
    {'shape_name': 'шестиугольник', 'draw': draw_hexagon}
]

print('Возможные фигуры')
for number, figure_info in enumerate(list_of_figure):
    print(number, ': ', figure_info['shape_name'])

while True:
    global_shape = input('Какую фигуру рисуем > ')

    if global_shape.isdecimal() and 0 <= int(global_shape) < len(list_of_figure):
        init_point = sd.get_point(sd.resolution[0] // 2, sd.resolution[1] // 2)
        #  перед вызовом функции, ее лучше конечно сохранить в переменную с понятным именем. Иначе этот кусок
        #  кода становится очень крутые, но малопонятным сходу.
        global_color = int(global_shape)
        draw_function = list_of_figure[global_color]['draw']
        draw_function(start_point=init_point)
        break
    else:
        print('Вы ввели некорретный номер!')

sd.pause()

#  Сделал пока так, но не понятно, фигура должна быть строго в центре экрана?
#  из-за того. что указываем точку старта отрисовки, происход некоторый перекос.

#  Ответ. Можно оставить так, если не очень любите геометрию) Если интерес есть, можете посчитать центр фигуры
#  (программно разумеется). Мне кажется самый простой способ: определить в какую окружность может быть списана фигура
#  использовать радиус это фигуры в качестве отступов по осям X, Y
#  Ответ: Вспомнил радиусы окружностей, всплакнув :( для каждой фигуры расчет свой, в пятиугольнике участвует синус.
#  Оставлю так.

# зачет!