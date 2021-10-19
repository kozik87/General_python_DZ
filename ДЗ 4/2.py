# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. 
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. 
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. 
# Можно ли, используя только методы класса str, решить поставленную задачу? 
# Функция должна возвращать результат числового типа, например float. 
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? 
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, 
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, 
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils

def parsing_XML_string(str, attr):
    """
    parsing_XML_string
    вход - строка XML и название атрибута
    выход - значение атрибута
    """
    attr_start = "<" + attr + ">"
    attr_end = "</" + attr + ">"

    return str[str.find(attr_start) + len(attr_start):str.find(attr_end)]
 
def currency_rates(valute):
    """
    Currency rates
    вход - валюта
    выход - значение курса валюты в руб на текущую дату
    """
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    
    currency_dict ={}
    currency_string = content.split("Valute ID")

    for idx, i in enumerate(currency_string, start = 0):
        if idx > 0:
            currency_dict.setdefault(parsing_XML_string(i, "CharCode"), float(parsing_XML_string(i, "Value").replace(",", ".")))
   
    return format(currency_dict.get(valute.upper()), ".2f")


print(currency_rates("USD"))
print(currency_rates("eur"))