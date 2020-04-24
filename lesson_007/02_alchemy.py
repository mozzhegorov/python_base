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

    #   Как можно реализовать метод __add__.
    #   Сравнение лучше производить через isinstance и сам класс (а не просто поле name у объекта).
    #   По условие __add__ Должен возвращать None.
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Filth()
        else:
            return None


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Filth()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if isinstance(other, Pressure):
            return Volcano()
        else:
            return None


class Dust:

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if isinstance(other, Pressure):
            return Volcano()
        else:
            return None


class Lightning:

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name


class Filth:

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name


class Steam:

    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name


class Lava:

    def __init__(self):
        self.name = 'Лава'

    def __str__(self, *args, **kwargs):
        return self.name

    def __add__(self, other):
        if isinstance(other, Pressure):
            return Volcano()
        else:
            return None


class Pressure:

    def __init__(self):
        self.name = 'Давление'

    def __str__(self, *args, **kwargs):
        return self.name


class Volcano:

    def __init__(self):
        self.name = 'Вулкан'

    def __str__(self, *args, **kwargs):
        return self.name


#  Добавьте цикл.
#  Давайте создадим список из всех элементов и перескрещиваем их между собой.
#  Причем цикл сделаем так, чтобы не было повторных пересечений. Например:
#       Вода + Огонь = Пар
#       Огонь + Вода = Пар (эта пара лишняя, т.к. от перестановки мест слагаемых сумма не меняется)
#  .
#  Как это лучше сделать?
#  Дам 2 наводки:
#   1. используйте enumerate() для 1го цикла;
#   2. Для второго цикл используйте не весь element_list, а только его срез начиная какого элемента.
#  .
#  Пример:
#  Пусть у нас есть список [1,2,3,4], сейчас мы имеем 16 пар: 1-1,1-2,1-3,...2-1,...,3-1, ...;
#  А хотим иметь только уникальные пары:
#  1-1, 1-2, 1-3, 1-4
#       2-2, 2-3, 2-4
#            3-3, 3-4
#                 4-4
#  .

element_list = [Water, Air, Fire, Earth]
for num, element in enumerate(element_list):
    for sub_element in element_list[num::]:
        if element != sub_element:  # добавил проверку на одинаковость элемента, можно убрать, но так думаю лучше
            print(element(), '+', sub_element(), '=', element() + sub_element())

print(Earth(), '+', Fire(), '+', Pressure(), '=', Earth() + Fire() + Pressure())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
