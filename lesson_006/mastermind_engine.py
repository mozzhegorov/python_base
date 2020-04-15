from random import randint, sample

main_number = 0


def make_number():
    global main_number
    main_number = sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    # main_number = str(randint(1, 9))
    # TODO: со строкой выше согласен. Примените здесь random.sample
    #  .
    #  пример работы sample()
    #       random.sample([1,2,3,4,5,6,7,8,9], 4)		# вернет список из 4 рандомных чисел
    while len(main_number) < 4:
        adding_number = sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 1)
        if adding_number[0] not in main_number:  # проверка на повторение добавляемого числа
            main_number += adding_number
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
    if len(set(number)) < 4 and number < 1000:
        return False
    return True
