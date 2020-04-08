# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from epic_painting.rainbow import draw_rainbow
from epic_painting.smile import draw_smile
from epic_painting.snow import snowfall
from epic_painting.snow import snowflake_dict_gen
from epic_painting.house import build_wall
from epic_painting.house import build_roof
from epic_painting.wood import draw_random_branches

sd.resolution = (1000, 400)

# Растим деревья
forest = []
for _ in range(3):
    forest.append({
        'angle': sd.random_number(80, 100),
        'length': sd.random_number(25, 55),
        'x': sd.random_number(795, 900),
        'y': sd.random_number(15, 20)
    })
for _, wood in enumerate(forest):
    print(wood)
    root_point = sd.get_point(wood['x'], wood['y'])
    draw_random_branches(start_point=root_point, angle=wood['angle'], length=wood['length'])

# Травка
sd.rectangle(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 20), sd.COLOR_DARK_GREEN)

# Радуга
draw_rainbow(320, -170, 700)

# Человечек
draw_smile(450, 150, sd.COLOR_YELLOW)
sd.line(sd.get_point(450, 100), sd.get_point(450, 50))
sd.line(sd.get_point(450, 50), sd.get_point(420, 20))  # Ноги
sd.line(sd.get_point(450, 50), sd.get_point(480, 20))
sd.line(sd.get_point(450, 80), sd.get_point(420, 90))  # Руки
sd.line(sd.get_point(450, 80), sd.get_point(480, 90))

# Строим стену и крышку
sd.rectangle(sd.get_point(600, 20), sd.get_point(770, 110), color=sd.COLOR_RED)
build_wall(left_bottom=(600, 20), right_top=(750, 100), color=sd.COLOR_DARK_RED)
for roof_length in range(230):
    build_roof(sd.get_point(570, 110), length=roof_length, angle=0, width=2)

# Делаем список стартовых снежинок
snowflake_dict = snowflake_dict_gen(left_bottom=(0, 20), right_top=(300, 100))

SUN_RADIUS_MAX = 50  # Радиус солнышка
animate_angle = 0  # Угол для анимации

while not sd.user_want_exit():

    for angle in range(0, 361, 60):
        angle += animate_angle
        sd.vector(start=sd.get_point(100, 300), angle=angle, width=8, length=80, color=sd.background_color)
        sd.circle(sd.get_point(100, 300), radius=50, width=50)
        # TODO: Есть лаг с миганием солнышка. Пока не нашел как устранить( Наименьшие баги когда добавил отрисовку
        #  солнышка в цикл
        #  Также пока не реализовал мигание смайлика, переливание радуги. Сделаю во второй иттерации :D

    animate_angle += 10
    for angle in range(0, 361, 60):
        angle += animate_angle
        sd.vector(start=sd.get_point(100, 300), angle=angle, width=8, length=80)

    sd.start_drawing()
    snowfall(snowflake_params=snowflake_dict, left_bottom=(0, 20), right_top=(300, 100))
    sd.finish_drawing()
    sd.sleep(0.1)

sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
