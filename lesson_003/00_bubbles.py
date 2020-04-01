# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 450)

radius = 50
for num_of_circle in range(3):
    radius = radius + 5
    sd.circle(point, radius, sd.COLOR_RED, 1)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
#     начиная с 3го модуля мы стремимся соблюдать PEP8.
#     Перемеинуйте функцию bubble в слово/словосочетание, глагол, чтобы он отражал суть - "нарисовать пузырек".
#     Функции и методы должны носить название-глаголы. А объекты - название-существительные. И bubble как раз больше
#     похож на существительное.
def draw_bubble(center_point, radius_step, color=sd.COLOR_RED):
    # TODO: просто интересно, а почему "_fun"?
    #  Ответ: локальная переменная, fun - сокращенное от function. Про "_" Вадим только в следующем модуле рассказал
    # TODO: Ответ. Ясно. Давайте уберем этот суффикс, пусть останется только "radius".
    #  Почему?
    #  Потому что такой суффикс обычно имеют именно ф-ции. А еще ф-ции можно хранится так, как и переменные, в списках
    #  или словарях. В 4ом модуле у нас будет словарь из ф-ции, и мы будем вызывать их по очереди в цикле.
    radius_fun = 30
    #  если переменная не используется (как "num_of_circle_fun"), то ее можно заменить на "_", это подчеркивает
    #  что данная переменная не важна.
    for radius_fun in range(radius_fun, radius_fun + 3 * radius_step, radius_step):  # сможете сделать так, чтобы цикл
        # выдавал значения радиуса?
        sd.circle(center_point, radius_fun, color, 1)


draw_bubble(sd.get_point(500, 500), 7, sd.COLOR_CYAN)

# Нарисовать 10 пузырьков в ряд
for bubble_coord_x in range(100, 1001, 100):
    draw_bubble(sd.get_point(bubble_coord_x, 100), 4)

# Нарисовать три ряда по 10 пузырьков
for bubble_coord_y in range(100, 301, 100):
    for bubble_coord_x in range(100, 1001, 100):
        draw_bubble(sd.get_point(bubble_coord_x, bubble_coord_y), 4)        # TODO: пожалуйста
                                                                            #  дайте им какой-нибудь цвет, чтобы я убедился,
                                                                            #  что дефолтное значение color - это не просто лазейка))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    # для генерации рандоного цвета используйте sd.random_color()
    # подставлять "голую" цифры 4 - не очень стиль. Лучше добавить: bubble(..., radius_step=4, ...)
    draw_bubble(sd.random_point(), radius_step=4, color=sd.random_color())

sd.pause()
