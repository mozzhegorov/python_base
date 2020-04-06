# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

snowflake_params = []

for i in range(N):
    snowflake_params.append({'branch_len': sd.random_number(10, 100),  # Раздаем длины лучей,
                             'x': sd.random_number(0, sd.resolution[0]),  # а также положения по оси У
                             'y': sd.random_number(0, sd.resolution[1])})  # и положения по оси X

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


y = sd.resolution[1]  # все снежинки поднимаем на верх
speed = 10

while not sd.user_want_exit():
    sd.start_drawing()

    #  Ни range(len(...)), ни enumerate(...) здесь не нужны. Мы можем использовать простой "цикл for". Пример:
    #           data = [{'numb': 100}, {'numb': 200}]
    #  .
    #           for index in range(len(data)):          # было
    #               print(data[index]['numb'])
    #  .
    #           for elem in data:                       # стало
    #               print(elem['numb'])
    #  .
    for param_of_snowflake in snowflake_params:
        # прячем снежинку
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])

        # передвигаем

        if param_of_snowflake['y'] > speed:
            sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.background_color)
            param_of_snowflake['y'] -= speed
            param_of_snowflake['x'] += sd.random_number(-5, 5)
        else:   # Добавляем снежинку с новыми параметрами
            param_of_snowflake['y'] = sd.resolution[1]
            param_of_snowflake['x'] = sd.random_number(0, sd.resolution[0])
            param_of_snowflake['branch_len'] = sd.random_number(10, 100)

        # красим белым
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])
        sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.COLOR_WHITE)

        #  добавить "упавшие снежинки возвращать назад"
    sd.finish_drawing()
    sd.sleep(0.1)

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
