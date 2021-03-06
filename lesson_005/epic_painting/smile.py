import simple_draw as sd


def draw_smile(x, y, color):
    sd.ellipse(sd.get_point(x - 50, y - 50), sd.get_point(x + 50, y + 20), color, 2)
    sd.line(sd.get_point(x - 10, y - 30), sd.get_point(x + 10, y - 30), color, 2)
    sd.line(sd.get_point(x - 10, y - 30), sd.get_point(x - 20, y - 20), color, 2)
    sd.line(sd.get_point(x + 20, y - 20), sd.get_point(x + 10, y - 30), color, 2)
    sd.circle(sd.get_point(x + 15, y), 9, color, 1)
    sd.circle(sd.get_point(x - 15, y), 9, color, 1)


#  пусть 3 параметр будет флагом (переменной принимающей значение True или False), которая определяет открыт глаз
#  или нет. Снаружи мы в зависимости от положения счетчика мы будет держать глаз открытым или закрытым. В итоге
#  смайлик будет моргать.
#  .
#  f_blink можно назвать этот флаг.
def draw_eyes(x, y, color, animate_factor):
    sd.circle(sd.get_point(x + 15, y), 7, sd.background_color, 0)
    sd.circle(sd.get_point(x - 15, y), 7, sd.background_color, 0)
    y += 9
    animate_factor -= animate_factor // 18 * 18
    if animate_factor < 9:
        sd.circle(sd.get_point(x + 15, y - animate_factor), animate_factor, color, 0)
        sd.circle(sd.get_point(x - 15, y - animate_factor), animate_factor, color, 0)
    else:
        sd.circle(sd.get_point(x + 15, y + animate_factor - 18), 18 - animate_factor, color, 0)
        sd.circle(sd.get_point(x - 15, y + animate_factor - 18), 18 - animate_factor, color, 0)
