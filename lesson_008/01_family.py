# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    # TODO: лучше нам эти поля сделать полями объекта.
    #  Иначе, если будет несколько домов, мы не сможем точно определить сколько денег/еды/шуб в каждом.
    total_earned_money = 0
    total_eaten_food = 0
    total_bought_coats = 0

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirty = 0

    def __str__(self):
        return 'В доме еды {}, денег {}, грязи {}'.format(self.food, self.money, self.dirty)

    def act(self):
        self.dirty += 5


class Person:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return ', счастья {}, сытость {}'.format(self.happiness, self.fullness)

    def eat(self):
        # TODO: метод не безопасен. Мы можем уйти в отрицательные значения для еды.
        cprint('{} поел(а)'.format(self.name), color='blue')
        self.house.food -= 20
        self.fullness += 20
        self.house.total_eaten_food += 20


class Husband(Person):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return 'Муж {}'.format(self.name) + super().__str__()

    def act(self):
        # TODO: понижение уровня счастья и проверка, что человек умер, может быть вынесена в act() Общего класса
        if self.house.dirty >= 90:
            self.happiness -= 10
        if self.happiness < 10 or self.fullness < 0:
            cprint('Муж {} умер...'.format(self.name), color='red')
            return

        if self.fullness <= 30:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif self.happiness <= 30:
            self.gaming()
        else:
            # TODO: понизить уровень счастья Мужа на 50% можно, если он помимо 3х действий ниже он будет еще и есть.
            #  У него тогда конечно "сытость" начнет расти быстро. Но иначе, пока не появился Кот, сделать это нельзя
            #  внутри класса Муж (еще есть способ в классе Жена).

            # TODO: 5 строк ниже можно заменить 1 строкой с choice() из списка функций
            rand_act = randint(0, 2)
            if rand_act == 0:
                self.work()
            else:
                self.gaming()

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.money += 150
        self.house.total_earned_money += 150

    def gaming(self):
        cprint('{} поиграл'.format(self.name), color='blue')
        self.fullness -= 10
        self.happiness += 20


class Wife(Person):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return 'Жена {}, счастья {}, сытость {}'.format(self.name, self.happiness, self.fullness)

    def act(self):
        # TODO: дублированный блок из act`а мужа
        if self.house.dirty >= 90:
            self.happiness -= 10
        if self.happiness < 10 or self.fullness < 0:
            cprint('Жена {} умерла...'.format(self.name), color='red')  # TODO: Отличие в 2х словах в выводе.
            return

        # TODO: нам нужно больше рандома в действиях жены. Тогда убораться она будет не сразу как только наступило 100+
        #  а как пришло в голову. Сейчас у нее оптимальный алгоритм, поэтому семья сыта и счастлива.
        if self.fullness <= 30:
            self.eat()
        elif self.house.food <= 40:
            self.shopping()
        elif self.house.dirty >= 100:
            self.clean_house()
        elif self.happiness <= 30:
            self.buy_fur_coat()
        else:
            self.clean_house()

    # TODO: это уже не 7ой модуль. Здесь будет 2 взрослых, 1 ребенок и Кот.
    #  Если не делать проверки вида "если ли деньги на покупки" - у нас будут отрицательные значения.
    def shopping(self):
        cprint('{} купила еды домой'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.food += 50
        self.house.money -= 50

    def buy_fur_coat(self):
        cprint('{} купила шубу'.format(self.name), color='blue')
        self.happiness += 60
        self.fullness -= 10
        # TODO: жена может купить шубу и оставить отрицательный баланс (кредиты по условию задачи не выдаются)
        self.house.money -= 350
        self.house.total_bought_coat += 1

    def clean_house(self):
        cprint('{} сделала уборку в доме'.format(self.name), color='blue')
        # TODO: можно применить тернарный оператор условия
        if self.house.dirty > 100:
            self.house.dirty -= 100
        else:
            self.house.dirty -= self.house.dirty
        self.fullness -= 10


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    # TODO: пусть act() возвращает True - если все ок, и False - если человек умер.
    home.act()
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

cprint('Всего заработано денег: {}, всего съедено еды: {}, куплено шуб: {}'.format(home.total_earned_money,
                                                                                   home.total_eaten_food,
                                                                                   home.total_bought_coats)
       , color='cyan')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
