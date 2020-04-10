# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 50


# TODO: пусть ф-ция возращает снежинку, а не добавляется в список.
#  Вместе snow_append будет get_snowflake.
def snow_append(_snowflake_params, branch_min=10, branch_max=100, y_min=0, y_max=sd.resolution[1], x_min=0,
                x_max=sd.resolution[0]):
    _snowflake_params.append({'branch_len': sd.random_number(branch_min, branch_max),  # Раздаем длины лучей,
                              'x': sd.random_number(x_min, x_max),  # а также положения по оси У
                              'y': sd.random_number(y_min, y_max),
                              'moving': 1})  # флаг активности


snowflake_params = []
# "i" можно заменить на "_", чтобы подчеркнуть, что переменная не используется. "_"
for _ in range(N):
    snow_append(_snowflake_params=snowflake_params)
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
                #  сделайте ф-цию. "вернуть снежинку", которая можно будет вызывать здесь и на 17ой строке,
                #  чтобы у нас не было дублирования кода.
                snow_append(_snowflake_params=snowflake_params, y_min=sd.resolution[1])
                # Убираем активность у старой снежинки
                param_of_snowflake['moving'] = 0

    for param_of_snowflake in snowflake_params:
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])

        #  цикл покраски снежинок в белый лучше вынести в отдельный цикл. Т.е. сначала все прячем+перемещаем.
        #  Потому у нас пустой экран. Потом красим белым.
        #  Зачем?
        #  Обратите внимание, что при пересечении снежинок у нас сейчас возникает перетирание веточек.
        #  Ответ: Не смог придумать ничего лучше как использовать перемнную активности для снежинки.
        #  В данном варианте решения добавляем еще одно снежинку и с ней работаем. Раньше снежинок было фиксированное
        #  количество, лишь менялись координаты, а старая (та что внизу) не перетиралась сама собой, но был баг.
        #  Теперь бага нет

        #  Ответ.
        #  Мой косяк, нужно было еще точнее формулировать. Речь шла только о падающих снежинках. Сугробу почти не помочь
        #  Текущий вариант "спасает" сугроб, но нужны доп.меры. Нужно добавить проверку, что число снежинок не превысило
        #  N * 5. И если превысило, то при добавлении новой снежинки (крайней), удалять самую старую (первую).
        # красим белым весь список снежинок, даже не активные

        sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.COLOR_WHITE)
        # print(len(snowflake_params))
        # TODO:
        #  "len(snowflake_params) > 5 * N_init" - это условие
        #  snowflake_params.pop(0) - это действие.
        #  .
        #  Давайте сделаем из этого if-блок.
        can_i_del = len(snowflake_params) > 5 * N  # Проверяем сколько элеметнов там у нас
        # print(can_i_del)
        can_i_del and snowflake_params.pop(0)       # TODO: рабочая, но не очевидная запись. Повышает сложность чтение
        # Нашел такой крутой способ условия. В общем он удаляет первый
        # элемент. Вроде работает

        # TODO: еще удалить законменченный код и лишние комментарии и TODО

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
