"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
nex = True
# функция my_func(), которая принимает три позиционных аргумента,
def my_func(user_ent1, user_ent2, user_ent3):
    """возвращает сумму наибольших двух аргументов """
    user_set1 = user_ent1 + user_ent2
    user_set2 = user_ent2 + user_ent3
    user_set3 = user_ent1 + user_ent3
    dict_sample = {user_set1, user_set2, user_set3}

    print(max(dict_sample))
 # пока "nex = True" выполнять цикл "while nex:"
while nex:
    try: # запрос у пользователя два ч
        user_ent1, user_ent2, user_ent3 = map(int, input("Введите через пробел три числа которые хотите поделить \n"
                                                         "Пример: 1  2  3 \n      :  ").split())
    except NameError as e: # проверка на ошибку ввода пользователем данных
        print(f"{e}\n Неверное значение данных")
        continue
    except ValueError as e: # проверка на ошибку ввода пользователем данных
        print(f"{e}\n Неверное значение данных")
        continue
    end_1 = my_func(user_ent1, user_ent2, user_ent3) #  вызв функции  my_func()
    while True: # проверка не хочет ли  пользователь продолжить
        next_add = input("Хотите продолжить ? Да/Нет\n")
        if next_add.lower() in ('да', 'нет'):
            nex = next_add.lower() == 'да'
            break
        else:
            print("Неверный ввод, повторите  (варианты ответа: Да/Нет)")
