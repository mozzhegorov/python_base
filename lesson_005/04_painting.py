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
from epic_painting.smile import draw_eyes
from epic_painting.snow import snowfall
from epic_painting.snow import snowflake_dict_gen
from epic_painting.house import build_wall
from epic_painting.house import build_roof
from epic_painting.house import build_window
from epic_painting.wood import draw_random_branches
from epic_painting.sun import draw_animate_sun

FLAKES_NUMBER = 50  # Количество снежинок
SUN_RADIUS_MAX = 50  # Радиус солнышка

sd.resolution = (1000, 400)

# Растим деревья
#  после отрисовки, деревья не перерисовываются. Может мы тогда сделаем 1 обезличенных цикл, который нарисует N
#  деревьев? Тогда нам не придется хранить список всех деревьев в течении всего времени работы

# Рисуем деревья
for _ in range(3):
    root_point = sd.get_point(sd.random_number(795, 900), sd.random_number(15, 20))
    draw_random_branches(start_point=root_point,
                         angle=sd.random_number(80, 100),
                         length=sd.random_number(25, 55))
    sd.random_point()

# Травка
sd.rectangle(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 20), sd.COLOR_DARK_GREEN)

# Человечек
draw_smile(450, 150, sd.COLOR_YELLOW)
sd.line(sd.get_point(450, 100), sd.get_point(450, 50))
sd.line(sd.get_point(450, 50), sd.get_point(420, 20))  # Ноги
sd.line(sd.get_point(450, 50), sd.get_point(480, 20))
sd.line(sd.get_point(450, 80), sd.get_point(420, 90))  # Руки
sd.line(sd.get_point(450, 80), sd.get_point(480, 90))

# Строим стену, крышу, окно
sd.rectangle(sd.get_point(600, 20), sd.get_point(770, 110), color=sd.COLOR_RED)
build_wall(left_bottom=(600, 20), right_top=(750, 100), color=sd.COLOR_DARK_RED)
build_roof(sd.get_point(570, 110), length=230)
build_window((650, 50), (720, 80))

# Делаем список стартовых снежинок
snowflake_dict = snowflake_dict_gen(N=FLAKES_NUMBER, left_bottom=(0, 20), right_top=(300, 100))

animate = 0  # Угол для анимации
animate_rainbow = 0
#  как сделать так, чтобы счетчик не уходил в бесконечность?
#  Можно ограничить положение счетчика каким-то числом, кратным 7 (чтобы радуга переключалась плавно).
#  Для солнца кратность не играет роли. Для смайлика тоже.
#  .
#  Переполнение счетчика произойти не может, но если позволить программе работать лет 100 (с учетом что sleep(0.1))
#  счетчик будет требовать памяти чуть больше обычного. Мелочь, но если sleep`а не будет вовсе, то за пару часов он
#  достигнет тех же значений, а за месяц может создать проблемы.
#  .
#  Поэтому такой случай лучше учесть, и не оставлять не обработанным.
while not sd.user_want_exit():
    sd.start_drawing()

    # Моргаем глазками
    draw_eyes(450, 150, sd.COLOR_YELLOW, animate)

    # Крутим солнышко
    animate += 1
    animate %= 360
    draw_animate_sun(shift_angle=animate,
                     x_center=100,
                     y_center=300)

    # Радуга
    animate_rainbow += 1
    animate_rainbow %= 7
    draw_rainbow(320, -170, 700, animate_rainbow)

    # Работаем со снегом
    snowfall(N_init=FLAKES_NUMBER, snowflake_params=snowflake_dict, left_bottom=(0, 20), right_top=(300, 100))

    sd.finish_drawing()
    sd.sleep(0.1)

sd.pause()

#  если смайлик вышел на улицу - пусть. Но окно в доме долнжо остаться

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
