# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os

from PIL import Image, ImageDraw, ImageFont, ImageColor
from datetime import date as date_type      # TODO: лучше оставить date - в большинстве кода оставляют неизменным.


def make_ticket(fio, from_, to, date):
    # TODO: Отличие isinstance() от type()
    #  isinstance() поддерживает наследование. Для isinstance() экземпляр производного класса
    #  также является экземпляром базового класса. Для type() это не так:
    #  .
    #         class A (list):
    #            pass
    #  .
    #         a = A()
    #         type(a) == list             # False
    #         type(a) == A                # True
    #         isinstance(a,A)             # True
    #         isinstance(a,list)          # True
    #  .
    #  Т.к. наледники обладают свойствами родителей (по крайней мере так должно быть в хорошем коде, за редкими
    #  исключениями), нам лучше использовать isinstance() вместо type()
    # Проверяем на корректность введенных данных
    if type(fio) is str and \
            type(from_) is str and \
            type(to) is str and \
            type(date) is date_type and \
            len(fio.split()) > 1:
        pass
    else:
        raise ValueError('Проверьте введенные данные')

    # TODO: 👍👍
    im = Image.open(os.path.join('images', 'ticket_template.png'), mode='r')
    font = ImageFont.truetype(font=os.path.join('images', 'Lucida Grande.ttf'), size=16)
    draw = ImageDraw.Draw(im)

    draw.text((45, 125), fio, fill=ImageColor.colormap['black'], font=font)
    draw.text((45, 195), from_, fill=ImageColor.colormap['black'], font=font)
    draw.text((45, 260), to, fill=ImageColor.colormap['black'], font=font)
    draw.text((285, 260), f'{date.day:02d}.{date.month:02d}', fill=ImageColor.colormap['black'], font=font)

    im.save(os.path.join('images', 'ticket.png'))
    im.show()


make_ticket('Мозжегоров Денис', 'Земля', 'Луна', date_type(2005, 5, 6))

# TODO: можно усложненную версию.
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
