import simple_draw as sd


# Рсиуем кружок цветом фона и потом рисуем солнышко :)
def draw_animate_sun(x_center=100, y_center=100, radius=50, ray_len=80, ray_width=8, shift_angle=5):
    sd.circle(sd.get_point(x_center, y_center),
              radius=ray_len + 5,
              width=0,
              color=sd.background_color)
    sd.circle(sd.get_point(x_center, y_center), radius=radius, width=0)

    # Крутим лучиками
    for angle in range(shift_angle, shift_angle + 361, 60):
        # angle += animate_factor
        sd.vector(start=sd.get_point(x_center, y_center), angle=angle, width=ray_width, length=ray_len)

    #   внутри ф-ции animate_factor выполняет роль "угол поворота". Почему название animate_factor подходит лучше,
    #   чем например delta_angle?
    #   Ответ: назвал shift_angle  (сдвиг угла)