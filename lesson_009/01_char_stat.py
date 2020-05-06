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
from operator import itemgetter
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

    def get_file_stat(self):
        if self.file_name.endswith('.zip'):
            self.unzip_file()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.get_line_stat(line=line)
        return self.stat

    def get_line_stat(self, line):
        for char in line:
            if char.isalpha():
                self.stat[char] += 1
        return self.stat

    def sorting(self):
        return sorted(self.stat.items())

    def print_stat(self):
        total_letters = 0
        print('''+---------+----------+
|  буква  | частота  |
+---------+----------+''')

        for pair in self.sorting():
            print(f'|{pair[0]:^9}|{pair[1]:^10}|')
            total_letters += pair[1]

        print(f'''+---------+----------+
|  итого  |{total_letters:^10}|
+---------+----------+''')


class RevAlphabeticSort(TextStat):

    def __init__(self, file_name):
        super().__init__(file_name=file_name)

    def sorting(self):
        return sorted(self.stat.items(), reverse=True)


class QuantitySort(TextStat):

    def __init__(self, file_name):
        super().__init__(file_name=file_name)

    def sorting(self):
        return sorted(self.stat.items(), key=itemgetter(1))


text = TextStat(file_name='python_snippets\\voyna-i-mir.txt.zip')
text.get_file_stat()
text.print_stat()

text = RevAlphabeticSort(file_name='python_snippets\\voyna-i-mir.txt.zip')
text.get_file_stat()
text.print_stat()

text = QuantitySort(file_name='python_snippets\\voyna-i-mir.txt.zip')
text.get_file_stat()
text.print_stat()

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


#  добавить Метод "форматированный вывод, в виде таблицы", согласно ТЗ.

#  добавить Метод "сортировку по алфавиту"
#  сортировка словаря.
#  Как сортировать? Использовать параметр 'key' у функции sorted.
#  Пусть есть словарь d, скормим его .items() функции sorted() и посмотрим что вышло:
#       d = {'b': 1, 'a': 2, 'c':3}
#       print(sorted(d.items()))            # [('a', 2), ('b', 1), ('c', 3)]
#  .
#  Ф-ция сортировки отсортировала список пар. Каждая пара ключ-значения представлена в виде кортежа.
#  .
#  Когда мы добавляем 'key', мы указываем, что сортировать нужно по какому-то критерию, который должен
#  высчитываться для каждого элемента списка, т.е. для каждой пары.
#  Пример:
#       # импортируем функцию, которая принимает индекс и выдает значение по нему, можно сказать
#       # что itemgetter - это и есть квадратные скобки '[]'
#       from operator import itemgetter
#       .
#       # .items() возвращает пары ключ-значение в виде кортежей. Поэтому здесь происходит сортировка
#       # списка пар ключ-значение. При этом в качестве ключа (критерия) кортировки берется значение,
#       # которое возвращает itemgetter для 1го (не 0го, а 1го) элемента. Т.е. для значения списка.
#       sorted(d.items(), key=itemgetter(1))
#  .
#  itemgetter(1) берет каждую пару и возвращает последний элемент: 2, 1, 3. Получив критерии по которым
#  нужно сортировать элементы, функция sort выполняет сортировку:
#        print(sorted(d.items(), key=itemgetter(1)))           # [('b', 1), ('a', 2), ('c', 3)]
#  .
#  В итоге, мы получаем список из котрежей, где 0ое значение - значения словаря, а 1ое значение - ключ
#  словаря. При этом, этот набор отсортирован по значениям! То, что нужно)
#  .
#  Сортировать словарь - непростая задача. Совсем. Есть более удобный способ, но он еще более сложный,
#  использует словарные включения. Поэтому мы пока остановимся на этом способе.


#  текущий подход сортировки интересный) У него есть 1 изъян: если в словаре будет 2 буквы: А и я, то у нас вместо
#  2х строк в таблице будет 60+ строк и большинство с нулями.
