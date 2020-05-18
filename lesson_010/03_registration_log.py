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
    #  если мы хотим разбить строку по пробелам, лучше всегда использовать .split() без параметра.
    #  Да, в таком случае символы перевода строки "\n" будут откинуты. Т.е. сначала будет выполнен .strip(),
    #  а только потом split(' ').
    line = line.split()
    person_name = line[0]
    person_email = line[1]
    person_age = line[2]

    if len(line) != 3:
        raise ValueError("Неверное количество параметров")
    if not person_name.isalpha():
        raise NotNameError("Указано не верно имя")
    if not ('@' in person_email and '.' in person_email):
        raise NotEmailError("Указан не верно Email")
    if person_age.isalpha():
        raise ValueError("Возраст указан не верно")
    # Info. попытка привести строку к целому само по себе вызове ValueError
    if not (9 < int(person_age) < 100):
        raise ValueError("Возраст не соответствует требованиям")
    return line


#  Нужен ли ValueError при split()?
#   x, y, z, d = 'a a a'.split()
#   Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#   ValueError: not enough values to unpack (expected 4, got 3)
#  .
#  Поэтому мы можем сразу приравнять split() к 3 переменным с понятными именами.
#  Или, если хочется явно вызывать этот эксепшн, пусть будет, я совсем не против. Только давайте после него, если
#  он не случился, разобьем list_line на 3 переменных с понятными именами. А то ниже, мы начинаем сравнивать
#  list_line[0] и list_line[1] и list_line[2] и понять что из них за что отвечает будет не просто)


#  если лог файл будет весить 1 ГБ, то мы будем держать в памяти это 1 ГБ.
#  Нам лучше открыть все 3 файла и делать чтение/запись в один момент.
good_list = ""
bad_list = ""
with open('registrations.txt', encoding='utf8') as ff:
    for line in ff:
        try:
            # print(checking_line(line=line))
            check_line(line=line)
            with open('registrations_good.log', mode='a') as file:
                file.write(line)
        except Exception as exc:
            # тут сразу будет запись в файл
            with open('registrations_bad.log', mode='a') as file:
                file.write(line)
            print(f'Ошибка в линии "{line[:-1]}" - {exc}')
