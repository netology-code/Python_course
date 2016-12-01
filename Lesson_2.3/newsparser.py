# в python3 такая строчка обычно не нужна
# но если у вас специфичные настройки компьютера
# может пригодиться
# -*- coding: UTF-8 -*-

import codecs
import json

with codecs.open('newsfr.json', encoding="iso8859_5") as news:
	print(json.load(news))

# print(ord('э')) # принимает букву, возвращает её код
# print(chr(1101)) # принимает число, возвращает букву, которая ей соответствует

