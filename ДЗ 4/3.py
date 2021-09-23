# 3. * (вместо 2) Доработать функцию currency_rates(): 
# теперь она должна возвращать кроме курса дату, 
# которая передаётся в ответе сервера. 
# Дата должна быть в виде объекта date. 
# Подумайте, как извлечь дату из ответа, 
# какой тип данных лучше использовать в ответе функции?

from requests import get, utils
from datetime import date

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
        else:
            cur_day, cur_month, cur_year = i[i.find('ValCurs Date="') + len('ValCurs Date="'):i.find('ValCurs Date="') + len('ValCurs Date="') + 10].split(".")
            cur_day = date(int(cur_year), int(cur_month), int(cur_day)).isoformat()
    return format(currency_dict.get(valute.upper()), ".2f"), cur_day


print(currency_rates("USD"))
print(currency_rates("eur"))