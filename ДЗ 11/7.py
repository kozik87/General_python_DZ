# 7.	Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». 
# Реализовать перегрузку методов сложения и умножения комплексных чисел. 
# Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), 
# выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.

class ComplexNumber:

    def __init__(self, a, b):
        '''Creates Complex Number'''
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + i * ({self.b})'

    def __add__(self, other):
        '''Adds complex numbers'''
        return f'({self.__str__()}) + ({other.__str__()}) = {self.a + other.a} + i * ({self.b + other.b})'

    def __sub__(self, other):
        '''Subtracts complex numbers'''
        return f'({self.__str__()}) - ({other.__str__()}) = {self.a - other.a} + i * ({self.b - other.b})'

    def __mul__(self, other):
        '''Multiplies complex numbers'''
        return f'({self.__str__()}) * ({other.__str__()}) = {self.a * other.a - self.b * other.b} + i * ({self.b * other.a + other.b * self.a})'

    def __truediv__(self, other):
        '''Divides complex numbers'''
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return f'({self.__str__()}) / ({other.__str__()}) = {(a * c + b * d)/(c ** 2 + d ** 2)} + i * ({(b * c - a * d)/(c ** 2 + d ** 2 )})'

c1 = ComplexNumber(5, 6)
c2 = ComplexNumber(1, 2)

print(c1)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)


