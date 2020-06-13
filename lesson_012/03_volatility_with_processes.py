# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
import multiprocessing
import os
from collections import defaultdict
from glob import glob as get_files_list
from operator import itemgetter
from threading import Thread

from funcy import chunks

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

#  имейте ввиду, что создавать сразу 100500 потоков (даже 100) на 4 ядерном процессор особого смысла
#  иметь не будет. Это непростая и большая тема, но кратко так:
#  1. Если задача требует много вычисление - важно количество физических ядер. И создание 100 потоков
#     не решит вопрос, т.к. у нас только 4 ядра. Это не наш случай, у нас простые вычисления;
#  2. Если задача требует много операций ввода/вывода, число потоков поможет, особенно если доступ
#     к разным источникам на разных дисках. Это уже ближе к нам, мы читаем файлы, как раз операции ввода.
#     НО. Созданы будут потоки. Все потоки будут исполнятся в 1 процессе с точки зрения ОС, т.е. это будет N потоков
#     внутри 1 потока с точки зрения ОС. Это обусловлено наличием GIL в Python;
#  3. Поэтому 2 варианта выше обычно запускают не на разных потоках, а на разных процессах.
#     Тогда каждый процесс будет своем ядре.
#  .
#  Зачем тогда потоки? Чаще нам достаточно мощностей 1 процесса, но хочется делать несколько небольших
#  дел одновременно: идет снег, мигает радуга, мигает смайлик) Странно было бы 1го крошечного элемента
#  GUI Телеграмма создавать отдельный процесс.
#  .
#  Важная мысль (продолжение пункт №2): Мы делали 1 вечный цикл и там все мультиплексировали. То же самое делает GIL.
#  .
#  Вот такие дела) Но это довольно грубое объяснение, хотя близкое к истине.
class ParsingTicker(multiprocessing.Process):

    def __init__(self, tickers_list, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tickers = tickers_list
        self.collector = collector

    def run(self):
        for ticker in self.tickers:
            with open(ticker, mode='r', encoding='utf8', buffering=1) as file:
                ticker_prices = self.get_prices_list(file)
                tickers_name = os.path.basename(ticker)
                tickers_name = tickers_name.split(sep='.')[0]
                self.collector.put(dict(ticker=tickers_name, volatility=self.counting_volatility(ticker_prices)))
                # print(f'Читаем файл {self.tickers_name}')

    @staticmethod
    def counting_volatility(ticker_prices):
        max_price = max(ticker_prices)
        min_price = min(ticker_prices)
        ave_price = (max_price + min_price) / 2
        volatility = (max_price - min_price) / ave_price * 100
        return volatility

    @staticmethod
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


@time_track
def main():
    tickers_stat = multiprocessing.Queue()
    all_files = get_files_list("trades/*.csv")
    files_in_thread = len(all_files) // 4
    tickers_stacks = [ParsingTicker(tickers_list=files_list, collector=tickers_stat) for files_list in
                      chunks(files_in_thread,
                             all_files)]

    for stack in tickers_stacks:
        stack.start()

    print(f'Количество потоков - {len(tickers_stacks)}')

    for stack in tickers_stacks:
        stack.join()

    tickers_vols = []
    zero_tickers = []
    while not tickers_stat.empty():
        data = tickers_stat.get()
        tickers_name = data['ticker']
        tickers_volatility = data['volatility']
        if tickers_volatility:
            tickers_vols.append((tickers_name, tickers_volatility))
        else:
            zero_tickers.append(tickers_name)

    tickers_vols.sort(key=itemgetter(1), reverse=True)
    print('Топ 3 лучших тикеров по волатильности')
    for ticker, vol in tickers_vols[0:3]:
        print(ticker, round(vol, 2))

    print('')
    print('Топ 3 худших тикеров по волатильности')
    for ticker, vol in tickers_vols[-1:-4:-1]:
        print(ticker, round(vol, 2))

    print('')
    print('Тикеры с нулевой волатильностью')
    for ticker in zero_tickers:
        print(ticker)


if __name__ == '__main__':
    main()
