import simple_draw as sd


def draw_random_branches(start_point, angle=90, length=100):
    root_end = sd.vector(start_point, angle, length)
    if length < 10:
        return

    length *= .75

    angle += 30
    random_angle = 30 - sd.random_number(60, 140) / 100 * 30
    random_length = .75 - sd.random_number(80, 120) / 100 * .75
    draw_random_branches(root_end, angle=angle + random_angle, length=length + random_length)

    angle -= 60
    random_angle = 30 - sd.random_number(60, 140) / 100 * 30
    random_length = .75 - sd.random_number(80, 120) / 100 * .75
    draw_random_branches(root_end, angle=angle + random_angle, length=length + random_length)

