# 5.	Представлен список чисел. Определить элементы списка, не имеющие повторений. 
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# ------ Решение в лоб ------
# rezult = []

# for i in range(0, len(src)):
#     k=0
#     for j in range(0, len(src)):
#         if src[i] == src[j]:
#             k+=1
#     if k < 2:        
#         rezult.append(src[i])

# print(rezult)

# rezult = (x, mylist.count(x)) for x in set(src))

# ------ Оптимизация ------

# rezult = []

# for i in range(0, len(src)):
#     if src.count(src[i]) < 2:        
#         rezult.append(src[i])

# print(rezult)

# ------ Оптимизация 2 ------

rezult = [i for i in src if src.count(i) == 1]     

print(rezult)