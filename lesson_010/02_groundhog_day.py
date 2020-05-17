# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import choice

ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0

# TODO: реализуйте все 7 исключений. Их классы.

# TODO: сделайте список классов Исключений. Потом рандомно, 1 к 13, выбираем 1 случайное исключени и возуждаем его.

def one_day():
    # TODO: в итоге у неас будет 1 if вместо 6
    if choice(range(1, 13)) == 1:
        raise BaseException('IamGodError')
    if choice(range(1, 13)) == 2:
        raise BaseException('DrunkError')
    if choice(range(1, 13)) == 3:
        raise BaseException('GluttonyError')
    if choice(range(1, 13)) == 4:
        raise BaseException('DepressionError')
    if choice(range(1, 13)) == 5:
        raise BaseException('SuicideError')
    if choice(range(1, 13)) == 6:
        raise BaseException('CarCrashError')
    return choice(range(1, 8))


now_day = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        now_day = one_day()
    except BaseException as exc:
        now_day = 0
        print(f'Поймано исключеие {exc}')
    finally:
        carma += now_day
        print(carma)


# https://goo.gl/JnsDqu
