# -*- coding: utf-8 -*-

import os
import shutil
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



class SortingUpToFolders:

    def __init__(self, basic_folder, direct_folder):
        # TODO: зачем нам это поле, если мы сразу открываем архив?
        self.basic_folder = basic_folder
        self.direct_folder = direct_folder
        self.files_time = {}
        self.files_list = {}
        # TODO: или зачем открывать сразу архив? Мне кажется более правильным, открывать архив не сразу в конструкторе,
        #  а непосредственно при команде get_files_stat()
        self.zfile = zipfile.ZipFile(self.basic_folder + '.zip', 'r')

    def get_files_stat(self):
        infolist = self.zfile.infolist()    # TODO: можно не использовать промежуточную переменную infolist
        for file in infolist:
            self.files_time[file.filename] = file.date_time[0:3]

    def create_new_dirs(self):
        # TODO: хорошо, удачно применили items(). Обычно вместо time пишу ts (timestamp)
        for file, time in self.files_time.items():
            filename = os.path.basename(file)       # TODO: можно убрать промежуточную переменную.
            if not filename:
                continue
            checking_path = os.path.normpath(os.path.join(self.direct_folder,
                                           str(time[0]),
                                           str(time[1]),
                                           str(time[2])))
            if not os.path.exists(checking_path):
                os.makedirs(os.path.join(checking_path))

    def copy_files(self):
        for file, time in self.files_time.items():
            filename = os.path.basename(file)       # TODO: можно убрать промежуточную переменную filename
            if not filename:
                continue

            source = self.zfile.open(file)
            destination = os.path.normpath(os.path.join(self.direct_folder,
                                                        str(time[0]),
                                                        str(time[1]),
                                                        str(time[2]),
                                                        os.path.basename(file)))
            with open(destination, 'wb') as outfile:
                shutil.copyfileobj(source, outfile)


sorting = SortingUpToFolders(basic_folder='icons', direct_folder='icons_by_year')
sorting.get_files_stat()
sorting.create_new_dirs()
sorting.copy_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
