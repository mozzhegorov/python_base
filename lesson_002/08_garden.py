#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)


# выведите на консоль все виды цветов
garden_meadow_set = set(garden_set | meadow_set)
print(garden_meadow_set)

# выведите на консоль те, которые растут и там и там
garden_meadow_set = set(garden_set & meadow_set)
print(garden_meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_meadow_set = set(garden_set - meadow_set)
print(garden_meadow_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
garden_meadow_set = set(meadow_set - garden_set)
print(garden_meadow_set)


#  все верно) в приципе, небольшие и несложные вычисления можно выполнять в print().
#  Небольшие - если размер print() умещается в одну строку длиной 120 символов;
#  Несложные - если внутри print() выполняет операция, результат которой очевиден. Мат.формулы почти всегда не очевидны.

# зачет!