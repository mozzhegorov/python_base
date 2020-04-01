# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
#  Вместо "for i in range(7)" используйте цикл обхода кортежа цветов rainbow_colors. Пример:
#           values = [1,2,3]
#           for i in values:
#               print(i)
#  .
#  Таким образом. Если в список цветов будет добавлен новый цвет (или удален), ваш код продолжит работать. В текущей
#  версии придется найти range(7) и изменить на range(6).

start_x = 50
end_x = 350
# TODO: во! То, что нужно. У нас есть кортеж и мы итерируемся по нему (т.е. перебираем один элемент за другим).
#  Если бы нам понадобились индексы, у нас был бы соблазн применить range(len()), но не стоило бы. В том случае
#  мы бы применили enumerate(). Пример (для расширения кругозора, и он гарантировано еще пригодится):
#       seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#       for season_id, season_name in enumerate(seasons):
# 	        print(season_id, ' - ', season_name)
#   .
#   В результате будет выведено:
#       0 - 'Spring'
#       1 - 'Summer'
#       2 - 'Fall'
#       3 - 'Winter'
#   .
for color in rainbow_colors:
    start_x += 5
    end_x += 5
    sd.line(sd.get_point(start_x, 50), sd.get_point(end_x, 450), color, 5)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

radius = 400

for color in rainbow_colors:
    radius += 4
    sd.circle(sd.get_point(-100, -100), radius, color, 4)


sd.pause()

# зачет!