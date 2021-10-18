# 2.	Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверить его работу на данных, вводимых пользователем. 
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_del = input("Введите делимое: ")
inp_to_del = input("Введите делитель: ")

try:
    inp_to_del = int(inp_to_del)
    inp_del = int(inp_to_del)
    if inp_to_del == 0:
        raise OwnError("Деление на ноль!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {inp_del / inp_to_del}")
