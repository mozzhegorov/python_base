#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

distances['Москва'] = {}
distances['Москва']['Лондон'] = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
distances['Москва']['Париж'] = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** .5

distances['Лондон'] = {}
distances['Лондон']['Москва'] = distances['Москва']['Лондон']
distances['Лондон']['Париж'] = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** .5

distances['Париж'] = {}
distances['Париж']['Лондон'] = distances['Лондон']['Париж']
distances['Париж']['Москва'] = distances['Москва']['Париж']

print(distances)




