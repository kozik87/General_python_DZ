# 1.	Не используя библиотеки для парсинга, распарсить (получить определённые данные) 
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

with open('/Users/konstantinkarnaukhov/Cloud Mail.Ru/DataEngineering/4_Основы Python/ДЗ/ДЗ 6/nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = f.readline()
    my_cortege = ()
    my_list = []
    while content:
        remote_addr = content.split('"')[1].split(" -")[0]
        request = content.split('"')[3]
        request_type = request.split(' ')[0]
        requested_resource = request.split(' ')[1]
        my_cortege = remote_addr, request_type, requested_resource
        my_list.append(my_cortege)
        content = f.readline()

print(my_list)
