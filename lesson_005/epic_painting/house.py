import simple_draw as sd


def build_wall(left_bottom=(0, 0), right_top=(100, 100), brick_height=10, brick_width=20, color=sd.COLOR_DARK_RED):
    x_offset = brick_width // 2

    for brick_bottom_y in range(left_bottom[1], right_top[1] + 1, brick_height):

        offset = x_offset if brick_bottom_y % (brick_height * 2) else 0
        offset += left_bottom[0]

        for brick_bottom_x in range(offset, right_top[0] + 1, brick_width):
            sd.rectangle(sd.get_point(brick_bottom_x, brick_bottom_y),
                         sd.get_point(brick_bottom_x + brick_width, brick_bottom_y + brick_height),
                         color=color, width=1)


#  убрать параметры, который мы не используем (т.е. убираем атавизмы, которые перекочивали вместе с ф-цией
#  "нарисовать треугольник".
#  Слить воедино ф-ции build_roof и draw_figure, т.к. ф-цию объявляют тогда, когда она вызывается во множестве мест.
#  Либо ф-ция должна делать какую-то определенную задачу (рисовать дом например).
#  Функция "нарисовать фигуру" рисует 1 вектор, причем вызов этой ф-ции занимает почти столько же, как и она сама.
def build_roof(start_point=sd.get_point(100, 100), length=50, color=sd.COLOR_YELLOW):
    for roof_length in range(length):
        vector_start_point = start_point
        for figure_angle in range(0, 240, 120):
            rib = sd.vector(start=vector_start_point,
                            angle=figure_angle,
                            length=roof_length,
                            color=color,
                            width=2)        # TODO: убрать ширину - ошибка с моей стороны. Поэтому восстановил ваш параметр)
            vector_start_point = rib
        sd.line(start_point, vector_start_point, color=color)


def build_window(left_bottom, right_top):
    sd.rectangle(sd.get_point(*left_bottom), sd.get_point(*right_top), color=sd.COLOR_WHITE)
    left_bottom = (left_bottom[0] + 5, left_bottom[1] + 5)
    right_top = (right_top[0] - 5, right_top[1] - 5)
    sd.rectangle(sd.get_point(*left_bottom), sd.get_point(*right_top))

    start_line = ((left_bottom[0] + right_top[0]) // 2, left_bottom[1])
    end_line = ((left_bottom[0] + right_top[0]) // 2, right_top[1])
    sd.line(sd.get_point(*start_line), sd.get_point(*end_line), width=2, color=sd.COLOR_WHITE)

    start_line = (left_bottom[0], (left_bottom[1] + right_top[1]) // 2)
    end_line = (right_top[0], (left_bottom[1] + right_top[1]) // 2)
    sd.line(sd.get_point(*start_line), sd.get_point(*end_line), width=2, color=sd.COLOR_WHITE)
