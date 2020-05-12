# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from abc import ABC, abstractmethod

class SortingAbstract(ABC):

    def __init__(self, basic_folder, direct_folder):
        self.basic_folder = basic_folder
        self.direct_folder = direct_folder
        self.files_time = {}
        self.files_list = {}
        self.zfile = None

    @abstractmethod
    def get_files_stat(self):
        pass

    def create_new_dirs(self):
        for file, ts in self.files_time.items():
            if not os.path.basename(file):
                continue
            checking_path = os.path.normpath(os.path.join(self.direct_folder,
                                                          str(ts[0]),
                                                          str(ts[1]),
                                                          str(ts[2])))
            if not os.path.exists(checking_path):
                os.makedirs(os.path.join(checking_path))

    @abstractmethod
    def copy_files(self):
        pass


class SortingZipToFolders(SortingAbstract):

    def get_files_stat(self):
        self.zfile = zipfile.ZipFile(self.basic_folder + '.zip', 'r')
        for file in self.zfile.infolist():
            self.files_time[file.filename] = file.date_time[0:3]

    def copy_files(self):
        for file, ts in self.files_time.items():
            if not os.path.basename(file):
                continue

            source = self.zfile.open(file)
            destination = os.path.normpath(os.path.join(self.direct_folder,
                                                        str(ts[0]),
                                                        str(ts[1]),
                                                        str(ts[2]),
                                                        os.path.basename(file)))
            with open(destination, 'wb') as outfile:
                shutil.copyfileobj(source, outfile)


class SortingFolderToFolders(SortingAbstract):

    def get_files_stat(self):
        for dirpath, _, filenames in os.walk(self.basic_folder):
            for file in filenames:
                filename = os.path.normpath(os.path.join(dirpath, file))
                self.files_time[filename] = (time.gmtime(os.path.getmtime(filename)).tm_year,
                                             time.gmtime(os.path.getmtime(filename)).tm_mon,
                                             time.gmtime(os.path.getmtime(filename)).tm_mday)

    def copy_files(self):
        for file, ts in self.files_time.items():
            if not os.path.basename(file):
                continue

            source = os.path.normpath(file)
            destination = os.path.normpath(os.path.join(self.direct_folder,
                                                        str(ts[0]),
                                                        str(ts[1]),
                                                        str(ts[2]),
                                                        os.path.basename(file)))
            shutil.copy2(source, destination)


sorting = SortingFolderToFolders(basic_folder='icons', direct_folder='icons_by_year')
sorting.get_files_stat()
sorting.create_new_dirs()
sorting.copy_files()


sorting = SortingZipToFolders(basic_folder='icons', direct_folder='icons_by_year_zip')
sorting.get_files_stat()
sorting.create_new_dirs()
sorting.copy_files()

# как насчет усложненной версии?
#       ОТВЕТ: а мне показалось я изначально усложненную версию начал. потому что
#       когда сделал предварительной распаковкой файлов в папку - они получились у меня датой создания днем распаковки
#       и в итоге все файлы в одну папку летели. я в итоге переделал на чтение из зип файла чтобы бралась дата создания
#       файла из зип. Сейчас немного не соображу как быть...

#  да, думаю некорректно задал вопрос.
#  Усложненная версия: реализованный шаблонный метод для двух классов. Один работает по архивам (текущий класс), второй
#  по разархивированным папкам (os.walk() и копировани файла простым copy2())
#  .
#  Сложность задачи: вычленить общую часть для обоих классов в родительскую, определить какие методы имеют разную
#  реализацию, а какие общую, т.е необходимо определить как из методов необходимо имплементировать в классах наследниках,
#  а какие сделать общими в родительском классе.
#  .
#  Общий алгоритм похож: проходим в цикле по списку файлов в папке/архиве и копирует в папки, в соответствии с датой
#  создания.
#  .
#  Примечание: для версии с os.walk() извлекать архив программно не нужно.

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
