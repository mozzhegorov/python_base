# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
from pprint import pprint
from collections import defaultdict


class TextStat:

    def __init__(self, file_name):
        self.stat = defaultdict(int)
        self.file_name = file_name

    def unzip_file(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        #  почему бы сразу не взять последний файл в списке, если он там есть?
        #  Мы в цикле распаковываем все файлы, а по итогу запоминаем только последний.
        self.file_name = zfile.namelist()[-1]
        zfile.extract(self.file_name)

    def open_file(self):
        if self.file_name.endswith('.zip'):
            self.unzip_file()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.get_stat(line=line)
        return self.stat

    def get_stat(self, line):
        for char in line:
            if char.isalpha():
                self.stat[char] += 1
        return self.stat


text = TextStat(file_name='python_snippets\\voyna-i-mir.txt.zip')
text.open_file()
# print(ord(min(text.stat)))
first_letter = ord(min(text.stat))
last_letter = ord(max(text.stat))
total_letters = 0

print('''+---------+----------+
|  буква  | частота  |
+---------+----------+''')

for i in range(first_letter, last_letter + 1):
    if chr(i) in text.stat:
        print(f'|{chr(i):^9}|{text.stat[chr(i)]:^10}|')
        total_letters += text.stat[chr(i)]

print(f'''+---------+----------+
|  итого  |{total_letters:^10}|
+---------+----------+''')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


#  можно использовать defaultdict
#       from collections import defaultdict
#  .
#       s = 'mississippi'         # берем строку (итерируемый объект)
#       d = defaultdict(int)      # создаем словарь (подробности ниже)
#       for k in s:               # проходимся по строке и выполняем += 1 для каждой буквы.
#           d[k] += 1
#  .
#       print(d.items())          # [('i', 4), ('p', 2), ('s', 4), ('m', 1)]
#  .
#  Почему код выше работает? Почему на строке "d[k] += 1" при попытке обращение к незаданному ранее ключу
#  не происходит исключение?
#  .
#  Когда мы создаем словарь defaultdict, мы передаем ему ФУНКЦИЮ, которая будет вызываться для инициализации
#  значения, если это значение не найдено в словаре. Поэтому когда мы обращаемся print(d[1000500]) в словаре
#  будет создана пара ключ 1000500 и значение int() (т.е. 0, т.к. int() == 0)
#  .
#  Примеры:
#       d_1 = defaultdict(int)      # {}
#       d_1[100500] += 100          # {100500: 100}
#       x = d_1[123]                # x = 0, d={100500: 100, 123: 0}
#  .
#       d_2 = default(list)         # {}
#       x = d_2['hello']            # x = [], d={'hello': []}
#       d_2['test'].append(123)     # d={'hello': [], 'test': [123]}
#  .
#  Поэтому мы можем удалить проверку условия и смело обращаться к значению по ключу (даже если его еще
#  нет).