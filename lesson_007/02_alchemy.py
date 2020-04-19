# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.name = 'Вода'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if other.name == 'Воздух':
            return 'Шторм'
        elif other.name == 'Огонь':
            return 'Молния'
        elif other.name == 'Земля':
            return 'Пыль'
        else:
            return 'Неизвестная реакция'


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if other.name == 'Вода':
            return 'Шторм'
        elif other.name == 'Огонь':
            return 'Пар'
        elif other.name == 'Земля':
            return 'Грязь'
        else:
            return 'Неизвестная реакция'


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if other.name == 'Воздух':
            return 'Молния'
        elif other.name == 'Вода':
            return 'Пар'
        elif other.name == 'Земля':
            return 'Лава'
        else:
            return 'Неизвестная реакция'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
