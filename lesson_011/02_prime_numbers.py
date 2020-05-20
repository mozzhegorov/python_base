# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.n_max = n

    def __iter__(self):
        self.num = 1                    # TODO: создание полей вне конструктора - крайне плохая идея.
        return self                     #  это поле должно быть и в конструкторе в первую очередь!

    def __next__(self):
        if self.num > self.n_max:
            raise StopIteration()       # TODO: Достаточно "raise StopIteration" (объект создавать не обязательно)
        self.num += 1
        for prime in self.prime_numbers:
            if self.num % prime == 0:
                break
        else:
            self.prime_numbers.append(self.num)
            return self.num

prime_number_iterator = PrimeNumbers(n=100)
# TODO: prime_number_iterator - это объект класс PrimeNumbers.
#  Это пока не итератор, т.к. мы не настроили его поля.
#  Итератор будет получен тогда, когда мы подставим его в цикл, или явно вызовем iter(prime_number_iterator).
vot_eto_iterator = iter(prime_number_iterator)  # здесь произойдет вызов __iter__, настройка полей и вернется тот же объект, но уже готовый к итерированию
for number in prime_number_iterator:
    if number:          # TODO: это хак. Класс PrimeNumbers возвращает None`ы и Простые числа?)
        print(number)

# TODO: надо поменять __next__ Так, чтобы он возвращал следующее простое число.

exit(123)
# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    pass
    # TODO здесь ваш код


for number in prime_numbers_generator(n=10000):
    print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
