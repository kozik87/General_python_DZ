# 1. Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

list_expressions = ["15 * 3", "15 / 3", "15 // 2", "15 ** 2"]

for i in list_expressions:
    print(i, '=', eval(i), type(eval(i)))