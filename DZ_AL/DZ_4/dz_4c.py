"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
"""

sum_all = [] # пустой список
for i in range(20, 241): # Сгенерированные цифрыот 20 до 240
    if ((i % 20 == 0) or (i % 21 == 0)): # кратные 20 или 21
        sum_all.append(i) # записмываем в sum_all все значения которые соотв условию
print("Элементы, удовлетворяющие условию : ", sum_all)
