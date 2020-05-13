# -*- coding: utf-8 -*-

from termcolor import cprint
from math import exp
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
COATS = 'coats'
MONEY = 'money'


class House:

    def __init__(self):
        self.money = 100
        self.dirty = 0

        self.icebox = {
            FOOD: 80,
            CATS_FOOD: 30
        }

        self.total = {
            MONEY: 0,
            FOOD: 0,
            COATS: 0,
            CATS_FOOD: 0
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
            # cprint('{} поел(а)'.format(self.name), color='blue')
            return True
        else:
            self.fullness -= 5
            # cprint('{} хотел поесть, но нет еды'.format(self.name), color='red')
            return False

    def is_alive(self):
        if self.fullness < 0:
            # cprint('Перс {} умер...'.format(self.name), color='red')
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
        if not super().is_alive() or self.happiness < 10:
            # cprint('Перс {} умер...'.format(self.name), color='red')
            return False
        return True


class Husband(Person):

    def __init__(self, name, house, sallory):
        super().__init__(name=name, house=house, gluttony=20)
        self.sallory = sallory

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
        # cprint('{} поработал'.format(self.name), color='blue')
        self.fullness -= 10
        self.house.money += self.sallory
        self.house.total[MONEY] += self.sallory

    def gaming(self):
        # cprint('{} поиграл'.format(self.name), color='blue')
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

        if self.fullness <= 40:
            super().eat()
        elif self.house.icebox[FOOD] <= 80:
            self.shopping()
        elif self.house.icebox[CATS_FOOD] <= 20:
            self.buy_cats_food()
        elif self.house.dirty > 80:
            self.clean_house()
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
        if self.house.money > 100:
            # cprint('{} купила еды домой'.format(self.name), color='blue')
            self.fullness -= 10
            self.house.icebox[FOOD] += self.house.money // 2
            self.house.money //= 2
            return True
        else:
            # cprint('{} хотела купить еды, но денег нет...'.format(self.name), color='red')
            self.fullness -= 5
            return False

    def buy_cats_food(self):
        if self.house.money > 50:
            # cprint('{} купила еды для кота'.format(self.name), color='blue')
            self.house.icebox[CATS_FOOD] += self.house.money // 2
            self.house.money //= 2
            self.fullness -= 10
            return True
        else:
            self.fullness -= 5
            return False

    def buy_fur_coat(self):
        if self.house.money > 350:
            # cprint('{} купила шубу'.format(self.name), color='blue')
            self.happiness += 60
            self.fullness -= 10
            self.house.money -= 350
            self.house.total[COATS] += 1
            return True
        else:
            # cprint('{} хотела купить шубу, но денег не хватило'.format(self.name), color='red')
            self.fullness -= 5
            return False

    def clean_house(self):
        # cprint('{} сделала уборку в доме'.format(self.name), color='blue')
        self.fullness -= 20
        self.house.dirty -= 100 if self.house.dirty > 100 else self.house.dirty


class Cat(Creature):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, gluttony=10, metabolism=2, type_food=CATS_FOOD)

    def __str__(self):
        return 'Котик {} сытость {}'.format(self.name, self.fullness)

    def act(self):
        if not super().is_alive():
            return False
        if self.fullness < 20:
            self.eat()
        else:
            choice([self.eat, self.sleep, self.soil])()
        return True

    def sleep(self):
        self.fullness -= 10
        return True

    def soil(self):
        self.fullness -= 10
        self.house.dirty += 5
        return True


class Child(Person):

    def __init__(self, name, house):
        super().__init__(name=name, house=house, gluttony=10)

    def __str__(self):
        return 'Ребенок {}'.format(self.name) + super().__str__()

    def act(self):
        if not super().act():
            return False
        if self.fullness < 20:
            self.eat()
        else:
            choice([self.eat, self.sleep, self.sleep])()
        return True

    def sleep(self):
        self.fullness -= 10


