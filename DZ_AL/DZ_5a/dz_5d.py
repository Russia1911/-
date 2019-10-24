"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open('C:\Python37\Line_6\DZ_AL\DZ_5a\mu_t.txt', 'r', encoding='UTF-8') as file:
    n = 1 # счетчик
    while n < 5:
        if n == 1:
            line = file.readline() # вытягиваем строку и проверяем
            new_line = line.replace('One — 1', 'Один - 1')
            print(new_line)
            n += 1
            ouf = open('C:\Python37\Line_6\DZ_AL\DZ_5a\mu_td.txt', 'a', encoding='UTF-8')
            ouf.write(str(new_line) + "\n")
            ouf.close()
        elif n == 2:
            line = file.readline()# вытягиваем строку и проверяем
            new_line = line.replace('Two — 2', 'Два - 2')
            print(new_line)
            n += 1
            ouf = open('C:\Python37\Line_6\DZ_AL\DZ_5a\mu_td.txt', 'a', encoding='UTF-8')
            ouf.write(str(new_line) + "\n")
            ouf.close()
        elif n == 3:
            line = file.readline()# вытягиваем строку и проверяем
            new_line = line.replace('Three — 3', 'Три - 3')
            print(new_line)
            n += 1
            ouf = open('C:\Python37\Line_6\DZ_AL\DZ_5a\mu_td.txt', 'a', encoding='UTF-8')
            ouf.write(str(new_line) + "\n")
            ouf.close()
        elif n == 4:
            line = file.readline()# вытягиваем строку и проверяем
            new_line = line.replace('Four — 4', 'Четыре - 4')
            print(new_line)
            n += 1
            ouf = open('C:\Python37\Line_6\DZ_AL\DZ_5a\mu_td.txt', 'a', encoding='UTF-8')
            ouf.write(str(new_line) + "\n")
            ouf.close()
        else:
            print("Конец перевода ")