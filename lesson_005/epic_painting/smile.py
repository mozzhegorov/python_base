import simple_draw as sd


def draw_smile(x, y, color):
    sd.ellipse(sd.get_point(x - 50, y - 50), sd.get_point(x + 50, y + 20), color, 2)
    sd.line(sd.get_point(x - 10, y - 30), sd.get_point(x + 10, y - 30), color, 2)
    sd.line(sd.get_point(x - 10, y - 30), sd.get_point(x - 20, y - 20), color, 2)
    sd.line(sd.get_point(x + 20, y - 20), sd.get_point(x + 10, y - 30), color, 2)
    sd.circle(sd.get_point(x + 15, y), 7, color, 1)
    sd.circle(sd.get_point(x - 15, y), 7, color, 1)
