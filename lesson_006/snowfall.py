import simple_draw as sd

snowflake_list = []


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

# TODO: вот эта функция играет роль " создать_снежинки(N) - создает N снежинок"
def snowflake_list_gen(N=10,
                       left_bottom=(0, 0),
                       right_top=(sd.resolution[0], sd.resolution[1]),
                       min_branch_len=2,
                       max_branch_len=7):
    """
        Создаем список со снежинками
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

# TODO: из задания
#  "номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана".
def get_fallen_snowflakes():
    """
        получаем номер упавшей снежинки
    """
    for number, snowflake in enumerate(snowflake_list):
        if snowflake['y'] < snowflake['branch_len']:
            print(number)
            return number

    # TODO: ф-ция должна возвращать список упаших снежинок

def move_snowflakes(speed=5):
    """
        Двигаем снежинки вниз со скоростью  speed
    """
    for snowflake in snowflake_list:
        snowflake['y'] -= speed
        snowflake['x'] += sd.random_number(-5, 5)


# TODO: "удалить_снежинки(номера) - удаляет снежинки с номерами из списка"
def delete_snowflake(number):
    """
        Удаляем номер упавшей снежинки
    """
    snowflake_list.pop(number)

# TODO: эта ф-ция уменьшенная версия самой первой ф-ции. Эту функциюу удалить.
def create_snowflake():
    """
        Создаем новую снежинку
    """
    snowflake_list.append(get_snowflake(branch_min=15,
                                        branch_max=30,
                                        y_min=sd.resolution[1]))
