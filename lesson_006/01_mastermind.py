# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastermind_engine import check_number
from mastermind_engine import make_number
from mastermind_engine import check_right

# Цикл всей игры, находимся там, пока играем. Если закончим игру, выходим черезе Break
while True:
    # модуль движка загадывает число
    print(make_number())
    my_num = 0
    steps = 0
    num_of_bulls = 0

    #   находимся в этом цикле, пока число не отгадано (количество быков меньше 4)
    while num_of_bulls < 4:
        # у пользователя запрашивается вариант числа
        if steps < 1:
            print('Я загадал, введите число')
        else:
            print('Не верно, введите число повторно')

        # дальше идем в бесконечный цикл внутри которого проверяем корректность введенного числа

        my_num = input()
        # проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
        if check_right(my_num):
            steps += 1
        else:
            print('Вы ввели не корректное число, введите заново')
            continue

        # модуль движка проверяет число и выдает быков/коров
        dict_of_bulls_cows = check_number(my_num)
        num_of_bulls = dict_of_bulls_cows['bulls']
        num_of_cows = dict_of_bulls_cows['cows']

        # результат быков/коров выводится на консоль
        print('Быков = ', num_of_bulls, 'Коров = ', num_of_cows)
    else:
        print('Вы выиграли, ваше количество шагов равно ', steps)
        if input('Еще партеечку? Если хотите сыграть напишите "Да"') != 'Да':
            print('Спасибо за игру!')
            break
