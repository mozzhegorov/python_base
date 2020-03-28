#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

lnth = violator_songs_list[5][1] + violator_songs_list[3][1] + violator_songs_list[-1][1]

# TODO: использовать round() вместо __round__()
print(f'Три песни звучат {lnth.__round__(2)} мин.')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут


lnth = violator_songs_dict["Sweetest Perfection"] + violator_songs_dict["Policy of Truth"] + violator_songs_dict["Blue Dress"]

#  ошибка в формате вывода.
#  'Время звучания "Sweetest Perfection", "Policy of Truth" и "Blue Dress" =  ХХХ мин.' - должно быть
#  'Время звучания "Sweetest Perfection", "Policy of Truth" и "Blue Dress" =  ХХХ.xx мин.' - выводит код
#  .
#  Примеры округлений:
#       pi = 3.1415
#       round(pi, 2)        # 3.14
#       round(pi, 0)        # 3.0
#       round(pi)           # 3
#       Студент: СДЕЛАНО!
print('Время звучания "Sweetest Perfection", "Policy of Truth" и "Blue Dress" = ', round(lnth), ' мин.')

lnth = violator_songs_dict["World in My Eyes"] + violator_songs_dict["Clean"] \
       + violator_songs_dict["Halo"] + violator_songs_dict["Personal Jesus"] + \
       + violator_songs_dict["Waiting for the Night"] + violator_songs_dict["Enjoy the Silence"]

print('А другие песни звучат ', round(lnth), ' мин.')

# зачет!