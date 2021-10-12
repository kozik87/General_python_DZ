# 4.	Реализуйте базовый класс Car:
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 
# 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Вызовите методы и покажите результат

from random import choice

class Car:
    
    direction = ['Left', 'Right']

    def __init__(self, s, c, n, p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def go(self):
        return 'Поехала'

    def stop(self):
        return 'Остановилась'

    def turn(self):
        return 'Повернула ' + choice(self.direction)

    def show_speed(self):
        return self.speed

class TownCar(Car):
    
    def show_speed(self):
        if self.speed > 60:
            return 'Превышена разрешенная скорость'
        else:
            return self.speed

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return 'Превышена разрешенная скорость'
        else:
            return self.speed

class PoliceCar(Car):
    def __init__(self, s, c, n, p=True):
        super().__init__(s, c, n, p)
        self.is_police = 1

print(TownCar(70, 'Red', 'Mersedes').go())
print(TownCar(70, 'Red', 'Mersedes').turn())
print(TownCar(70, 'Red', 'Mersedes').stop())
print(TownCar(70, 'Red', 'Mersedes').show_speed())

print(Car(70, 'Red', 'Mersedes').go())
print(Car(70, 'Red', 'Mersedes').turn())
print(Car(70, 'Red', 'Mersedes').stop())
print(Car(70, 'Red', 'Mersedes').show_speed())

