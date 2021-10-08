# 4.	*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ 
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
# Только теперь не нужно создавать словарь с данными. 
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). 
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

my_dict = {}

with open('ДЗ 6/users.csv', 'r', encoding='utf-8') as f_u:
    with open('ДЗ 6/hobby.csv', 'r', encoding='utf-8') as f_h:
        with open('ДЗ 6/users_hobby.txt', 'w', encoding='utf-8') as f:
            
            content_u = f_u.readline().replace(',', ' ').replace('\n', '')
            content_h = f_h.readline().replace('\n', '')

            while content_u or content_h:
                my_dict.setdefault(content_u, content_h)
                
                content_u = f_u.readline().replace(',', ' ').replace('\n', '')
                content_h = f_h.readline().replace('\n', '')

            f.write(str(my_dict))