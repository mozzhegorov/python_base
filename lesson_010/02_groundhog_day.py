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
#  Ответ: каюсь, видимо не до конца впитал абстрактные классы (методы).
#         наследование от ABC включил для того, чтобы абстрактный класс ошибок создать не могли.
#         далее декораторы я конечно позорно распихал, а конструктор планировалось что будет каждый раз вызываться
#         свой, без вызова родительского конструктора, как делали в абстрактных классах. В родительском классе был
#         создан конструктор для того, чтобы в родительском классе метод __str__ не ругался ни на что. В общем еще раз
#         подумал и понял что здесь абстрактные классы особо не нужны, так как нет большой цепочки методов. И вообще
#         не нужны много классов. В итоге остановился на одном классе. Очень хочу надеяться что этот метод верный,
#         а не создавать кучу классов для ошибок.

# TODO: согласно заданию должно быть минимум 6 видов исключений.
#  Реализуется просто: наследуется от CustomException, а тело - конструктор, который жестко задает сообщение исключения.

class CustomException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# TODO: это будет кортеж Классов, а не объектов
exceptions = [
    CustomException("IamGodError"),
    CustomException("DrunkError"),
    CustomException("GluttonyError"),
    CustomException("DepressionError"),
    CustomException("SuicideError"),
    CustomException("CarCrashError")
]


def one_day():
    exc_chance = randint(0, 12)
    # TODO: ОТВЕТ: тут видимо не до конца понял ТЗ. Сейчас с вероятность 1/13 выдается какая-то ошибка, а далее еще с
    #  вероятностью 1/6 выбор ошибки.
    if exc_chance == 0:
        exc_num = randint(0, 5)
        raise exceptions[exc_num]       # TODO: используйте choice(), чтобы выбрать 1 элемент из списка.
    return randint(1, 8)


now_day = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        now_day = one_day()
    # TODO: здесь перечислить обрабатываемые исключения.
    except Exception as exc:
        now_day = 0
        print(f'Поймано исключеие {exc}')       # TODO: пишет "Поймано исключение SuicideError", но это не исключение SuicideError
    finally:                                    #  это исключение CustomException с сообщением об ошибке "SuicideError"
        carma += now_day                        #  а должно быть правда исключение класса SuicideError
        print(carma)

# https://goo.gl/JnsDqu
