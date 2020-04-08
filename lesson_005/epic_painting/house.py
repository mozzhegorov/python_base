import simple_draw as sd


def draw_figure(figure_angle, start_point=sd.get_point(400, 400), angle=12, length=70, width=1):
    vector_start_point = start_point
    rib = sd.get_vector(start_point=vector_start_point,
                        angle=angle + figure_angle,
                        length=length,
                        width=width)
    rib.draw()
    return rib.end_point


def build_wall(left_bottom=(0, 0), right_top=(100, 100), brick_height=10, brick_width=20, color=sd.COLOR_DARK_RED):
    x_offset = brick_width // 2

    for brick_bottom_y in range(left_bottom[1], right_top[1] + 1, brick_height):

        offset = x_offset if brick_bottom_y % (brick_height * 2) else 0
        offset += left_bottom[0]

        for brick_bottom_x in range(offset, right_top[0] + 1, brick_width):
            sd.rectangle(sd.get_point(brick_bottom_x, brick_bottom_y),
                         sd.get_point(brick_bottom_x + brick_width, brick_bottom_y + brick_height),
                         color=color, width=1)


def build_roof(start_point=sd.get_point(100, 100), angle=0, length=50, width=1):
    vector_start_point = start_point
    for figure_angle in range(0, 240, 120):
        vector_start_point = draw_figure(width=width,
                                         figure_angle=figure_angle,
                                         start_point=vector_start_point,
                                         angle=angle,
                                         length=length)
    sd.line(start_point, vector_start_point, width=width, color=sd.COLOR_YELLOW)
