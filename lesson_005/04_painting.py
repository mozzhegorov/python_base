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
from epic_painting.house import build_window
from epic_painting.wood import draw_random_branches

sd.resolution = (1000, 400)

# Растим деревья
#  после отрисовки, деревья не перерисовываются. Может мы тогда сделаем 1 обезличенных цикл, который нарисует N
#  деревьев? Тогда нам не придется хранить список всех деревьев в течении всего времени работы
wood = {
    'angle': 0,
    'length': 0,
    'x': 0,
    'y': 0
}
for _ in range(3):
    # TODO: может просто сгенерируем переменные x,y, и т.п. и обойдемся без словаря wood?
    wood['x'] = sd.random_number(795, 900)
    wood['y'] = sd.random_number(15, 20)
    wood['length'] = sd.random_number(25, 55)
    wood['angle'] = sd.random_number(80, 100)
    root_point = sd.get_point(wood['x'], wood['y'])
    draw_random_branches(start_point=root_point, angle=wood['angle'], length=wood['length'])
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

# Строим стену и крышку
sd.rectangle(sd.get_point(600, 20), sd.get_point(770, 110), color=sd.COLOR_RED)
build_wall(left_bottom=(600, 20), right_top=(750, 100), color=sd.COLOR_DARK_RED)
#  Сделайте так, чтобы у нас вызывалась ф-ция "нарисовать крышу" 1 раз и он рисовала крышу.
#  .
#  p.s. чтобы нарисовать закрашенный треугольник укажите width=0
# TODO: перенесли цикл внутрь - хорошо. Про "width=0" - ступил. Это же не родной треугольник, а наш собственный.
#  У методов библиотеки задание width=0 приводит к заливки фигуры одним цветом. К сожаление, треугольника в их числе
#  нет.
build_roof(sd.get_point(570, 110), length=230)

# Рисуем окно
build_window((650, 50), (720, 80))

# Делаем список стартовых снежинок
FLAKES_NUMBER = 50
snowflake_dict = snowflake_dict_gen(N=FLAKES_NUMBER, left_bottom=(0, 20), right_top=(300, 100))

SUN_RADIUS_MAX = 50  # Радиус солнышка
animate = 0  # Угол для анимации

while not sd.user_want_exit():
    sd.start_drawing()

    # TODO: все что касается солнышка - вынести в отдельный модуль sun.py. Сделать в нем метод draw_sun.
    #  Мы инкапсулируем внутрь ф-ции. Тогда здесь код будет состоять только из вызовов этих ф-ций.
    # Рсиуем кружок цветом фона и потом рисуем солнышко :)
    sd.circle(sd.get_point(100, 300), radius=85, width=50, color=sd.background_color)
    sd.circle(sd.get_point(100, 300), radius=50, width=50)

    #  а это что?)
    #  Для анимации солнышка :)
    # Крутим лучиками
    animate += 1
    for angle in range(0, 361, 60):
        angle += animate * 5
        sd.vector(start=sd.get_point(100, 300), angle=angle, width=8, length=80)

    # Радуга
    draw_rainbow(320, -170, 700, animate)

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
