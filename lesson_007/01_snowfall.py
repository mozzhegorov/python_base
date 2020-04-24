# -*- coding: utf-8 -*-

import simple_draw as sd

INIT_FLAKES = 20


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, y_min=0):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.random_number(y_min, sd.resolution[1])
        self.branch_len = sd.random_number(5, 15)
        self.speed = sd.random_number(3, 8)
        self.color = sd.COLOR_WHITE
        self.move_flag = True

    def to_up(self):
        self.y = sd.resolution[1]

    def clear_previous_picture(self):
        """
            Убираем предыдущую снежинку
        """
        sd.snowflake(center=sd.get_point(self.x, self.y),
                     length=self.branch_len,
                     color=sd.background_color)

    def move(self):
        """
            Двигаем снежинку вниз со скоростью  speed
        """
        if self.y > self.branch_len:
            self.y -= self.speed
            self.x += sd.random_number(-5, 5)

    def draw(self):
        """
            Рисуем снежинку на экране
        """
        sd.snowflake(center=sd.get_point(self.x, self.y),
                     length=self.branch_len,
                     color=self.color)

    def can_fall(self):
        """
            Определяем возможность снежинки двигаться вниз
        """
        return self.y > self.branch_len


# flake = Snowflake()
# while not sd.user_want_exit():
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)


def get_flakes(count=10):
    """
        Собираем первоначальный список снежинок
    """
    list_of_flakes = []
    for i in range(count):
        list_of_flakes.append(Snowflake())
    return list_of_flakes


def get_fallen_flakes(all_flakes):
    """
        выдает список номеров снежинок, которые вышли за границу экрана
    """
    num_of_fallen = 0
    for snowflake in all_flakes:
        if not snowflake.can_fall() and snowflake.move_flag:
            num_of_fallen += 1
            snowflake.move_flag = False
    return num_of_fallen


def append_flakes(count):
    """
        Добавляем снежинки
    """
    global flakes
    for _ in range(count):
        flakes.append(Snowflake(y_min=sd.resolution[1]))


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=INIT_FLAKES)  # создать список снежинок
while not sd.user_want_exit():
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху

    if len(flakes) > INIT_FLAKES * 5:
        flakes.pop(0)
    sd.sleep(0.1)

sd.pause()
