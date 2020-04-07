# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as room_1_folks
from room_2 import folks as room_2_folks

print('В комнате room_1 живут:', ', '.join(room_1_folks))
print('В комнате room_2 живут:', ', '.join(room_2_folks))
