"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""
# Создать программно файл в текстовом формате
file = open('C:\Python37\Line_6\DZ_AL\DZ_5a\my_file.txt', 'w', encoding='UTF-8')
nex_inp = True
user_list = []
while nex_inp == True:
    user_inp = input("Ввод: ") # данные, вводимые пользователем.
    if not user_inp:
        nex_inp = False
        break
    else:
        user_list.append(user_inp)

file.writelines('\n'.join(user_list))
file.close()








