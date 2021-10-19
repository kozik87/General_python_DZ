# 5.	**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, 
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла. 
# Проверить работу скрипта.


def load_and_save (file_name_1, file_name_2, file_name_save):
    my_dict = {}

    with open(file_name_1 + '.csv', 'r', encoding='utf-8') as f_u:
        with open(file_name_2 + '.csv', 'r', encoding='utf-8') as f_h:
            with open(file_name_save + '.txt', 'w', encoding='utf-8') as f:
                
                content_u = f_u.readline().replace(',', ' ').replace('\n', '')
                content_h = f_h.readline().replace('\n', '')

                while content_u or content_h:
                    my_dict.setdefault(content_u, content_h)
                    
                    content_u = f_u.readline().replace(',', ' ').replace('\n', '')
                    content_h = f_h.readline().replace('\n', '')

                f.write(str(my_dict))
    
    return 1


def main(argv):
   program, *args = argv
   result = load_and_save(file_name_1= args[0], file_name_2 = args[1], file_name_save = args[2])
   print(f'Файлы {args[0]}.csv и {args[1]}.csv объеденены и записаны в {args[2]}.txt')

   return 0

if __name__ == '__main__':
   import sys

   exit(main(sys.argv))