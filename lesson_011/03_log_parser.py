# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

from collections import defaultdict
from itertools import islice


#  сильная сторона Итераторов/Генераторов в том, что мы не храним огромное число данные сразу; и не генерируем
#  огромное число данных, чтобы потом выдать 1 строку.
#  .
#  Типичный пример итератора: range()

# test = range(10**8)     # Это генератор невероятно огромного списка. Но он не создан, хотя готов к этому.
# test_iter = iter(test)
# print(test_iter)
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))

#  он не выдает все числа сразу, а отдает по одному, когда надо.
#  Если же мы попытается создать словарь таких размеров:
# lst = list(test)        # Эта операция займет несколько секунд

#  сейчас наш код действует по 2ому пути. Мы берем файл логов, весь парсим его и выдаем результат по кусочкам.
#  Если в файле будет 100500 строк, то сначала все должны будет распарсить.
#  .
#  Наша же задача: написать такой итератор, чтобы при следующем запуске он открывал файл на нужной строке, парсил
#  столько строк, сколько произошло событий за 1 минуту. Затем выдает результат и останавливается.
#  .
#  Даю 2 наводки:
#   1. открытый файл - итерируемый объект;
#   2. islice.


#  Простой срез и "умный срез".
#  from itertools import islice
#  lst = [0,1,2,3,4,5,6,7,8,9,10]
#  slice_1 = lst[2:9:3]                 # [2, 5, 8]
#  islice_2 = islice(lst, 2, 9, 3)      # <itertools.islice object at 0x0000021EB6555368>
#  slice_2 = list(islice_2)             # [2, 5, 8]
#  .
#  Простой срез lst[2:9:3] сразу возвращает наш результат (список)
#  А умный срез islice(lst, 2, 9, 3) возвращает итератор по списку "начиная с элемента №2 по 9 с шагом 3"
#  .
#  Представим, что в lst находится 100500 элементов. Если взять срез размером с его половину,
#  то затраты памяти увеличатся в 1.5 раза. И этот срез будет лежать в памяти. А можно взять умный
#  срез, который будет возвращать нам по 1 элементу за раз.
#  .
#  islice - это оптимизированный вариант среза, который может пригодиться, если нам не нужен весь
#           срез сразу, и мы хотим обрабатывать значения среза по одному.
#  .
#  https://docs.python.org/2/library/itertools.html#itertools.islice

class ParseNok:

    def __init__(self, source):
        self.file_name = source
        self.nok_count = defaultdict(int)
        self.file = None
        self.file = open(self.file_name, 'r', encoding='utf8')
        self.next_before_dt = [None, None]

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.next_before_dt[0] = self.next_before_dt[1]
            line = islice(self.file, 0, 1)
            data_string = list(line)

            if not data_string:
                self.file.close()
                raise StopIteration

            data_string = data_string[0]
            date_time = data_string[1:17]
            if self.next_before_dt[0] is not None \
                    and date_time != self.next_before_dt[0] \
                    and self.nok_count[self.next_before_dt[0]] != 0:
                if "NOK" in data_string:
                    self.nok_count[date_time] += 1
                self.next_before_dt[1] = date_time
                break
            if "NOK" in data_string:
                self.nok_count[date_time] += 1
            self.next_before_dt = [date_time, date_time]
        return self.next_before_dt[0], self.nok_count[self.next_before_dt[0]]


grouped_events = ParseNok(source='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')


# test = [1, 2, 3, 4, 5, 6]
# test_iter = iter(test)
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))

# class Test:
#
#     def __init__(self):
#         self.listing_iter = range(10)
#         print(self.listing_iter)
#         self.iter_obj = iter(self.listing_iter)
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         # a = 0
#         # while True:
#         #     line = list(islice(self.iter_obj, 0, 1))
#         #     print(line)
#         #     a += 1
#         #     if a > 10:
#         #         break
#         if self.i > 10:
#             raise StopIteration
#         return islice(self.iter_obj, 0, 3)
#
#
# # Test_1 = Test()
# # for i in Test_1:
# #     print(list(i))
