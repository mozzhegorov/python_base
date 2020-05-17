# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_line(line):
    line = line.split(' ')
    if len(line) < 3:
        raise ValueError("Недостаточно параметров")
    if not line[0].isalpha():
        raise NotNameError("Указано не верно имя")
    if not ('@' in line[1] and '.' in line[1]):
        raise NotEmailError("Указан не верно Email")
    if not (9 < int(line[2]) < 100):
        raise ValueError("Возраст не соответствует требованиям")
    return line


good_list = ""
bad_list = ""
with open('registrations.txt', encoding='utf8') as ff:
    for line in ff:
        try:
            # print(checking_line(line=line))
            check_line(line=line)
            good_list += line
        except Exception as exc:
            bad_list += line
            print(f'Ошибка в линии "{line[:-1]}" - {exc}')

with open('registrations_bad.log', mode='w') as file:
    file.write(bad_list)

with open('registrations_good.log', mode='w') as file:
    file.write(good_list)
