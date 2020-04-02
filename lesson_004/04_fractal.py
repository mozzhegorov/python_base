# -*- coding: utf-8 -*-
import random
# TODO: Библиотека выше не используется.

import simple_draw as sd

sd.resolution = (600, 400)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(start_point, angle=90, length=100):
    if length < 10:
        return
    # TODO: Очень важно соблюдать стили имен переменных/констант/классов/модулей/исключений.
    #  .
    #  I. Переменные.
    #  Имя должно отражаться суть того, что хранит переменная. Имена написаны исключительно строчными (маленькими) буквами.
    #  Имя переменной может состоять максимум из 3-4 слов, в таком случае слова разделяются символом "_".
    #   Правильно:      user_input, months_31_days, sorted_dict, point_2;
    #   Не правильно:   userinput, userInput, UserInput, USERINPUT, Userinput, point2       (не верный стиль);
    #                   my_var, my_lst, point_13, point_15, thing, peremennay               (не понятно что хранит).
    v2 = sd.vector(start_point, angle + 30, length)
    v3 = sd.vector(start_point, angle - 30, length)         # TODO: вот это видимо right_branch
    length *= .75
    angle += 30
    draw_branches(v2, angle=angle, length=length)
    angle -= 60
    draw_branches(v3, angle=angle, length=length)


# root_point = sd.get_point(sd.resolution[0] // 2, 0)
# draw_branches(root_point)

root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
# TODO: не столь красиво конечно вышло со вторым вариантом..
def draw_random_branches(start_point, angle=90, length=100):
    if length < 10:
        return
    # TODO: Это видимо левая ветка.
    random_angle = sd.random_number(60, 140) / 100 * 30     # TODO: а это видимо дельта для угла левой ветки. Может весь угол сразу считать?
    random_length = sd.random_number(80, 120) / 100
    v2 = sd.vector(start_point, angle + random_angle, length * random_length)       # TODO: чтобы тут не суммировать дельту и угол

    random_angle = sd.random_number(60, 140) / 100 * 30
    random_length = sd.random_number(80, 120) / 100
    v3 = sd.vector(start_point, angle - random_angle, length * random_length)

    # TODO: рандомную длину перетерли! Для левой ветки передастся длина правой ветки.
    length *= sd.random_number(80, 120) / 100 * .75
    # TODO: так может просто передадим "angle + random_angle", "angle - random_angle"? (лучше бы рандомный угол сразу считать, без дельты)
    angle += sd.random_number(60, 140) / 100 * 30

    draw_branches(v2, angle=angle, length=length)
    angle -= sd.random_number(60, 140) / 100 * 60
    draw_branches(v3, angle=angle, length=length)


# Пригодятся функции
# sd.random_number()
root_point = sd.get_point(300, 30)
draw_random_branches(start_point=root_point, angle=90, length=100)

sd.pause()

# TODO: корень деревьям еще нарисуйте пожалуйста. Алгоритм лучше будет смотреться, если вызов ф-ции рисует 1 палочку,
#  и вызывает 2 версии себя ну и т.д.