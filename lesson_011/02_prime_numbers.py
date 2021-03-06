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
        self.num = None

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num > self.n_max:
            raise StopIteration
        # print(self.prime_numbers)
        while True:
            self.num += 1
            for prime in self.prime_numbers:
                if self.num % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.num)
                return self.num


# prime_number = PrimeNumbers(n=100)
# for number in prime_number:
#     print(number)

# exit(123)


# после подтверждения части 1 преподователем, можно делать
# можно делать часть 2
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []

    for num in range(2, n):
        for prime in prime_numbers:
            if num % prime == 0:
                break
        else:
            prime_numbers.append(num)
            yield num


def is_polyndrom(num):
    str_num = str(num)
    num_len = len(str_num)
    if num < 10:
        return False
    for i in range(num_len):
        if str_num[i] != str_num[-i - 1]:
            return False
    return True


def is_happy_num(num):
    str_num = str(num)
    num_len = len(str_num)
    left = 0
    right = 0
    if num < 10:
        return False
    for i in range(num_len // 2):
        left += int(str_num[i])
        right += int(str_num[-i - 1])
    return left == right


def is_sabita(num):
    _num = (num + 1) / 3
    while _num > 2:
        if _num % 2 != 0:
            return False
        _num //= 2
    if _num in (1, 2):
        return True
    return False


test_number = 123321
print(is_happy_num(test_number))
print(is_polyndrom(test_number))
print(is_sabita(12))

# TODO: 1 вариант. всё как и было, фильтруем с помощью if
for number in prime_numbers_generator(n=10000):
    if is_polyndrom(number):
        print(number)

# TODO: 2 вариант. используем цикл через lambda, потом фильтруем и выводим.
prime_number = map(lambda x: x, prime_numbers_generator(n=10000))
sabita_prime_nums = filter(is_sabita, prime_number)
sabita_prime_nums_list = list(sabita_prime_nums)
print(sabita_prime_nums_list)


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

#  prime_number_iterator - это объект класс PrimeNumbers.
#  Это пока не итератор, т.к. мы не настроили его поля.
#  Итератор будет получен тогда, когда мы подставим его в цикл, или явно вызовем iter(prime_number_iterator).
#  ОТВЕТ: Я вроде это понял, но ведь класс был итерируемый, поэтому не стал его еще загонять в iter(),
#  к тому же работало. В общем вопрос таки, необходимо даже итерируемый класс приводить к итерируемому объекту?

#  явно получать итератор не нужно. Иногда нужно, но не в этом случае.
#  .
#  В прошлой версии было написано:
#       prime_number_iterator = PrimeNumbers(n=100)
#  .
#  Название не точно отражало суть. Это был объект класса PrimeNumbers. Пока еще не итератор. А вот когда мы подставили
#  его в цикл, то цикл сам, без нашего вмешательства вызвал iter(), получил итератор и использовал его.
#  .
#  Как можно проверить "PrimeNumbers(n=100)" это итератор или нет? Выполнить next() по нему. Будет ошибка.
#  .
#  ИТОГО:
#  1. вызывать iter() самому не нужно;
#  2. но за нас это делает цикл, это надо понимать;
#  3. Да, __iter__ возвращает сам объект self. НО до того, пока __iter__ не сработал, объект не может итерироваться,
#     происходит ошибка.
#  .
#  Обычно делают 2 отдельных класса. Итератор (реализует __iter__) в отдельном классе от Коллекции (реализует __next__).

# зачет!