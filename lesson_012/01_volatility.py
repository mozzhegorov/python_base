# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import os
from operator import itemgetter
#from utils import time_track       # TODO: pip install utils - поставил какую-то другую либу, в которой нет time_track. Какой модуль вы устанавливали?

zero_tickers = []
nonzero_tickers_list = []


def get_file_list(folder):
    file_list = []
    _, _, filenames = next(os.walk(folder))     # TODO: компактный вариант. Цикл мы используем лишь, чтобы он вызвал за нас next(). Итерация все равно 1.
    #for _, _, filenames in os.walk(folder):
    for file in filenames:
        filename = os.path.normpath(os.path.join(folder, file))
        file_list.append((filename, file))
    return file_list

# TODO: а еще вот это посмотрите:
#  https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory#comment25692343_3207973
#  Возможно решите избавиться от get_file_list в пользу словарного включения.

def counting_volatily(ticker_prices):
    max_price = max(ticker_prices)
    min_price = min(ticker_prices)
    ave_price = (max_price + min_price) / 2
    volatility = (max_price - min_price) / ave_price * 100
    return round(volatility, 2)     # TODO: лучше конечно округлять только при выводе


def get_prices_list(file):
    ticker_prices = []
    for string in file:
        price = string.split(sep=",")[2]
        try:
            price = float(price)
        except ValueError:
            continue
        except Exception as exc:
            print(exc)
            continue
        ticker_prices.append(price)
    return ticker_prices


class ParsingTicker:

    def __init__(self, filename, tickers_name):
        self.file = filename
        self.volatily = 0
        self.tickers_name = tickers_name

    def run(self):
        # TODO: Более "трушный" способ открытия файла: с использование with. В таком случае, если произойдет исключение
        #  оно будет выбрашено навер, как обычно, НО файл будет закрыт. Сейчас, при исключении, файл останется открытым
        file = open(self.file, mode='r', encoding='utf8', buffering=1)
        ticker_prices = get_prices_list(file)
        self.volatily = counting_volatily(ticker_prices)
        file.close()


#@time_track
def main():
    files_list = get_file_list(folder='trades')
    tickers = [ParsingTicker(filename=file[0], tickers_name=file[1]) for file in files_list]

    for ticker in tickers:
        ticker.run()
        if ticker.volatily == 0:
            zero_tickers.append(ticker.tickers_name)
        else:
            nonzero_tickers_list.append((ticker.tickers_name, ticker.volatily))

    nonzero_tickers_list.sort(key=itemgetter(1), reverse=True)
    print('Топ 3 лучших тикеров по волатильности')
    for ticker, vol in nonzero_tickers_list[0:3]:
        print(ticker, vol)

    print('')
    print('Топ 3 худших тикеров по волатильности')
    for ticker, vol in nonzero_tickers_list[-1:-4:-1]:
        print(ticker, vol)

    print('')
    print('Тикеры с нулевой волатильностью')
    for ticker in zero_tickers:
        print(ticker)


if __name__ == '__main__':
    main()
