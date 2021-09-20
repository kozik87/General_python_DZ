# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов 
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# \ а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
#  в которых фамилия начинается с соответствующей буквы. Например:
# >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     }, 
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"], 
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

# def thesaurus_adv(*args):
#     """ 
#     This function is creating dictionary with keys - first letter of surname 
#     and arguments are dictionary with keys - first letter of firstname
#     """
#     my_dict = {}
#     my_dict_names = {}

#     for i in args:
#         if not i.split(" ")[1][0] in my_dict: 
#             my_dict.setdefault(i.split(" ")[1][0], {}).setdefault(i[0], [i])
#         else:         
#             if i[0] in my_dict[i.split(" ")[1][0]]:
#                 my_dict_names = my_dict.get(i.split(" ")[1][0])
#                 my_dict[i.split(" ")[1][0]][i[0]]= my_dict_names.get(i[0]) + [i]    
#             else:
#                 my_dict.setdefault(i.split(" ")[1][0], {}).setdefault(i[0], [i])
#     return my_dict


# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

#Вариант 2
def thesaurus_adv(*args):
    """ 
    This function is creating dictionary with keys - first letter of surname 
    and arguments are dictionary with keys - first letter of firstname
    """
    my_dict = {}

    for fullname in args:
        
        firstname, surname = fullname.split()

        my_dict.setdefault(surname[0], {}).setdefault(firstname[0], []).append(fullname)

    return my_dict

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))