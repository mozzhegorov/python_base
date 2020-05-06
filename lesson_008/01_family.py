# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, choice

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

FOOD = 'food'
CATS_FOOD = 'cats_food'


class House:

    def __init__(self):
        self.money = 100
        self.dirty = 0

        self.icebox = {
            FOOD: 50,
            CATS_FOOD: 30
        }

        self.total = {
            'money': 0,
            FOOD: 0,
            CATS_FOOD: 0,
            'coats': 0
        }

    def __str__(self):
        return 'В доме еды {}, еды кошака {}, денег {}, грязи {}'.format(self.icebox[FOOD],
                                                                         self.icebox[CATS_FOOD],
                                                                         self.money,
                                                                         self.dirty)

    def act(self):
        self.dirty += 5


class Creature:

    def __init__(self, name, house, gluttony, type_food, metabolism=1, init_fullness=30):
        self.name = name
        self.house = house
        self.fullness = init_fullness
        self.gluttony = gluttony
        self.type_food = type_food
        self.metabolism = metabolism

    def eat(self):
        if self.house.icebox[self.type_food] > self.gluttony:
            self.fullness += self.gluttony * self.metabolism - 5
            self.house.icebox[self.type_food] -= self.gluttony
            self.house.total[self.type_food] += self.gluttony
            cprint('{} поел(а)'.format(self.name), color='blue')
            return True
        else:
            self.fullness -= 5
            cprint('{} хотел поесть, но нет еды'.format(self.name), color='red')
            return False

    def is_alive(self):
        if self.fullness < 0:
            cprint('Перс {} умер...'.format(self.name), color='red')
            return False
        return True


class Person(Creature):

    def __init__(self, name, house, gluttony=20):
        super().__init__(name=name, house=house, gluttony=gluttony, type_food=FOOD)
        self.happiness = 100

    def __str__(self):
        return ', счастья {}, сытость {}'.format(self.happiness, self.fullness)

    def caress_cat(self):
        self.fullness -= 10
        self.happiness += 5

    def act(self):
        if self.house.dirty >= 90:
            self.happiness -= 10
        #  код выполняется слева направо. Если первое условие будет нарушено - второе не будет проверяться.
        #  Нам лучше проверять сначала "not super().is_alive()", а потом "уровень счастья".
        #  .
        #  Почему?
        #  В данном случае это не влечет за собой последствий никаких. Но часто условия строят таким образом:
        #       if my_object is not None and my_object.my_field > 100500
        #  .
        #  Если в условии выше поменять местами условие, то в случае, когда my_object будет None, "my_object.my_field"
        #  попытается обратиться к полю .my_field у None. Т.е. в этом случае порядок важен.
        #  .
        #  Вернемся к нашим делам. У нас внутри "super().is_alive()" может быть спрятана подобная операция сравнения,
        #  которая не позволяет обращаться к полям, которых нет. Т.е. еще раз: в данном случае, это не критично, но
        #  лучше вырабатывать в себе привычку "что порядок условий важен", условие родителя может быть важнее.
        if not super().is_alive() or self.happiness < 10:
            cprint('Перс {} умер...'.format(self.name), color='red')
            return False
        return True


