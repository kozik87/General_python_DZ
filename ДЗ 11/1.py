# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. 
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime

class Date:
    def __init__(self, date):
        self.date =  datetime.strptime(date, '%d-%m-%Y')
        self.date_rus = self.date.strftime('%d.%m.%Y')
        self.day = self.date.strftime('%d')
        self.month = self.date.strftime('%m')
        self.year = self.date.strftime('%Y')

    @classmethod
    def data_to_int(cls, date, date_type):
        if date_type == 'd':
            return cls(date).day
        elif date_type == 'm':
            return cls(date).month
        elif date_type == 'y':
            return cls(date).year
        else:
            return 'Ошибка ввода типа даты'

    @staticmethod
    def valid_data(date):
        day, month, year = map(int, date.split('-'))
        return day >= 1 and day <= 31 and month <= 12 and year > 0 

d1 = '31-01-2021'
d1_show = Date(d1)
print(d1_show.date_rus)
print(Date.data_to_int(d1, 'd'))
print(Date.data_to_int(d1, 'm'))
print(Date.data_to_int(d1, 'y'))

print(Date.valid_data(d1))
