import simple_draw as sd


def draw_smile(x, y, color):
    sd.ellipse(sd.get_point(x - 50, y - 50), sd.get_point(x + 50, y + 20), color, 2)
    sd.line(sd.get_point(x - 10, y - 30), sd.get_point(x + 10, y - 30), color, 2)
    sd.line(sd.get_point(x - 10, y - 30), sd.get_point(x - 20, y - 20), color, 2)
    sd.line(sd.get_point(x + 20, y - 20), sd.get_point(x + 10, y - 30), color, 2)
    sd.circle(sd.get_point(x + 15, y), 7, color, 1)
    sd.circle(sd.get_point(x - 15, y), 7, color, 1)


def draw_eyes(x, y, color, animate_factor):
    sd.circle(sd.get_point(x + 15, y), 6, sd.background_color, 0)
    sd.circle(sd.get_point(x - 15, y), 6, sd.background_color, 0)
    y += 7
    animate_factor -= animate_factor // 7 * 7
    print(animate_factor)
    sd.circle(sd.get_point(x + 15, y - animate_factor), animate_factor, color, 0)
    sd.circle(sd.get_point(x - 15, y - animate_factor), animate_factor, color, 0)
