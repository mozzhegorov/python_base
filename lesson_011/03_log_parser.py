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


class ParseNok:

    def __init__(self, source):
        self.file_name = source
        self.nok_count = defaultdict(int)
        self.parsing()
        self.iter_date_time = iter(self.nok_count.keys())  # говорим что ключи self.nok_count - итерируемый объект
        self.iter_nok_quantity = iter(self.nok_count.values())  # для второго варианта решения задачи

    def __iter__(self):
        return self

    def __next__(self):
        date_time = next(self.iter_date_time)  # перехожим по ключу как по итерируемому объекту словаря
        nok_quantity = self.nok_count[date_time]  # TODO: Основной, т.к. точно указываем на элемент словаря
        # nok_quantity = next(self.iter_nok_quantity)    # TODO: Один из вариантов решения задачи.
        return date_time, nok_quantity

    def parsing(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    date_time = line[1:17]
                    self.nok_count[date_time] += 1

    def print_result(self):
        for date_time, quantity in self.nok_count.items():
            print(f'{date_time}: {quantity}')


grouped_events = ParseNok(source='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

# test = [1, 2, 3, 4, 5, 6]
# test_iter = iter(test)
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))
