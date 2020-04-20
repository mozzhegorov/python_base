# -*- coding: utf-8 -*-


from random import randint, choice

from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cats_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды кота осталось {}, уровень загрязненности {}'.format(
            self.food, self.money, self.cats_food, self.dirt)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    # TODO: давайте сделаем все буквы в названии метода строчными, чтобы соответствовать стилю PEP8.
    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        print(self.house.cats_food, self.cat.fullness)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.cats_food < 20 and self.cat.fullness < 20:
            self.buy_cats_food()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt > 40:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()        # TODO: телевизор (3,4,5,6), а есть() и работать() соответственно 1 и 2.
                                    #  Однако Гарри Поттер тот еще лентяй!

    def get_cat(self, cat):
        self.cat = cat
        cat.house = self.house
        self.fullness -= 5
        cprint('{} Подобрал кота'.format(self.name), color='cyan')

    def buy_cats_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cats_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning(self):
        cprint('{} прибрался в доме'.format(self.name), color='blue')
        # TODO: а если грязи в доме меньше 100?
        self.house.dirt -= 100
        self.fullness -= 20


class Cat:
    names = ['Васька', 'Муська', 'Арчи', 'Бисквит', 'Тимоша', 'Симба', 'Шкипер', ]

    def __init__(self):
        self.name = choice(Cat.names)
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {} сытость {}'.format(self.name, self.fullness)

    def sleeping(self):
        cprint('{} спит'.format(self.name), color='blue')
        self.fullness -= 10

    def eating(self):
        if self.house.cats_food >= 10:
            cprint('{} спит'.format(self.name), color='blue')
            self.fullness += 20
            self.house.cats_food -= 10
        else:
            print('Еды для кота не осталось!')

    def cutting_wallpapers(self):
        cprint('{} подрал обои'.format(self.name), color='blue')
        self.house.dirt += 5
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.eating()
        elif dice == 1:
            self.sleeping()
        else:
            self.cutting_wallpapers()


my_sweet_home = House()
person = Man(name='Гарри Поттер')
pat = Cat()

person.go_to_the_house(house=my_sweet_home)
person.get_cat(cat=pat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    person.act()
    pat.act()
    print('--- в конце дня ---')
    print(person)
    print(pat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
