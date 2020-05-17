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
    # TODO: если мы хотим разбить строку по пробелам, лучше всегда использовать .split() без параметра.
    #  Да, в таком случае символы перевода строки "\n" будут откинуты. Т.е. сначала будет выполнен .strip(),
    #  а только потом split(' ').
    line = line.split(' ')
    if len(line) < 3:   # TODO: а если больше?  здесь лучше подойдет ==
        raise ValueError("Недостаточно параметров")

    # TODO: Здесь лучше распаковать кортеж в 3 переменных, с понятным именами. И дальше проверять их, а не line[0] или line[2]

    if not line[0].isalpha():
        raise NotNameError("Указано не верно имя")
    if not ('@' in line[1] and '.' in line[1]):
        raise NotEmailError("Указан не верно Email")

    # TODO: Info. попытка привести строку к целому само по себе вызове ValueError
    if not (9 < int(line[2]) < 100):
        raise ValueError("Возраст не соответствует требованиям")
    return line
# TODO: Нужен ли ValueError при split()?
#   x, y, z, d = 'a a a'.split()
#   Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#   ValueError: not enough values to unpack (expected 4, got 3)
#  .
#  Поэтому мы можем сразу приравнять split() к 3 переменным с понятными именами.
#  Или, если хочется явно вызывать этот эксепшн, пусть будет, я совсем не против. Только давайте после него, если
#  он не случился, разобьем list_line на 3 переменных с понятными именами. А то ниже, мы начинаем сравнивать
#  list_line[0] и list_line[1] и list_line[2] и понять что из них за что отвечает будет не просто)




# TODO: если лог файл будет весить 1 ГБ, то мы будем держать в памяти это 1 ГБ.
#  Нам лучше открыть все 3 файла и делать чтение/запись в один момент.
good_list = ""
bad_list = ""
with open('registrations.txt', encoding='utf8') as ff:
    for line in ff:
        try:
            # print(checking_line(line=line))
            check_line(line=line)
            good_list += line
        except Exception as exc:
            # TODO: тут сразу будет запись в файл
            bad_list += line
            print(f'Ошибка в линии "{line[:-1]}" - {exc}')

with open('registrations_bad.log', mode='w') as file:
    file.write(bad_list)

with open('registrations_good.log', mode='w') as file:
    file.write(good_list)
