#d = '你好{},今天星期几\'{}？'.format('Tom', 123)
# print(d)

import random

a = random.randint(100, 10000)
hour = a // 3600
minutes = a % 3600 // 60
seconds = a % 60
print(a)

a1 = '{}秒 = {}小时，{}分钟，{}秒'.format(a, hour, minutes, seconds)
print(a1)
#nihao
