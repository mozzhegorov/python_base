import simple_draw as sd


def draw_rainbow(x, y, radius):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    for color in rainbow_colors:
        radius += 4
        sd.circle(sd.get_point(x, y), radius, color, 4)