class Husband(Person):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, gluttony=20)

    def __str__(self):
        return 'Муж {}'.format(self.name) + super().__str__()

    def act(self):
        if not super().act():
            return False

        if self.fullness <= 30:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif self.happiness <= 30:
            self.gaming()
        else:
            choice([self.work, self.gaming])()
        return True

    def work(self):
        cprint('{} поработал'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.money += 150
        self.house.total['money'] += 150

    def gaming(self):
        cprint('{} поиграл'.format(self.name), color='blue')
        self.fullness -= 10
        self.happiness += 20


class Wife(Person):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, gluttony=20)

    def __str__(self):
        return 'Жена {}, счастья {}, сытость {}'.format(self.name, self.happiness, self.fullness)

    def act(self):
        if not super().act():
            return False

        if self.fullness <= 30:
            super().eat()
        elif self.house.icebox[FOOD] <= 40:
            self.shopping()
        elif self.happiness <= 30:
            self.buy_fur_coat()
        else:
            choice([self.clean_house,
                    self.eat,
                    self.eat,
                    self.shopping,
                    self.shopping])()
        return True

    def shopping(self):
        if self.house.money > 50:
            cprint('{} купила еды домой'.format(self.name), color='blue')
            self.fullness -= 10
            self.house.icebox[FOOD] += 50
            self.house.money -= 50
            return True
        else:
            cprint('{} хотела купить еды, но денег нет...'.format(self.name), color='red')
            self.fullness -= 5
            return False

    def buy_cats_food(self):
        if self.house.money > 50:
            cprint('{} купила еды для кота'.format(self.name), color='blue')
            self.house.cats_food += 50
            self.house.money -= 50
            self.fullness -= 10
            return True
        else:
            self.fullness -= 5
            return False

    def buy_fur_coat(self):
        if self.house.money > 350:
            cprint('{} купила шубу'.format(self.name), color='blue')
            self.happiness += 60
            self.fullness -= 10
            self.house.money -= 350
            self.house.total['coats'] += 1
            return True
        else:
            cprint('{} хотела купить шубу, но денег не хватило'.format(self.name), color='red')
            self.fullness -= 5
            return False

    def clean_house(self):
        cprint('{} сделала уборку в доме'.format(self.name), color='blue')
        self.fullness -= 20
        self.house.dirty -= 100 if self.house.dirty > 100 else self.house.dirty


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.act()
    # print(serge.act())
    # print(masha.act())
    if not (serge.act() and masha.act()):
        break
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

cprint('''Всего заработано денег: {}, 
всего съедено еды: {}, 
кошачьей еды {}, 
куплено шуб: {}'''.format(home.total['money'],
                          home.total[FOOD],
                          home.total[CATS_FOOD],
                          home.total['coats'])
       , color='cyan')


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

#  Общий класс с Cat.
#  Вообще с котом вы способны на большее. Посмотрите сколько методов пришлось для Кота скопировать. Почему? Потому что
#  у него не общего класс с Мужем, Женой и Ребенком. Почему? Потому у них общий родитель - Human, а кот это не человек.
#  Как быть? Сделать еще один класс. Как вы думаете что между ними общего, если на секундочку
#  забыть, что они живут в одном доме. Что общего между кошкой, собакой, Человеком?
#  Какие методы можно было вынести в этот класс? (их немного, но вынести можно)
#  .
#  Примечание: чтобы проделать такой фокус, в классе Дом лучше вместо полей "кошачья еда" и "человеческая еда"
#  ввести поле "холодильник", которое может быть словарем с 2 ключами: "кошачья еда" и ...;
#  Так же лучше создать глобальные, вне классов, константы CAT_FOOD = 'cat' и ... Что будут играть роль ключей в этом
#  холодильнике. При создании объекта Cat конструктор класса будет вызывать конструктор Общего класса, который будет
#  принимать на вход "тип пищи", который кушает создаваемый объект.
#  .
#  А в методе eat() просто будет по умолчанию брать "тип пищи" из холодильника и отниматься от нужной пищи.
#  .
#  Примечание: помните, что в общем классе мы можем реализовать метод, допустим, is_alive(), который будет проверять
#  только уровень еды (т.к. для кошки уровень счастья не нужен). В классе кошики перегружать is_alive тогда не нужно,
#  его достаточно. А в классе Человек, мы можем использовать is_alive родителя и дополнить его проверкой на уровень
#  счастья.
#  Т.е. сейчас наша главная задача при проектировании классов: сделать так, чтобы все общие часть попали в родителей.
class Cat(Creature):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, gluttony=10, metabolism=2, type_food=CATS_FOOD)

    def act(self):
        if not super().is_alive():
            return False
        if self.fullness < 10:
            self.eat()
        else:
            choice(self.eat, self.sleep, self.soil)()
        return True

    def sleep(self):
        self.fullness -= 10
        return True

    def soil(self):
        self.fullness -= 10
        self.house.dirty += 5
        return True


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

# TODO: вот с этим еще надо разобраться. При запуске программа спустя первую симуляцию выкинет эксепшн.
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
