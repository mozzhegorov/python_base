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
from random import randint, choice
from abc import ABC, abstractmethod

ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0


class CustomException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class IamGodError(CustomException):
    def __init__(self):
        super().__init__(message="IamGodError")


class DrunkError(CustomException):
    def __init__(self):
        super().__init__(message="DrunkError")


class GluttonyError(CustomException):
    def __init__(self):
        super().__init__(message="GluttonyError")


class DepressionError(CustomException):
    def __init__(self):
        super().__init__(message="DepressionError")


class SuicideError(CustomException):
    def __init__(self):
        super().__init__(message="SuicideError")


class CarCrashError(CustomException):
    def __init__(self):
        super().__init__(message="CarCrashError")


exceptions = [
    IamGodError,
    DrunkError,
    GluttonyError,
    DepressionError,
    SuicideError,
    CarCrashError
]


def one_day():
    if not randint(0, 12):          # TODO: хорошо)
        raise choice(exceptions)
    return randint(1, 8)


now_day = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    now_day = 0
    try:
        now_day = one_day()
    except IamGodError as exc:
        print(f'Поймано исключеие {exc}')
    except DrunkError as exc:
        print(f'Поймано исключеие {exc}')
    except GluttonyError as exc:
        print(f'Поймано исключеие {exc}')
    except DepressionError as exc:
        print(f'Поймано исключеие {exc}')
    except SuicideError as exc:
        print(f'Поймано исключеие {exc}')
    except CarCrashError as exc:
        print(f'Поймано исключеие {exc}')
    finally:
        carma += now_day
        print(carma)

# https://goo.gl/JnsDqu

# зачет!