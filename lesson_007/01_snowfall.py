# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.resolution[1]
        self.branch_len = sd.random_number(5, 15)
        self.speed = 5
        self.color = sd.COLOR_WHITE

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
        return self.y > self.speed


flake = Snowflake()

while not sd.user_want_exit():
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    print(flake.can_fall())
    if not flake.can_fall():
        break
    sd.sleep(0.1)

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
