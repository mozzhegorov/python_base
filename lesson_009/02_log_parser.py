# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint
from collections import defaultdict


class ParseLog:

    def __init__(self, source, target_prefix):
        self.file_name = source
        self.target_file = target_prefix + source
        self.nok_count = defaultdict(int)

    def parsing(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    # TODO: внутрь лучше предавать line
                    self.counting_nok(date_time=line[1:17])

    # TODO: а в ней уже резать строку и добавлять в словарь
    def counting_nok(self, date_time):
        self.nok_count[date_time] += 1
        return self.nok_count

    def write_target_file(self):
        file_name = self.target_file
        file = open(file_name, mode='w')  # mode (режим): запись символьная, кодировка по умолчанию utf8
        # TODO: Здесь лучше применть items()
        for string in self.nok_count:
            file.write(f'{string}: {self.nok_count[string]}\n')
        file.close()


read_file = ParseLog(source='events.txt', target_prefix='parsing_')
read_file.parsing()
#pprint(read_file.nok_count)
read_file.write_target_file()


# TODO: После описанных правок, можно создать 3 новых класса-наследника, которые будут прегружать метод counting_nok()
#  и определять в нем какой длины должен быть ключ (часы, минуты или год).
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


