# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 50

snowflake_params = []
# "i" можно заменить на "_", чтобы подчеркнуть, что переменная не используется. "_"
for _ in range(N):
    snowflake_params.append({'branch_len': sd.random_number(10, 100),  # Раздаем длины лучей,
                             'x': sd.random_number(0, sd.resolution[0]),  # а также положения по оси У
                             'y': sd.random_number(0, sd.resolution[1]),
                             'moving': 1})  # флаг активности
    # ееее, вот это круто: прям внтури генерируется словарь. Отлично, хороший программист сделал бы так же

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
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])
        # передвигаем и прячем снежинку только если снежинка имеет флаг активности
        if param_of_snowflake['moving'] == 1:
            if param_of_snowflake['y'] > speed:
                sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.background_color)
                param_of_snowflake['y'] -= speed
                param_of_snowflake['x'] += sd.random_number(-5, 5)
            else:
                # Добавляем еще одну снежинку на верх
                snowflake_params.append({'branch_len': sd.random_number(10, 100),  # Раздаем длины лучей,
                                         'x': sd.random_number(0, sd.resolution[0]),  # а также положения по оси У
                                         'y': sd.resolution[1],
                                         'moving': 1})  # флаг активности
                # Убираем активность у старой снежинки
                param_of_snowflake['moving'] = 0

    for param_of_snowflake in snowflake_params:
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])

        # TODO: цикл покраски снежинок в белый лучше вынести в отдельный цикл. Т.е. сначала все прячем+перемещаем.
        #  Потому у нас пустой экран. Потом красим белым.
        #  Зачем?
        #  Обратите внимание, что при пересечении снежинок у нас сейчас возникает перетирание веточек.
        #  Ответ: Не смог придумать ничего лучше как использовать перемнную активности для снежинки.
        #  В данном варианте решения добавляем еще одно снежинку и с ней работаем. Раньше снежинок было фиксированное
        #  количество, лишь менялись координаты, а старая (та что внизу) не перетиралась сама собой, но был баг.
        #  Теперь бага нет
        # красим белым весь список снежинок, даже не активные
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
