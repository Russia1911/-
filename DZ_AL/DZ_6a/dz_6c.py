"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_full_profit). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    """класс для всех сотрудников"""

    def __init__(self, name, surname, position, income, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position # (должность)
        self.income = income # (доход)
        self.salary = salary
        self.bonus = bonus


    def user_income(self):
        print('Оклад: {}. Зарплата: {}'.format(self.salary, self.bonus))

    def get_full_name(self):
        print('Имя: {}. Фамилия: {}\nДохода с учетом премии {} '.format(self.name, self.surname, self.salary +
                                                                          self.bonus))



class Position (Worker):

    def get_full_name2(self):
        print('Имя: {}. Фамилия: {}\nДохода в {} с учетом премии {}'.format(self.name, self.surname, self.income,
                                                                            self.salary +self.bonus))






user_Worker1 = Worker("Александр", "Зубов", "Гейм-дз", "Руб", 20000, 20000)
user_Worker1.user_income()
user_Worker1.get_full_name()
user_Worker2 = Position("Александр", "Зубов", "Гейм-дз", "Руб", 20000, 20000)
user_Worker2.get_full_name2()

