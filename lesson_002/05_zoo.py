#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo = zoo + birds

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO: результат правильный, давайте добавим сообщение "Лев сдити в клетке №..." (аналогично для жаворонка)
print(zoo.index('lion') + 1)
print(zoo.index('lark') + 1)


# TODO: все правильно, теперь давайте закрепим 2 других метода:
#  1. добавьте птиц из списка birds в последние клетки зоопарка с помощью .extend;
#  2. уберите слона не по значению remove('elephant'), а через удаление по индексу .pop()

