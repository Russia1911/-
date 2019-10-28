"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните ызов методов и также покажите результат
"""

# Создаем класс Car
class Car:
    is_police = True # методы
    def __init__(self,name , color, show_speed , speed ):
        self.speed = speed
        self.color = color
        self.name = name
        self.show_speed = show_speed

    def user_method(self):
        """ Метод вывода информации о машине """
        print("Марка:{}\nЦвет:{}\n ".format(self.name, self.color))

    def go(self):
        return "машина поехала"
    def stop(self):
        return "машина остановилась"
    def turn_right (self):
        return "машина повернула в право"
    def turn_left (self):
        return "машина повернула в лево "

""" TEST
s = Car("км/ч", "red", "Лада гранта", 50)
s.user_method()
"""

class TownCar(Car):
    def user_method2(self):
        """ Метод вывода информации о машине """
        if self.show_speed <= 60:
            print("Марка:{}\nЦвет:{}\nТекущяя скорость: {} {} ".format(self.name, self.color, self.show_speed,
                                                                       self.speed))
        else:
            print("Марка:{}\nЦвет:{}\nТекущяя скорость: {} {}\nПривышение скорости!!!".format(self.name, self.color,
                                                                                        self.show_speed, self.speed))

Town_Car = TownCar("Лада гранта","Белая", 50 ,"км/ч")
Town_Car.user_method2()
print('--------------------')

class SportCar(Car):
    def user_method3(self):
        """ Метод вывода информации о машине """
        print("Марка:{}\nЦвет:{}\nТекущяя скорость: {} {} ".format(self.name, self.color, self.show_speed,
                                                                   self.speed))

Sport_Car = SportCar("Ламборджини","Желтый", 40 ,"км/ч")
Sport_Car.user_method3()
print('--------------------')

class WorkCar(Car):
     def user_method4(self):
        """ Метод вывода информации о машине """
        if self.show_speed <= 40:
            print("Марка:{}\nЦвет:{}\nТекущяя скорость: {} {} ".format(self.name, self.color, self.show_speed,
                                                                       self.speed))
        else:
            print("Марка:{}\nЦвет:{}\nТекущяя скорость: {} {}\nПривышение скорости!!!".format(self.name, self.color,
                                                                                        self.show_speed,self.speed))

Work_Car = WorkCar("Гран Торино ","Красный", 61 ,"км/ч")
Work_Car.user_method4()
print('--------------------')

class PoliceCar(Car):
    def user_method5(self):
        """ Метод вывода информации о машине """
        print("Марка:{}\nЦвет:{}\nТекущяя скорость: {} {} ".format(self.name, self.color, self.show_speed,
                                                                   self.speed))
#
Police_Car = PoliceCar("Ford mustang gt","Черный", 100 ,"км/ч")
Police_Car.user_method5()
print('--------------------')