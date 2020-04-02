# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
# TODO: вот тут нам будет ооочень удобен список словарей, вместо списка списков.
#  Мы будем часто обращаться к полям, и куда легче понять поле snowflake_params[0]['x'] (и то, [0] не будет)
snowflake_params = []

for i in range(N):
    # TODO: Добавьте помимо x, length еще 'y'
    snowflake_params.append([sd.random_number(10, 100), sd.random_number(0, sd.resolution[0])]) # Раздаем длины
    # лучей, а также положения по оси У


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# TODO: у каждой снежинки должен быть свой 'y'
y = sd.resolution[1]    # все снежинки поднимаем на верх
speed = 5

while True:
    sd.start_drawing()

    # TODO: Ни range(len(...)), ни enumerate(...) здесь не нужны. Мы можем использовать простой "цикл for". Пример:
    #           data = [{'numb': 100}, {'numb': 200}]
    #  .
    #           for index in range(len(data)):          # было
    #               print(data[index]['numb'])
    #  .
    #           for elem in data:                       # стало
    #               print(elem['numb'])
    #  .
    for i in range(N):
        # прячем снежинку
        snowflake_center = sd.get_point(snowflake_params[i][1], y + speed)
        sd.snowflake(snowflake_center, snowflake_params[i][0], color=sd.background_color)

        # передвигаем
        snowflake_params[i][1] += sd.random_number(-5, 5)
        # TODO: добавить y

        # красим белым
        snowflake_center = sd.get_point(snowflake_params[i][1], y)
        sd.snowflake(snowflake_center, snowflake_params[i][0], color=sd.COLOR_WHITE)

        # TODO: добавить "упавшие снежинки возвращать назад"
    sd.finish_drawing()
    y -= speed
    sd.sleep(0.1)

    # TODO: можно перенести условие вместо True в while.
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


