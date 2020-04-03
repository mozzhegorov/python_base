# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BRICK_WIDTH = 100
BRICK_HEIGHT = 50
x_offset = BRICK_WIDTH // 2


sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)

for brick_bottom_y in range(0, SCREEN_HEIGHT + 1, BRICK_HEIGHT):
    #  Тернарный оператор условия.
    #  Если if|else нужен только для того, чтобы прибавить/отнять какое-то число от исходного, то можно
    #  использовать тернальный оператор if|else. Пример:
    #               if some_condition:
    #                   a = 100
    #               else:                       			 # было
    #                   a = 200.
    #  .
    #               a = 100 if some_condition else 200       # стало
    #  .              ↑  ↑                          ↑
    #  Аналогично и +=, *=, -=, /=:
    #               a *= 4 if some_condition_2 else 2        # если ДА - умножим в 4 раза, если НЕТ - в 2 раза
    #  .               ↑ ↑                          ↑

    offset = x_offset if brick_bottom_y % (BRICK_HEIGHT * 2) else 0

    for brick_bottom_x in range(offset, SCREEN_WIDTH + 1, BRICK_WIDTH):
        sd.rectangle(sd.get_point(brick_bottom_x, brick_bottom_y),
                     sd.get_point(brick_bottom_x + BRICK_WIDTH, brick_bottom_y + BRICK_HEIGHT),
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

# зачет!