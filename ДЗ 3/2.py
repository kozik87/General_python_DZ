# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — 
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

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
    
   if str(word).capitalize() == str(word):         
       return dict_eng.get(str(word).lower()).capitalize()
   else:
       return dict_eng.get(word)



print(num_translate("one"))
print(num_translate("ten"))
print(num_translate("ten1111"))
print(num_translate("Four"))
print(num_translate("Six"))
