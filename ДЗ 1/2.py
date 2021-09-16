# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» 
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

def is_sum_figures_deleted_7 (x):
    
    x = str(x)
    x_len = len(x)
    sum_x_fegures = 0
    i = 0

    while i < x_len:
        sum_x_fegures += int(x[i])
        i += 1
    
    if sum_x_fegures % 7 == 0:
        return True
    else:
        return False

cube_list = []
num = 1
idx = 0
sum_elements = 0

# можно делать через for i in range(1, 1000, 2)
while num < 1000:
   cube_list.append(num ** 3)
   if is_sum_figures_deleted_7(cube_list[idx]):
       sum_elements += cube_list[idx]
   num += 2
   idx += 1

print(sum_elements)

cube_list = []
num = 1
idx = 0
sum_elements = 0 

while num < 1000:
   cube_list.append(num ** 3 + 17)
   if is_sum_figures_deleted_7(cube_list[idx]):
       sum_elements += cube_list[idx]
   num += 2
   idx += 1

print(sum_elements)