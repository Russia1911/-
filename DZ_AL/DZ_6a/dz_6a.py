"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Время перехода между режимами должно составлять 7 и 2 секунды.
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time

# Создаем класс TrafficLight
class TrafficLight :
    # создаем атрибуты класса
    __color_red = 'red'
    __color_green = 'green'
    __color_yellow = 'yellow'
    # создаем методы класса
    def __init__(self, color_red = 'red' , color_green = 'green' , color_yellow = 'yellow'):
        self.color_red = color_red
        self.color_green = color_green
        self.color_yellow = color_yellow
    # создаем методы класса
    def running(self):
        for x in range(10):
            print(self.color_red)
            time.sleep(7)
            print(self.color_yellow)
            time.sleep(2)
            print(self.color_green)
            time.sleep(1)

# создав экземпляр и вызвав описанный метод.
start_user = TrafficLight()

start_user.running()
