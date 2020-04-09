import simple_draw as sd


def snowflake_dict_gen(N=10, left_bottom=(0, 0), right_top=(100, 100), max_branch_len=5):
    snowflake_dict = []
    for i in range(N):
        snowflake_dict.append({'branch_len': sd.random_number(3, max_branch_len),  # Раздаем длины лучей,
                               'x': sd.random_number(left_bottom[0], right_top[0]),  # а также положения по оси У
                               'y': sd.random_number(left_bottom[1], right_top[1]),
                               'moving': 1})
    return snowflake_dict


def snowfall(snowflake_params=None, speed=2, left_bottom=(0, 0), right_top=(100, 100), max_branch_len=5):
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
                # TODO: сделайте ф-цию. "вернуть снежинку", которая можно будет вызывать здесь и на 7ой строке,
                #  чтобы у нас не было дублирования кода.
                # Добавляем еще одну снежинку на верх
                snowflake_params.append({'branch_len': sd.random_number(2, max_branch_len),  # Раздаем длины лучей,
                                         'x': sd.random_number(left_bottom[0], right_top[0]),
                                         'y': right_top[1],
                                         'moving': 1})  # флаг активности
                # Убираем активность у старой снежинки
                param_of_snowflake['moving'] = 0

        # TODO: цикл покраски снежинок в белый лучше вынести в отдельный цикл. Т.е. сначала все прячем+перемещаем.
        #  Потому у нас пустой экран. Потом красим белым.
        #  Зачем?
        #  Обратите внимание, что при пересечении снежинок у нас сейчас возникает перетирание веточек.
        #  Ответ: Не смог придумать ничего лучше как использовать перемнную активности для снежинки.
        #  В данном варианте решения добавляем еще одно снежинку и с ней работаем. Раньше снежинок было фиксированное
        #  количество, лишь менялись координаты, а старая (та что внизу) не перетиралась сама собой, но был баг.
        #  Теперь бага нет

        # TODO: Ответ.
        #  Мой косяк, нужно было еще точнее формулировать. Речь шла только о падающих снежинках. Сугробу почти не помочь
        #  Текущий вариант "спасает" сугроб, но нужны доп.меры. Нужно добавить проверку, что число снежинок не превысило
        #  N * 5. И если превысило, то при добавлении новой снежинки (крайней), удалять самую старую (первую).
    for param_of_snowflake in snowflake_params:
        snowflake_center = sd.get_point(param_of_snowflake['x'], param_of_snowflake['y'])
        # красим белым весь список снежинок, даже не активные
        sd.snowflake(snowflake_center, param_of_snowflake['branch_len'], color=sd.COLOR_WHITE)
        #  добавить "упавшие снежинки возвращать назад"
