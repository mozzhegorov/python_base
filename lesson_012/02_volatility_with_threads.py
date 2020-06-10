# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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

import os
from glob import glob as get_files_list
from operator import itemgetter
from threading import Thread

from python_snippets.utils import time_track

zero_tickers = []
nonzero_tickers_list = []

# def get_files_list(folder):
#     folder = folder.split('/')[0]
#     file_list = []
#     for _, _, filenames in os.walk(folder):
#         for file in filenames:
#             filename = os.path.normpath(os.path.join(folder, file))
#             file_list.append(filename)
#     return file_list


def counting_volatility(ticker_prices):
    max_price = max(ticker_prices)
    min_price = min(ticker_prices)
    ave_price = (max_price + min_price) / 2
    volatility = (max_price - min_price) / ave_price * 100
    return volatility


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


class ParsingTicker(Thread):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = filename
        self.volatility = 0
        self.tickers_name = 0

    def run(self):
        with open(self.file, mode='r', encoding='utf8', buffering=1) as file:
            ticker_prices = get_prices_list(file)
            self.volatility = counting_volatility(ticker_prices)
            self.tickers_name = os.path.basename(self.file)
            self.tickers_name = self.tickers_name.split(sep='.')[0]
            # print(f'Читаем файл {self.tickers_name}')


@time_track
def main():
    files_list = get_files_list("trades/*.csv")
    tickers = [ParsingTicker(filename=file) for file in files_list]

    for ticker in tickers:
        ticker.start()

    for ticker in tickers:
        ticker.join()

    for ticker in tickers:
        if ticker.volatility == 0:
            zero_tickers.append(ticker.tickers_name)
        else:
            nonzero_tickers_list.append((ticker.tickers_name, ticker.volatility))

    nonzero_tickers_list.sort(key=itemgetter(1), reverse=True)
    print('Топ 3 лучших тикеров по волатильности')
    for ticker, vol in nonzero_tickers_list[0:3]:
        print(ticker, round(vol, 2))

    print('')
    print('Топ 3 худших тикеров по волатильности')
    for ticker, vol in nonzero_tickers_list[-1:-4:-1]:
        print(ticker, round(vol, 2))

    print('')
    print('Тикеры с нулевой волатильностью')
    for ticker in zero_tickers:
        print(ticker)


if __name__ == '__main__':
    main()
