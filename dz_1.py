# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# Имя пользователя +  время в сек
user_1 = input("Введите имя ользователя: ")
second_3 = int(input("Введите время в секундах: "))
# // Целочисленное деление
clock_1 = second_3 // 3600
second_3 %= 3600
minutes_2 = second_3 // 60
second_3 %= 60
Otvet = user_1, f"ваш ответ в формате чч:мм:сс  {clock_1}:{minutes_2}:{second_3}"
print(Otvet)