# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# for num_line in range(7):
#     start_x = 50 + num_line * 5
#     end_x = 350 + num_line * 5
#     sd.line(sd.get_point(start_x, 50), sd.get_point(end_x, 450), rainbow_colors[num_line], 5)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

radius = 400

for num_line in range(7):
    center_radius = radius + num_line * 4
    sd.circle(sd.get_point(-100, -100), center_radius, rainbow_colors[num_line], 4)


sd.pause()
