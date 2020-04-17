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

snowfall.snowflake_list_gen(N=30, min_branch_len=15, max_branch_len=30)
while not sd.user_want_exit():
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snowfall.draw_snowflakes(color=sd.background_color)
    #  сдвинуть_снежинки()
    snowfall.move_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    snowfall.draw_snowflakes(color=sd.COLOR_RED)

    fallen_snowflakes = snowfall.get_fallen_snowflakes()
    #  если есть номера_достигших_низа_экрана() то
    # TODO: условие грамотно упростили. Молодец.
    if fallen_snowflakes:
        # TODO: Поменял оередность созадния/удаления, критично ли? в функции удаления снежинки чиститится список с
        #  упавшими снежинками. Их количество использую в функции создания снежинок.

        # TODO: Шутите?)) Вы же сейчас удаление сделали с конца! А добавление снежинок куда идет?
        # создать_снежинки(count)
        snowfall.snowflake_list_gen(N=len(fallen_snowflakes),
                                    left_bottom=(0, sd.resolution[1]))
        # удалить_снежинки(номера)
        snowfall.delete_snowflake() # TODO: функция должна принимать параметр - список упаших

    sd.sleep(0.1)

sd.pause()