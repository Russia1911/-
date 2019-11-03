"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""



class Complex_number:


    def __init__(self, number_1):
        self.number_1 = number_1

    def __add__(self, other):

        return Complex_number(self.number_1 + other.number_1)
    def __mul__(self, other):

        return Complex_number(self.number_1 * other.number_1)

if __name__ == '__main__':
    mc_1 = Complex_number(10)
    mc_2 = Complex_number(2)
    print(mc_1.number_1 + mc_2.number_1)
    print(mc_1.number_1 * mc_2.number_1)
