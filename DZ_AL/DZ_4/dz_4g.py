"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
# import math чтобы упростить  поиск  факториала числа n
import math
# import randint чтобы упростить генирацию рандом чисел
from random import randint

n = 0
numbers = []
# функция
def fibo_gen (nums):
    """
    :param nums: числа n
    :return:  произведение чисел от 1 до n
    """
    for i in nums:
        yield(math.factorial(i))

while n < 15:
    for i in range(15):
        numbers.append(randint(1, 15))
        sqr = fibo_gen(numbers)
        n += 1
    break
print("Сгенерированные цифры  : ", numbers)
print("Факториал сгенерированных цифр : ", list(sqr))