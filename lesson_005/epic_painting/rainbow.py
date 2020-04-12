import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def draw_rainbow(x, y, radius, color_offset):
    # TODO: используйте срезы, чтобы склеить 2 половины rainbow_colors.
    #  [1,2,3, (режем) 4,5,6]     - режем в нужном месте
    #  [4,5,6, (клеем) 1,2,3]     - склеиваем половины поменяв местами.
    #   Ответ: не понимаю. Зачем это?

    for _ in range(color_offset):
        rainbow_colors.append(rainbow_colors[0])
        rainbow_colors.pop(0)

    for color in rainbow_colors:  # TODO: можно даже здесь подставить, не создавая доп.переменную
        radius += 4
        sd.circle(sd.get_point(x, y), radius, color, 4)

#  Пусть функция отрисовки радуги рисует радугу начиная с указанного в параметре номера цвета.
#  Мы добавим параметр "color_offset", который будет определяеть, начиная с какого цвета рисовать радугу.
#  Допустим color_offset=0, тогда радуга: красный, оранжевый, желает, ..., феолетовый;
#           color_offset=1, тогда радуга: оранжевый, желтый,..., феолетовый, красный (циклический сдвиг на 1 цвет);
#           color_offset=2, тогда радуга: желтый, ..., феолетовый, красный, оранжевый (циклический сдвиг на 1 цвет);
#  .
#  Нам нужно, чтобы был метод draw_rainbow(), который рисует всю радугу. Целиком. Метод принимает следующие
#  параметры:
#   1. x, y - где рисовать радугу;
#   2. radius - радиус минимального кольца цвета;
#   3. color_offset - начиная с какого цвета рисовать радугу.
#  .
#  Пример вызова метода:
#       draw_rainbow(x=100, y=500, radius=50, color_offset=0)   # красный,оранжевый,...,феолетовый;
#       draw_rainbow(x=100, y=500, radius=50, color_offset=1)   # оранжевый,..., феолетовый, красный
#       draw_rainbow(x=100, y=500, radius=50, color_offset=6)   # феолетовый, красный, оранжевый,...
