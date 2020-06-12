# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
import argparse

from PIL import Image, ImageDraw, ImageFont, ImageColor
from datetime import date


def make_ticket(fio, from_, to, ticket_date, save_to='ticket.png'):
    #  Отличие isinstance() от type()
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

    if isinstance(fio, str) and \
            isinstance(from_, str) and \
            isinstance(to, str) and \
            isinstance(ticket_date, date) and \
            len(fio.split()) > 0:
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
    draw.text((285, 260), f'{ticket_date.day:02d}.{ticket_date.month:02d}', fill=ImageColor.colormap['black'], font=font)

    im.save(os.path.join('images', save_to))
    im.show()


# make_ticket('Денис Мозжегоров', 'Земля', 'Луна', date_type(2005, 5, 6))

parser = argparse.ArgumentParser(description='Get ticket')

parser.add_argument('--fio', action='store', dest='fio', type=str, required=True)
parser.add_argument('--from_', action='store', dest='from_', type=str, required=True)
parser.add_argument('--to', action='store', dest='to', type=str, required=True)
parser.add_argument('--date', action='store', dest='date', type=str, required=True)
parser.add_argument('--save_to', action='store', dest='save_to', type=str, default='ticket.png')

args = parser.parse_args()

ticket_date = list(map(int, args.date.split(',')))
make_ticket(fio=args.fio.replace(',', ' '),
            from_=args.from_,
            to=args.to,
            ticket_date=date(*ticket_date),
            save_to=args.save_to)

# TODO: Работает скрипт с форматом строки типа
#       python 01_ticket.py --fio Денис,Мозжегоров --to Луна --from_ Земля --date 2020,5,5

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
