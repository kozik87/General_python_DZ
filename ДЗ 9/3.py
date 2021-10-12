# 3.	Реализовать базовый класс Worker (работник):
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», 
# например, {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
# и дохода с учётом премии (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        # self.wage = w
        # self.bonus = b
        self._income = {"wage": w, "bonus": b}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

reuqest = Position('Иван', 'Пушкин', 'Директор', 400000, 800000)
print(reuqest.get_full_name())
print(reuqest.get_total_income())