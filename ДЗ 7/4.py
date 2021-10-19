# 4.	Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — 
# верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов 
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), 
# например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
import django
from collections import defaultdict

def dir_info():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dir, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[size] += 1

    for size, num in sorted(django_files.items()):
        print(f'{size}: {num}')

dir_info()