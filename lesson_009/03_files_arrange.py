# -*- coding: utf-8 -*-

import os, time, shutil

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
import zipfile
from pprint import pprint


class SortingUpToFolders:

    def __init__(self, basic_folder, direct_folder):
        self.basic_folder = basic_folder
        self.direct_folder = direct_folder
        self.files_time = {}
        self.files_list = {}

    def unzipping(self):
        zfile = zipfile.ZipFile(self.basic_folder + '.zip', 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)

    def get_files_list(self):
        for dirname, dirnames, filenames in os.walk(self.basic_folder):
            self.files_list[dirname] = filenames

    def get_files_stat(self):
        for dir, dir_files in self.files_list.items():
            for file in dir_files:
                secs = os.path.getmtime(os.path.join(dir, file))
                file_time = time.gmtime(secs)
                # print(file)
                self.files_time[file] = file_time
        # z = zipfile.ZipFile(self.basic_folder + '.zip')
        # info = z.infolist()
        # for file in info:
        #     self.files_time[file] = file.date_time[0:3]

    def create_new_dirs(self):
        inside_dirs = {}
        # if os.path.exists(self.direct_folder):
        #     inside_dirs = os.listdir(self.direct_folder)
        #     pprint(inside_dirs)
        # else:
        #     os.makedirs(self.direct_folder)

        for file, time in sorting.files_time.items():
            if os.path.exists(os.path.join(self.direct_folder,
                                           str(time.tm_year),
                                           str(time.tm_mon),
                                           str(time.tm_mday))):
                pass
            else:
                os.makedirs(os.path.join(self.direct_folder,
                                         str(time.tm_year),
                                         str(time.tm_mon),
                                         str(time.tm_mday)))


sorting = SortingUpToFolders(basic_folder='icons', direct_folder='icons_by_year')
sorting.unzipping()
sorting.get_files_list()
sorting.get_files_stat()
# # print(sorting.files_time)
sorting.create_new_dirs()

# z = zipfile.ZipFile('icons.zip')
# info = z.infolist()
# for file in info:
#     print(file.filename)
#     print(file.date_time)
# print(zipfile.ZipFile('icons.zip').from_file(filename='\\icons\\actions\\address-book-new.png'))
# with zipfile.ZipInfo('icons.zip') as myzip:
#     print(myzip)
    # for dirs in myzip.namelist():
    #     print(dirs)
    #     secs = os.path.getmtime(dirs)
    #     file_time = time.gmtime(secs)
    #     print(file_time)
        # with myzip.open('eggs.txt') as myfile:
        #     print(myfile.read())

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
