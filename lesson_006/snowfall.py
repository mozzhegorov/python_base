import simple_draw as sd

snowflake_dict = []


def get_snowflake(branch_min=10,
                  branch_max=100,
                  y_min=0,
                  y_max=sd.resolution[1],
                  x_min=0,
                  x_max=sd.resolution[0]):
    return {'branch_len': sd.random_number(branch_min, branch_max),  # Раздаем длины лучей,
            'x': sd.random_number(x_min, x_max),  # а также положения по оси У
            'y': sd.random_number(y_min, y_max),
            'moving': 1}  # флаг активности


def snowflake_dict_gen(N=10,
                       left_bottom=(0, 0),
                       right_top=(sd.resolution[0], sd.resolution[1]),
                       min_branch_len=2,
                       max_branch_len=7):
    for _ in range(N):
        # TODO: указание глобальных переменных происходит раньше всех остальных операций
        global snowflake_dict
        snowflake_dict.append(get_snowflake(branch_min=min_branch_len,
                                            branch_max=max_branch_len,
                                            y_min=sd.random_number(left_bottom[1], right_top[1]),
                                            y_max=right_top[1],
                                            x_min=left_bottom[0],
                                            x_max=right_top[0]))


def draw_snowflakes(color):
    for snowflake in snowflake_dict:
        sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']),
                     length=snowflake['branch_len'],
                     color=color)

# TODO: что делает эта ф-ция? Пожалуйста добавьте комменатрии на каждую строку
def get_fallen_snowflakes():
    for number, snowflake in enumerate(snowflake_dict):
        if snowflake['y'] < snowflake['branch_len']:
            print(number)
            return number


def move_snowflakes(speed=5):
    for snowflake in snowflake_dict:
        snowflake['y'] -= speed
        snowflake['x'] += sd.random_number(-5, 5)

# TODO: по заданию здесь должна быть еще одна ф-ция. И ее нужно будет использовать в вечном цикле, а то она там сейчас
#  раписана, вместо того, чтобы бы здесь)