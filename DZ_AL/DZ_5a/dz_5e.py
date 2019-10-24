"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
file = open('C:\Python37\Line_6\DZ_AL\DZ_5a\my_file.txt', 'w', encoding='UTF-8')
nex_inp = True
user_list = []
while nex_inp == True:
    user_inp = input("Ввод чисел: ")
    if not user_inp:
        nex_inp = False
        break
    else:
        user_list.append(user_inp)

file.writelines(' '.join(user_list))
file.close()
file = open('C:\Python37\Line_6\DZ_AL\DZ_5a\my_file.txt', 'r', encoding='UTF-8')
a = file.read().split()
file.close()
s = 0
for elem in a:
    s += int(elem)
print(s)


ouf = open('C:\Python37\Line_6\DZ_AL\DZ_5a\my_file.txt', 'w', encoding='UTF-8')
ouf.write(str(s)+"\n")
ouf.close()


