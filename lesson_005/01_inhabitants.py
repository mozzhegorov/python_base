# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as room_1_folks
from room_2 import folks as room_2_folks

print('В комнате room_1 живут:', end=' ')
for num, folk in enumerate(room_1_folks):
    print(folk) if num == (len(room_1_folks) - 1) else print(folk, end=', ')

print('В комнате room_2 живут:', end=' ')
for num, folk in enumerate(room_2_folks):
    print(folk) if num == (len(room_2_folks) - 1) else print(folk, end=', ')
