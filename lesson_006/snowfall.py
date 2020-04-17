import simple_draw as sd

snowflake_list = []
list_of_fallen = []     # TODO: убрать эту глобальную переменную (см. ниже)


def get_snowflake(branch_min=10,
                  branch_max=100,
                  y_min=0,
                  y_max=sd.resolution[1],
                  x_min=0,
                  x_max=sd.resolution[0]):
    """
        Создаем элемент для списка словарей параметров снежинок
    """
    return {'branch_len': sd.random_number(branch_min, branch_max),  # Раздаем длины лучей,
            'x': sd.random_number(x_min, x_max),  # а также положения по оси У
            'y': sd.random_number(y_min, y_max),
            'moving': 1}  # флаг активности


def snowflake_list_gen(N=10,
                       left_bottom=(0, 0),
                       right_top=(sd.resolution[0], sd.resolution[1]),
                       min_branch_len=15,
                       max_branch_len=30):
    """
        создает N снежинок
    """
    global snowflake_list
    for _ in range(N):
        snowflake_list.append(get_snowflake(branch_min=min_branch_len,
                                            branch_max=max_branch_len,
                                            y_min=sd.random_number(left_bottom[1], right_top[1]),
                                            y_max=right_top[1],
                                            x_min=left_bottom[0],
                                            x_max=right_top[0]))


def draw_snowflakes(color):
    """
        Рисуем все снежинки на экране
    """
    for snowflake in snowflake_list:
        sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']),
                     length=snowflake['branch_len'],
                     color=color)


def get_fallen_snowflakes():
    """
        выдает список номеров снежинок, которые вышли за границу экрана
    """
    # TODO: пусть этот список здесь и создается) Зачем он нам глобально? не зачем)
    global list_of_fallen
    for number, snowflake in enumerate(snowflake_list):
        if snowflake['y'] < snowflake['branch_len']:
            list_of_fallen.append(number)

    return list_of_fallen


def move_snowflakes(speed=5):
    """
        Двигаем снежинки вниз со скоростью  speed
    """
    for snowflake in snowflake_list:
        snowflake['y'] -= speed
        snowflake['x'] += sd.random_number(-5, 5)

# TODO: функция должна принимать на вход список индексов.
def delete_snowflake():
    """
        удаляет снежинки с номерами из списка
    """
    global list_of_fallen
    for del_item in list_of_fallen[::-1]:  # Удаляем в обратном порядке, чтобы не удалить не ту снежинку.
        snowflake_list.pop(del_item)        # TODO: Круто!) Именно то, что нужно)
    list_of_fallen.clear()
