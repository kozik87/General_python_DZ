# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 
# c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. 
# Подумайте, как и где лучше хранить информацию, 
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(word):
   """ This function is translating numeric from English into Russian 
   For expample: num_translate("one") -->> "один"
   """
   dict_eng = {
            "zero":     "ноль",
            "one":      "один",
            "two":      "два",
            "three":    "три",
            "four":     "четыри",
            "five":     "пять",
            "six":      "шесть",
            "seven":    "семь",
            "eight":    "восеь",
            "nine":     "девять",
            "ten":      "десять", 
            }
            
   return dict_eng.get(word)

print(num_translate("one"))
print(num_translate("ten"))
print(num_translate("ten1111"))

