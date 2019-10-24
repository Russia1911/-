"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
try:
    with open('C:\Python37\Line_6\DZ_AL\DZ_5a\my_file.txt', 'r', encoding='UTF-8') as file:
        print("Всего слов: \n", file.read())
except IOError:
    pass
finally:
    file = open('C:\Python37\Line_6\DZ_AL\DZ_5a\my_file.txt', 'r', encoding='UTF-8')
    line = 0
    for i in file:
        line += 1
        # флаг для удобства фиксации перехода
        flag = 0
        # слова
        word = 0
        for j in i:
            if j != ' ' and flag == 0:
                word += 1 # счетчик
                flag = 1
            elif j == ' ':
                flag = 0

        print(i, len(i), 'симв.', word, 'слов')

    print(line, 'строк')
    file.close()
