"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать день, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
"""Реализовать класс «Дата»"""
class Date:
    "«день-месяц-год»."
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-')) # перевод в int операясь на разделение "-"
        date1 = (day, month, year)

        return date1
#" @staticmethod, проводит валидацию числа, месяца и года (например, месяц — от 1 до 12)"
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        # не в каждом месяце 31 день ...
        return day <= 31 and month <= 12 and year <= 9999

user_date = Date.from_string('11-09-2012')
user_is_date = Date.is_date_valid('11-09-2012')

print(user_date)
print(user_is_date)









