# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1200, 600)

for num_line in range(0, sd.resolution[1], 50):
    sd.line(sd.get_point(0, num_line), sd.get_point(sd.resolution[0], num_line), sd.COLOR_RED, 1)
    for num_line_ver in range(num_line % 100, sd.resolution[0], 100):
        sd.line(sd.get_point(num_line_ver, num_line), sd.get_point(num_line_ver, num_line + 50), sd.COLOR_RED, 1)

sd.pause()
