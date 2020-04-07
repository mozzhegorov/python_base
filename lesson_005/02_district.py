# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
import district.central_street.house1.room1
import district.central_street.house1.room2
import district.central_street.house2.room1
import district.central_street.house2.room2
import district.soviet_street.house1.room1
import district.soviet_street.house1.room2
import district.soviet_street.house2.room1
import district.soviet_street.house2.room2

area = {
    'central_street': {
        'house1': {
            'room1': [],
            'room2': []
        },
        'house2': {
            'room1': [],
            'room2': []
        }
    },
    'soviet_street': {
        'house1': {
            'room1': [],
            'room2': []
        },
        'house2': {
            'room1': [],
            'room2': []
        }
    },
}

area['central_street']['house1']['room1'] = district.central_street.house1.room1.folks
area['central_street']['house1']['room2'] = district.central_street.house1.room2.folks
area['central_street']['house2']['room1'] = district.central_street.house2.room1.folks
area['central_street']['house2']['room2'] = district.central_street.house2.room2.folks
area['soviet_street']['house1']['room1'] = district.soviet_street.house1.room1.folks
area['soviet_street']['house1']['room2'] = district.soviet_street.house1.room2.folks
area['soviet_street']['house2']['room1'] = district.soviet_street.house2.room1.folks
area['soviet_street']['house2']['room2'] = district.soviet_street.house2.room2.folks

all_folks = []

for street_name, street in area.items():
    for house_name, house in street.items():
        for room_name, room in house.items():
            all_folks.extend(area[street_name][house_name][room_name])

print(', '.join(all_folks))
