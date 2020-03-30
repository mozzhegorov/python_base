# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BRICK_WIDTH = 100
BRICK_HEIGHT = 50
x_offset = 50

sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)

for brick_bottom_y in range(0, SCREEN_HEIGHT + 1, BRICK_HEIGHT):
    for brick_bottom_x in range(0, SCREEN_WIDTH + 1, BRICK_WIDTH):
        if brick_bottom_y % (BRICK_HEIGHT * 2) == 0:
            offset = x_offset
        else:
            offset = 0
        sd.rectangle(sd.get_point(brick_bottom_x + offset, brick_bottom_y),
                     sd.get_point(brick_bottom_x + offset + BRICK_WIDTH, brick_bottom_y + BRICK_HEIGHT),
                     color=sd.COLOR_RED, width=1)
sd.pause()

#  элегантный способ, но не универсальный. Стоит изменить размер кирпича, допустим на 100 и 30 и стена поедет.

#  тут на плотно предстоит поработать)
#  Ввести константы ширина/высота экрана;
#  Ввести константы ширина/высота кирпичика;.
#  Задать размер полотна, используя контсанты sd.resolution = (ширина, высота);
#  Изменить циклы по y и x так, чтобы они использовали эти константы.
#  Добавить if между двумя циклами, чтобы определять x_offset (т.к. num_line % 100 не универсален, хотя крут)
#  Так же можно, желательно, заменить 2 вызова sd.line на 1 вызов sd.rectangle.
#  .
#  Какая выгода? Мы сможет контролировать размер стены и кирпича из одного места кода, и менять стиль стены 1 движением,
#  не залезая внутрь основного кода. Код будет более гибок. И в одном из следующих заданий его можно будет использовать
#  чтобы отрисовать небольшую стену "домика".