class Experiment:

    def __init__(self, childs, cats, sallory, freq_money_collapse, freq_food_collapse, exp_quantity):
        self.good_experiments = 0
        self.num_childs = childs
        self.num_cats = cats
        self.sallory = sallory
        self.freq_money_collapse = freq_money_collapse
        self.freq_food_collapse = freq_food_collapse
        self.exp_quantity = exp_quantity
        self.quan_food_collapse = 0
        self.quan_money_collapse = 0
        self.total_days = 0

    def do_experiment(self):

        self.home = House()
        self.serge = Husband(name='Сережа', house=self.home, sallory=sallory)
        self.masha = Wife(name='Маша', house=self.home)
        self.cats = []
        self.childs = []
        child_names = ['Коля', 'Вася', 'Дима', 'Женя', 'Саша', 'Андрей']
        cat_names = ['Муся', 'Пушок', 'Мурзик', 'Васька', 'Вискас']
        for i in range(self.num_childs):
            self.childs.append(Child(name=choice(child_names), house=self.home))
            child_names.remove(self.childs[i].name)

        for i in range(self.num_cats):
            self.cats.append(Cat(name=choice(cat_names), house=self.home))
            cat_names.remove(self.cats[i].name)

        for day in range(365):
            # cprint('================== День {} =================='.format(day), color='red')
            self.home.act()
            self.total_days += 1

            # Подкидываем монетку с вероятностью 1/365*(частота коллапсов)
            if self.freq_money_collapse != 0 and randint(1, 365 // self.freq_money_collapse) == 1:
                self.home.money %= 2
                self.quan_money_collapse += 1
                # cprint('Пропала половина денег', color='red')

            if self.freq_food_collapse != 0 and randint(1, 365 // self.freq_food_collapse) == 1:
                self.home.icebox[FOOD] %= 2
                self.quan_food_collapse += 1
                # cprint('Пропала половина еды', color='red')

            cats_alive = True
            for cat in self.cats:
                cats_alive &= cat.act()
                if not cats_alive:
                    break

            childs_alive = True
            for child in self.childs:
                childs_alive &= child.act()
                if not childs_alive:
                    break

            if not all([self.serge.act(), self.masha.act(), cats_alive, childs_alive]):
                return 0

        #     cprint(self.home, color='cyan')
        #     cprint(self.serge, color='cyan')
        #     cprint(self.masha, color='cyan')
        #     for child in self.childs:
        #         cprint(child, color='cyan')
        #     for cat in self.cats:
        #         cprint(cat, color='cyan')
        #
        # cprint('''Всего заработано денег: {},\n всего съедено еды: {},\n куплено шуб: {}'''
        #        .format(self.home.total[MONEY],
        #                self.home.total[FOOD],
        #                self.home.total[COATS]), color='cyan')
        return 1

    def counting_good(self):
        for _ in range(self.exp_quantity):
            self.good_experiments += self.do_experiment()
        self.sub_factor = (self.num_childs * 100 + self.num_cats * 100) / self.sallory + \
                          (self.freq_food_collapse + self.freq_money_collapse) / 10
        print(f'{self.good_experiments} / {self.exp_quantity}')
        if self.good_experiments > 0:
            self.factor = (exp((self.good_experiments / self.exp_quantity)*10 - 10) +
                           self.total_days / (365 * self.exp_quantity)) * \
                          self.sub_factor / 2
        else:
            self.factor = -1 * self.total_days / self.sub_factor / 100

    def __lt__(self, other):
        return self.factor < other.factor

    def __str__(self):
        return f'''
Данные эксперимента: 
количество детей {self.num_childs}, 
количество котов {self.num_cats},
сумма зарплаты {self.sallory},
частота пропажи еды (раз в год) {self.freq_food_collapse},
частота пропажи денег (раз в год) {self.freq_money_collapse}, 
количество хороших экспериментов {self.good_experiments} / {self.exp_quantity},
соотношение хороших экспериментов {self.good_experiments / self.exp_quantity}, 
количество пропаданий еды в среднем {self.quan_food_collapse/self.exp_quantity:.2f},
количество пропаданий денег в среднем {self.quan_money_collapse/self.exp_quantity:.2f},
вес параметров {self.sub_factor:.2f},
вес эксперимента {self.factor:.2f}
'''


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


# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.act()
#     # print(serge.act())
#     # print(masha.act())
#     if not (serge.act() and masha.act()):
#         break
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#
# cprint('''Всего заработано денег: {},
# всего съедено еды: {},
# куплено шуб: {}'''.format(home.total[MONEY],
#                           home.total[FOOD],
#                           home.total[COATS])
#        , color='cyan')

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

exp_list = []

exp_options = {
    'CATS_MAX': 5,
    'CHILDS_MAX': 5,
    'SALLORY_MIN': 150,
    'SALLORY_MAX': 500,
    'SALLORY_STEP': 50,
    'MONEY_COLLAPSE': 5,
    'FOOD_COLLAPSE': 5,
    'QUANTITY': 5
}

# Считаем количество вариантов
quantity_of_experiments = (exp_options['CATS_MAX'] - 1) * \
                          (exp_options['CHILDS_MAX'] - 1) * \
                          ((exp_options['SALLORY_MAX'] - exp_options['SALLORY_MIN']) //
                           exp_options['SALLORY_STEP'] + 1) * \
                          (exp_options['MONEY_COLLAPSE'] - 1) * \
                          (exp_options['FOOD_COLLAPSE'] - 1)

num_of_experiment = 0

for cats_num in range(1, exp_options['CATS_MAX']):
    for childs_num in range(1, exp_options['CHILDS_MAX']):
        for sallory in range(exp_options['SALLORY_MIN'], exp_options['SALLORY_MAX'] + 1, exp_options['SALLORY_STEP']):
            for money_collapse_per_year in range(1, exp_options['MONEY_COLLAPSE']):
                for food_collapse_per_year in range(1, exp_options['FOOD_COLLAPSE']):
                    experiment_1 = Experiment(childs=childs_num,
                                              cats=cats_num,
                                              sallory=sallory,
                                              freq_money_collapse=money_collapse_per_year,
                                              freq_food_collapse=food_collapse_per_year,
                                              exp_quantity=exp_options['QUANTITY'])
                    experiment_1.counting_good()
                    exp_list.append(experiment_1)
                    num_of_experiment += 1
                    print(f'Прогресс: {num_of_experiment} / {quantity_of_experiments}')

exp_list.sort(reverse=True)
print(f'''
Топ 5 лучших экспериментов: 
1 - {exp_list[0]} 
2 - {exp_list[1]} 
3 - {exp_list[2]}
4 - {exp_list[3]}
5 - {exp_list[4]}''')


print(f'''
Топ 5 худших экспериментов: 
1 - {exp_list[-1]} 
2 - {exp_list[-2]} 
3 - {exp_list[-3]}
4 - {exp_list[-4]}
5 - {exp_list[-5]}''')

#  Класс Эксперимент.
#  Сделайте небольшой класс Experiment.
#  В конструкторе будут все поля: число людей, кошек, ЗП, частота пропадания еды и денег, число повторений эксперимента, число удачных повторений.
#  Так же нужно будет перегрузить оператор сравнения - __lt__.
#  .
#  Запускаем несколько вложенных циклов (по ЗП, кол-во кошек и т.п.), перебираем разные наборы
#  параметров. Проводим симуляции, результаты сохраняем в объекты Experiment().
#  Все результаты сохраняются в список Experiment`ов.
#  Перегрузка оператора __lt__ позволит нам отсортировать список стандартной функцией
#  sorted(my_list) и взять срез лучших и худших 5 примеров.
#  .
#  Далее, перегрузив метод __str__ у Experiment мы сможем печатать информацию об экспериментах в цикле, не
#  зная ничего о его полях, логика будет инкапсулировано в класс Эксперимент. Т.е. 1 раз написали, а дальше
#  используем, и не приходится каждый раз вспоминать, какое поле должно быть больше, меньше или
#  равно нулю.
#  .
#  p.s. так же можно добавить поле "число повторений". Чем больше больше повторений, тем более
#  достоверны результаты эксперимента.


#  Коэффициент. Вес эксперимента.
#  У класса Experiment нужно добавить ф-цию "отдай вес". Вес эксперимента, т.е. насколько он,
#  скажем так, "крут" (т.е. эксперимент с 1 человеком, ЗП 10000, и 0 котами нас не слишком
#  интересует, поэтому его вес должен быть низкий; а вот случай, где 3 человека и 4 кота
#  выживают на 200 рублей - для нас интересен (конечно, если он успешен)).
#  .
#  Это нам пригодится для сравнения Экспериментов между собой. Мы можем ввести "веса" и сранивать этим результат, и
#  определить какой наиболее сторгий набор параметров позволит нам прокормить как можно больше котов.
#  .
#  Пример как посчитать вес:
#     вес_эксперимента = (число_успешных_попыток_эксперимента / (общее_число попыток + 3))
#                        * (число_пропаж_еды / 5)
#                        * (число_пропаж_денег / 7)
#                        * (число_человек * 30 + число_котов * 20) / ЗП
#  Посчитанный вес будет отражать ценность данного эксперимента. И будет учитывать все параметры.
#  Я написал приблизительную формулу. Вероятно, вы можете ее уточнить, т.к. например понимаете
#  что какой-то из параметров доментирует над другими.
#  .
#  Наша задача: определить эксперитмен, отражающий самый-самый экстремальный способ выживания семьи.
#  .
#  Основной плюс: мы используем средства питона,
#  1. перегрузив __lt__ может использовать sort() + срезы для получения лучших/худших;
#  2. перегрузив __str__ можем получать инфу об эксперименте не вдаваясь в то, какие поля у эксперимента.
