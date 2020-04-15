# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowfall.snowflake_dict_gen(N=10, min_branch_len=15, max_branch_len=30)
print(snowfall.snowflake_dict)
while not sd.user_want_exit():
    snowfall.draw_snowflakes(color=sd.background_color)
    snowfall.move_snowflakes()
    snowfall.draw_snowflakes(color=sd.COLOR_RED)
    print(snowfall.get_fallen_snowflakes())

    # TODO: ф-ция должна вызывать 1 раз, результат ее работы сохраняться и дальше мы будем работать уже с этим
    #  результатом
    if snowfall.get_fallen_snowflakes() is not None:
        snowfall.snowflake_dict.pop(snowfall.get_fallen_snowflakes())
        snowfall.snowflake_dict.append(snowfall.get_snowflake(branch_min=15,
                                                              branch_max=30,
                                                              y_min=sd.resolution[1]))
    sd.sleep(0.1)

sd.pause()
