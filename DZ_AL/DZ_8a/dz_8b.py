"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
с ошибкой.
"""

"класс-исключение"
class MyError(ZeroDivisionError):
    def __init__(self, text):
        self.txt = text

"ввод числа пользователем "
user_input = input("Введите положительное целое число: ")
try:
    user_input = int(user_input)  # преобразование строки в число

    if user_input / 0: # если число дел на 0 вызыв MyError вывод текста ошибки вывод пользователю
        raise MyError
except ValueError:
    print("Тип ошибки значения!")
except ZeroDivisionError as _:
    print(_)
else:
    print(user_input) # ошибка division by zero