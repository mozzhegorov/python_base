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
    snowflake_params.append([sd.random_number(10, 100), sd.random_number(0, sd.resolution[0])]) # Раздаем длины
    # лучей, а также положения по оси У


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


y = sd.resolution[1]    # все снежинки поднимаем на верх
speed = 5

while True:
    sd.start_drawing()
    for i in range(N):
        snowflake_center = sd.get_point(snowflake_params[i][1], y + speed)
        sd.snowflake(snowflake_center, snowflake_params[i][0], color=sd.background_color)
        snowflake_params[i][1] += sd.random_number(-5, 5)
        snowflake_center = sd.get_point(snowflake_params[i][1], y)
        sd.snowflake(snowflake_center, snowflake_params[i][0], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    y -= speed
    sd.sleep(0.1)
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


