# 2.	*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, 
# размер которых превышает объем ОЗУ компьютера.

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

my_dict = {}

for i in my_list:
    
    if i[0] in my_dict:
        counter = my_dict.get(i[0]) + 1
        
        my_dict[i[0]] = counter
    else:
        my_dict.setdefault(i[0], 1)


ssd = sorted(my_dict, key=my_dict.__getitem__)
ip_largest = {}
for i in range(-1, -5, -1):
    ip_largest.setdefault(ssd[i], my_dict[ssd[i]])

# 5 ip адресов с самым большим кол-вом запросов
print(ip_largest)