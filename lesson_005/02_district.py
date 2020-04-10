# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# дайте псевдонимы для каждого модуля, слишком длинный путь, чтобы просто так использовать.
import district.central_street.house1.room1 as central_h1_r1       # пример
import district.central_street.house1.room2 as central_h1_r2
import district.central_street.house2.room1 as central_h2_r1
import district.central_street.house2.room2 as central_h2_r2
import district.soviet_street.house1.room1 as soviet_h1_r1
import district.soviet_street.house1.room2 as soviet_h1_r2
import district.soviet_street.house2.room1 as soviet_h2_r1
import district.soviet_street.house2.room2 as soviet_h2_r2

area = {
    'central_street': {
        'house1': {
            'room1': central_h1_r1.folks,
            'room2': central_h1_r2.folks
        },
        'house2': {
            'room1': central_h2_r1.folks,
            'room2': central_h2_r2.folks
        }
    },
    'soviet_street': {
        'house1': {
            'room1': soviet_h1_r1.folks,
            'room2': soviet_h1_r2.folks
        },
        'house2': {
            'room1': soviet_h2_r1.folks,
            'room2': soviet_h2_r2.folks
        }
    },
}

# было бы достаточно врунчую сложить все списки, не создавая цикл и словарь.
all_folks = []

for street_name, street in area.items():
    for house_name, house in street.items():
        for room_name, room in house.items():
            all_folks.extend(area[street_name][house_name][room_name])

# на 4ой строке указан формат вывода.
print('На районе живут', ', '.join(all_folks))

# зачет!