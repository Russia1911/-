"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

"""
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
"""
#  использовать функцию count() и cycle() модуля itertools.
from itertools import cycle
from itertools import count


user_list = []
for i in count(1): # начинаем с 1 и прис i пока i не больше 8
    if i > 8: #  если i  больше 8  break
        break
    else: # записываем в user_list
        user_list.append(i)
print(user_list)

"""
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

count = 0
for item in cycle('Алекс'): # бесконечно зациклить буквы 'Алекс'
    if count > 8:
        break
    print(item) # пока count < 0
    count += 1