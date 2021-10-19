# 5.	Реализовать класс Stationery (канцелярская принадлежность):
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self):
        self.title = 'title'

    def draw(self):
        return "Запуск отрисовки"

class Pen(Stationery):
    def draw(self):
        return "Запуск отрисовки ручка"

class Pencil(Stationery):
    def draw(self):
        return "Запуск отрисовки карандаш"

class Handle(Stationery):
    def draw(self):
        return "Запуск отрисовки маркер"

print(Stationery().draw())
print(Pen().draw())
print(Pencil().draw())
print(Handle().draw())