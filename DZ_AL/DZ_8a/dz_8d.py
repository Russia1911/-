"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""




class Office_equipment:
    quantity_printer = 0


    def __init__(self, manufacturer, name , what_seal , print_format, quantity ):
        self.manufacturer = manufacturer # производитель
        self.name = name #название
        self.what_seal = what_seal # какая печать
        self.print_format = print_format # формат печати
        self.quantity = int(quantity) # количество
        Office_equipment.quantity_printer += self.quantity


    def info_Office_equipment(self):
        print("Название : {}\nКакая печать : {}\nФормат печати : {}\nКоличество : {}-шт "
              .format(self.name, self.what_seal, self.print_format, self.quantity))



class printer(Office_equipment):
    def info_Office_equipment(self):

        print("Производитель : {}\nНазвание : {}\nКакая печать : {}\nФормат печати : {}\nКоличество : {}-шт "
              .format(self.manufacturer,self.name, self.what_seal, self.print_format, self.quantity))

user_Office_equipment_printer = printer("Asus","EpsonL120", "4-цветная струйная печать",
                                         "макс. формат печати A4 (210 × 297 мм)", "12")
user_Office_equipment_printers = Office_equipment
user_Office_equipment_printer.info_Office_equipment()
print("--------------------------------------------")

class scanner(Office_equipment):
    def info_Office_equipment(self):
        print("Производитель : {}\nНазвание : {}\nКакая печать : {}\nФормат печати : {}\nКоличество : {}-шт "
              .format(self.manufacturer, self.name, self.what_seal, self.print_format, self.quantity))

user_Office_equipment_scanner = printer("Asus","МФУ Xerox WorkCentre 3025BI", "ч/б лазерная печать",
                                         "разрешение 4800x9600 dpi", "8")

user_Office_equipment_scanner.info_Office_equipment()
print("--------------------------------------------")


class copier(Office_equipment):
    def info_Office_equipment(self):
        print("Производитель : {}\nНазвание : {}\nКакая печать : {}\nФормат печати : {}\nКоличество : {}-шт "
              .format(self.manufacturer, self.name, self.what_seal, self.print_format, self.quantity))


user_Office_equipment_copier = printer("Asus", "МФУ Xerox B205", "ч/б лазерная печать",
                                        "макс. формат печати A4 (210 × 297 мм)", "10")
user_Office_equipment_copier.info_Office_equipment()
print("--------------------------------------------")
Office_equipment_warehouse_HT = Office_equipment
print("Колличество тавара на складе ", Office_equipment_warehouse_HT.quantity_printer, 'шт')


"""
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""


NUMBER, WHERE_ARE = range(2)


class sklad:
    def __init__(self):
        self.dic = {}
    #количество на складе
    def add(self, name, amount):
        self.dic[name] = [amount, None]
        self.mwhere(name, amount)
    #находятся ли в наличии
    def mwhere(self, name, amount):
        if self.dic[name][NUMBER] <= 0:
            self.self.dic[name][WHERE_ARE] = "missing"
        else:
            self.dic[name][WHERE_ARE] = amount
    # добавить товар
    def plus(self, name, p):
        self.dic[name][NUMBER] += p
        self.mwhere(name, self.dic[name][NUMBER])

    # минус товар
    def minus(self, name, m):
        self.dic[name][NUMBER] -= m
        self.mwhere(name, self.dic[name][NUMBER])

if __name__ == '__main__':
    m = sklad()

    printer, scanner, copier = "принтер", "сканер", "ксерокс"
    m.add(printer, 12)
    m.add(scanner, 8)
    m.add(copier, 10)
    print (printer, m.dic[printer][WHERE_ARE], '\n', scanner, m.dic[scanner][WHERE_ARE], '\n', copier, m.dic[copier][WHERE_ARE])