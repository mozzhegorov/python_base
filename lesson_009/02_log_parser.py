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
from collections import defaultdict
from abc import ABC, abstractmethod


#  Надеюсь, что вы смогли сами реализовать это в 01_char_stat.py задаче) В этом файле приведу пример.
class ParseLogAbstract(ABC):  # наследовались от ABC

    def __init__(self, source, target_prefix):
        self.file_name = source
        self.target_file = target_prefix + source
        self.nok_count = defaultdict(int)

    def parsing(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    date_time = self.parse_line(line=line)
                    self.nok_count[date_time] += 1

    @abstractmethod
    def parse_line(self, line):  # установили этот метод абстрактным
        pass

    def write_target_file(self):
        file_name = self.target_file
        file = open(file_name, mode='w')  # mode (режим): запись символьная, кодировка по умолчанию utf8
        for date_time, quantity in self.nok_count.items():
            file.write(f'{date_time}: {quantity}\n')
        file.close()


class ParseMinLog(ParseLogAbstract):

    def parse_line(self, line):
        return line[1:17]


class ParseHourLog(ParseLogAbstract):

    def parse_line(self, line):
        return line[1:14]


class ParseDayLog(ParseLogAbstract):

    def parse_line(self, line):
        return line[1:11]


class ParseMonthLog(ParseLogAbstract):

    def parse_line(self, line):
        return line[1:8]


read_file = ParseMinLog(source='events.txt', target_prefix='parsing_Min_')
read_file.parsing()
read_file.write_target_file()

read_file = ParseHourLog(source='events.txt', target_prefix='parsing_Hour_')
read_file.parsing()
read_file.write_target_file()

read_file = ParseDayLog(source='events.txt', target_prefix='parsing_Day_')
read_file.parsing()
read_file.write_target_file()

read_file = ParseMonthLog(source='events.txt', target_prefix='parsing_Month_')
read_file.parsing()
read_file.write_target_file()

#  После описанных правок, можно создать 3 новых класса-наследника, которые будут прегружать метод counting_nok()
#  и определять в нем какой длины должен быть ключ (часы, минуты или год).
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# зачет!