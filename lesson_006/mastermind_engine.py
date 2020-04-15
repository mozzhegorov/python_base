from random import randint

main_number = 0


def make_number():
    global main_number
    main_number = str(randint(1, 9))

    # TODO: со строкой выше согласен. Примените здесь random.sample
    #  .
    #  пример работы sample()
    #       random.sample([1,2,3,4,5,6,7,8,9], 4)		# вернет список из 4 рандомных чисел
    while len(main_number) < 4:
        adding_number = str(randint(0, 9))
        if adding_number not in main_number:
            main_number += adding_number
    return main_number


def check_number(checking_number):
    quantity_bulls = 0
    quantity_cows = 0

    checking_number_str = str(checking_number)

    # TODO: указание глобальных переменных пишется в самом начале ф-ции
    global main_number

    # TODO: какой тип имеет main_number?
    main_number_str = str(main_number)
    for i, item_checking_number in enumerate(checking_number_str):
        for k, item_main_number in enumerate(main_number_str):
            if item_checking_number == item_main_number and k != i:
                quantity_cows += 1
        if item_checking_number == main_number_str[i]:
            quantity_bulls += 1
    return {'bulls': quantity_bulls, 'cows': quantity_cows}


def check_repeat(number):
    if len(set(number)) < 4:
        return 0
    return 1
