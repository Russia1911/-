"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
# вводим через пробел два числа которые хотите поделить
user_ent1, user_ent2 = map(int, input("Введите через пробел два числа которые хотите поделить \n Пример: (n1 / n2) :  "
                                      ).split())
def user_func(user_ent1, user_ent2): # озиционные аргументы (user_ent1, user_ent2)
    try: # если  при делении user_ent1 / user_ent2 или  user_ent2 / user_ent1 возникнет ошибка
        user_ent1 / user_ent2 or user_ent2 / user_ent1
    except ZeroDivisionError as e:  # тогда программа выдаст print("Деление на 0 ") и вернет 0 return 0
        print("Деление на 0 ")
        return 0
    else:
        return user_ent1 / user_ent2 or user_ent2 / user_ent1
arg = user_func (user_ent1, user_ent2)

print("Ответ: ", round(arg, 2))  # получаем ответ
