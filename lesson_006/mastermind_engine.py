from random import randint, sample

main_number = 0


def make_number():
    global main_number
    # main_number = str(randint(1, 9))      #  это же был крутой рабочий способ, способ выше подразумевает создание
    #                                               списка из 10 чисел, и только потом из него выберут 1 число.

    #  пример работы sample()
    #       random.sample([1,2,3,4,5,6,7,8,9], 4)		# вернет список из 4 рандомных чисел

    sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    main_number = sample(sample_list[1::], 1)
    sample_list.remove(*main_number)
    main_number += sample(sample_list, 3)

    # while len(main_number) < 4:
    #     sample_list.remove(main_number[len(main_number)-1])
    #     main_number.extend(sample(sample_list, 1))

    # main_number = str(randint(1, 9))
    # while len(main_number) < 4:
    #     main_number = str(randint(0, 9))
    #     if adding_number[0] not in main_number:  # проверка на повторение добавляемого числа
    #         main_number += adding_number

    #
    #  sample - это функция, которая ЗА нас выберет N рандомных неповторяющихся между собой чисел из списка который мы
    #  ей передали. Нам нет никакого смысла самим контролировать что он выбирает.
    #  .
    #  Красивая схема может выглядеть так:
    #   загадываем 1ую цифру, используя randint;
    #   создаем список из 10 цифр; удаляем в нем цифру, которая была загадана randint();
    #   используем sample() по оставшемуся списку чисел, чтобы он загадал нам оставшиеся цифры.
    #   .
    #   В итоге получаем число из 4 цифр, 1ая не 0, и все не повторяющиеся.

    # TODO: или вы заменили randint() на sample, потому то пытались сложить Число и Список и вылетала ошибка?
    #   ОТВЕТ:  Не, логика другая была) не додумал/не дочитал про Sample и пошел не по тому пути. Сейчас в итоге
    #   отказался от randint, так как не поулчилось уложиться в меньше чем 4 строки так как сейчас.
    return main_number


def check_number(checking_number):
    global main_number

    quantity_bulls = 0
    quantity_cows = 0

    checking_number_str = list(checking_number)
    for i, item_checking_number in enumerate(checking_number_str):
        for k, item_main_number in enumerate(main_number):
            if int(item_checking_number) == item_main_number and k != i:
                quantity_cows += 1
        if int(item_checking_number) == main_number[i]:
            quantity_bulls += 1
    return {'bulls': quantity_bulls, 'cows': quantity_cows}


def check_right(number):
    if len(set(number)) < 4 or \
            not number.isdigit() or \
            int(number) < 1000 or \
            len(number) > 4 or \
            number[0] == '0':
        return False
    return True

    #  у нас должны быть проверки для случае:
    #  1. введена фраза вместо числа;
    #  2. повторяющиеся цифры в числе;
    #  3. слишком длинное или короткое число;
    #  4. число начинается с 0.
