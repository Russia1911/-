"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from Line_6 import test_4a

user_var1 = test_4a.user_var1  # user_var1 = int(input("выработка в часах")) пользователь вводит чило
user_var2 = test_4a.user_var2  # user_var2 = int(input("ставка в час")) пользователь вводит чило
user_var3 = test_4a.user_var3  # user_var3 = int(input("премия")) пользователь вводит чило

from functools import partial

def my_func(param_1, param_2): # parameter (param_1, param_2)
    def test(x):
        return (param_1 * param_2) + x
    return test

new_my_func = partial(my_func, user_var1 , user_var2)()

print(new_my_func(user_var3))









