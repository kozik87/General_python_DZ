# 3.	Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
# Проверить работу исключения на реальном примере. 
# Запрашивать у пользователя данные и заполнять список необходимо только числами. 
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
# пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
# При этом скрипт завершается, сформированный список с числами выводится на экран.

# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю 
# ввести текст (не число) и отобразить соответствующее сообщение. 
# При этом работа скрипта не должна завершаться.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
inp_num = 0

while inp_num != 'stop':
    inp_num = input("Введите элемент списка (число)': ")

    try:
        if not inp_num.isnumeric():
            raise OwnError("Ошибка.  введен текст!")
    except OwnError as err:
        print(err)
    else:
        my_list.append(inp_num)
    
print(my_list)