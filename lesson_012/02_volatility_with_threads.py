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

# TODO: имейте ввиду, что создавать сразу 100500 потоков (даже 100) на 4 ядерном процессор особого смысла
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


# TODO: функции get_prices_list и counting_volatility должны стать статическими методами в классе ParsingTicker.
#  Это мы как-то упустили в первой задаче.
class ParsingTicker(Thread):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: лучше сделать, чтобы был не 1 файл, а список файлов.
        self.file = filename
        self.volatility = 0
        self.tickers_name = 0

    def run(self):
        # TODO: здесь тогда будет считаться информация по нескольких тикерам сразу
        with open(self.file, mode='r', encoding='utf8', buffering=1) as file:
            ticker_prices = get_prices_list(file)
            self.volatility = counting_volatility(ticker_prices)
            self.tickers_name = os.path.basename(self.file)
            self.tickers_name = self.tickers_name.split(sep='.')[0]
            # print(f'Читаем файл {self.tickers_name}')


# TODO: этот метод можно сделать статическим. Что это означает?
#  Что метод можно вызывать даже тогда, когда объект класса не инициализирован, т.к. метод не использует поля
#  объекта. Пример:
#  .
#  class MySum:
#     def __init__(self, param_1, param_2):
#        self.field_1 = param_1
#        self.field_2 = param_2
#  .
#     def sum(self):
#        return self.field_1 + self.field_2
#  .
#     @staticmethod
#     def sum_2(param_1, param_2):
#        return param_1 + param_2
#  .
#  Второй метод не использует поля объекта, поэтому создание объекта не обязательно для того, чтобы его вызывать:
#     MySum.sum_2(100, 500)     # вызываем метод, как простую функцию) Объект создавать не нужно. Вызываем от имени класса.
#  .
#  А вот для 1го метода, создание объект обязательно:
#     obj = MySum(100, 500)
#     obj.sum()



@time_track
def main():
    files_list = get_files_list("trades/*.csv")
    # TODO: сейчас мы создаем на 1 тикер 1 поток. Создание потока - штука затратная. Лучше создать 4-8 потоков, и каждому
    #  дать одинаковое количество файлов.
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
