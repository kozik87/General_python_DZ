# 2.	Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
#  Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod

class Clother(ABC):
    result = 0
    def __init__(self, V):
        self.V = V
    
    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clother.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        rez= Clother.result
        Clother.result = 0
        return f'{rez}'


class Coat(Clother):
    @property
    def consumption(self):
        return  round(self.V / 6.5 + 0.5)

class Suit(Clother):
    @property
    def consumption(self):
        return round(self.V * 2 + 0.3)

a = Suit(138)
b = Coat(22)
print(a + b)