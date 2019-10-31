"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
user_min = []
user_max = []
user = 0
user_list = {}
with open('C:\Python37\Line_6\DZ_AL\DZ_5a\salarios.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        key,  value = line.split()
        user_list[key] = int(value)
        # если ЗП < 20к записываем имя в user_min = []
        if int(value) < 20000:
            user_min.append(key)
            user += 1
        else:
            user_max.append(key)
            user += 1

print(user_list)
# вывести фамилии этих сотрудников
print("Зарплата меньше 20к ", user_min)
#
user_sum = (user_list['Залбеков'] + (user_list['Чаталбащян']) + (user_list['Иванов']) + (user_list['Кузнецов'])) / user
print("Подсчет средней величины дохода сотрудников сост.", user_sum, "руб")
