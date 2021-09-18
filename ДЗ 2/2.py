# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём 
# до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - 
# можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
str_new = []

for str_x in str:
    if str_x.isdigit():
        str_new.append('"')
        str_new.append(str_x.zfill(2))
        str_new.append('"')
    else:
        str_new.append(str_x)

print(' '.join(str_new))