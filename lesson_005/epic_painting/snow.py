import simple_draw as sd


# TODO: пусть ф-ция возращает снежинку, а не добавляется в список.
#  Вместе snow_append будет get_snowflake.
def snow_append(_snowflake_params, branch_min=10, branch_max=100, y_min=0, y_max=sd.resolution[1], x_min=0,
                x_max=sd.resolution[0]):
    _snowflake_params.append({'branch_len': sd.random_number(branch_min, branch_max),  # Раздаем длины лучей,
                              'x': sd.random_number(x_min, x_max),  # а также положения по оси У
                              'y': sd.random_number(y_min, y_max),
                              'moving': 1})  # флаг активности


def snowflake_dict_gen(N=10, left_bottom=(0, 0), right_top=(100, 100), min_branch_len=2, max_branch_len=7):
    snowflake_dict = []
    for _ in range(N):
        snow_append(_snowflake_params=snowflake_dict,
                    branch_min=min_branch_len,
                    branch_max=max_branch_len,
                    y_min=left_bottom[1],
                    y_max=right_top[1],
                    x_min=left_bottom[0],
                    x_max=right_top[0]
                    )
    return snowflake_dict


def snowfall(N_init, snowflake_params=None, speed=2, left_bottom=(0, 0), right_top=(100, 100), min_branch_len=2,
             max_branch_len=7):
    if snowflake_params is None:
        snowflake_params = snowflake_dict_gen(10)
    for param_of_snowflake in snowflake_params:
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])
        # передвигаем и прячем снежинку только если снежинка имеет флаг активности
        if param_of_snowflake['moving'] == 1:
            if param_of_snowflake['y'] > speed + left_bottom[1]:
                sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.background_color)
                param_of_snowflake['y'] -= speed
                param_of_snowflake['x'] += sd.random_number(-5, 5)
            else:
                #  сделайте ф-цию. "вернуть снежинку", которая можно будет вызывать здесь и на 7ой строке,
                #  чтобы у нас не было дублирования кода.
                # Добавляем еще одну снежинку на верх
                snow_append(_snowflake_params=snowflake_params,
                            branch_min=min_branch_len,
                            branch_max=max_branch_len,
                            y_min=right_top[1],
                            y_max=right_top[1],
                            x_min=left_bottom[0],
                            x_max=right_top[0]
                            )
                # Убираем активность у старой снежинки
                param_of_snowflake['moving'] = 0

        #  цикл покраски снежинок в белый лучше вынести в отдельный цикл. Т.е. сначала все прячем+перемещаем.
        #  Потому у нас пустой экран. Потом красим белым.
        #  Зачем?
        #  Обратите внимание, что при пересечении снежинок у нас сейчас возникает перетирание веточек.
        #  Ответ: Не смог придумать ничего лучше как использовать перемнную активности для снежинки.
        #  В данном варианте решения добавляем еще одно снежинку и с ней работаем. Раньше снежинок было фиксированное
        #  количество, лишь менялись координаты, а старая (та что внизу) не перетиралась сама собой, но был баг.
        #  Теперь бага нет

        #  Ответ.
        #  Мой косяк, нужно было еще точнее формулировать. Речь шла только о падающих снежинках. Сугробу почти не помочь
        #  Текущий вариант "спасает" сугроб, но нужны доп.меры. Нужно добавить проверку, что число снежинок не превысило
        #  N * 5. И если превысило, то при добавлении новой снежинки (крайней), удалять самую старую (первую).
    for param_of_snowflake in snowflake_params:
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])
        # красим белым весь список снежинок, даже не активные
        sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.COLOR_WHITE)
        #  добавить "упавшие снежинки возвращать назад"
        # print(len(snowflake_params))

        # TODO:
        #  "len(snowflake_params) > 5 * N_init" - это условие
        #  snowflake_params.pop(0) - это действие.
        #  .
        #  Давайте сделаем из этого if-блок.
        can_i_del = len(snowflake_params) > 5 * N_init  # Проверяем сколько элеметнов там у нас
        # print(can_i_del)
        can_i_del and snowflake_params.pop(0)           # TODO: рабочая, но не очевидная запись. Повышает сложность чтение
        # Нашел такой крутой способ условия. В общем он удаляет первый
        # элемент. Вроде работает
