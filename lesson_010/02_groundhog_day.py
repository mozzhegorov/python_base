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
from random import randint
from abc import ABC, abstractmethod

ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0

# TODO: понимаю, почему наследуем от Exception, но не понимаю, зачем наследовались еще и от ABC?
class CustomException(Exception, ABC):
    def __init__(self):     # TODO: почему бы родительскому конструктору сразу не принимать параметр "месседж"?
        self.message = None

    def __str__(self):
        return self.message


class IamGodError(CustomException):
    @abstractmethod         # TODO: почему конструктор у нас абстрактный?
    def __init__(self):     # TODO: PyCharm подсвечивает грязно-желтым "__init__". Это warning. Если навести мышку, то
        self.message = 'IamGodError'        # то узнаем, что внутри своего конструктора забыли вызвать родительский конструктор.

class DrunkError(CustomException):
    @abstractmethod
    def __init__(self):
        self.message = 'DrunkError'


class GluttonyError(CustomException):
    @abstractmethod
    def __init__(self):
        self.message = 'GluttonyError'


class DepressionError(CustomException):
    @abstractmethod
    def __init__(self):
        self.message = 'DepressionError'


class SuicideError(CustomException):
    @abstractmethod
    def __init__(self):
        self.message = 'SuicideError'


class CarCrashError(CustomException):
    @abstractmethod
    def __init__(self):
        self.message = 'CarCrashError'

# TODO: список сделан логично.
exceptions = [
    IamGodError,
    DrunkError,
    GluttonyError,
    DepressionError,
    SuicideError,
    CarCrashError
]


def one_day():
    exc_num = randint(0, 12)
    if exc_num < len(exceptions):   # TODO: значит исключения будут вызван в случаях от 0 до 5. Т.е. 6 из 12 вариантов. Т.е. вероятность 50%.
        raise exceptions[exc_num]   #  какую вероятность от нас требует задание? вероятность возникновения исключения
    return randint(1, 8)


now_day = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        now_day = one_day()
    except Exception as exc:
        now_day = 0
        print(f'Поймано исключеие {exc}')
    finally:
        carma += now_day
        print(carma)

# https://goo.gl/JnsDqu
