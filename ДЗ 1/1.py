## 1. Реализовать вывод информации о промежутке времени в зависимости от 
# его продолжительности duration в секундах: до минуты: <s> сек; до 
# часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; 
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input("Введите число: "))

ss = duration % 60
mm = duration // 60
hh = duration // 3600
dd = duration // 86400

if mm < 1:
    print(f"{ss} сек")
elif hh < 1:
    print(f"{mm} мин {ss} сек")
elif dd < 1:
    mm = mm % 60
    print(f"{hh} час {mm} мин {ss} сек")
else:
    mm = mm % 60
    hh = hh % 24
    print(f"{dd} дн {hh} час {mm} мин {ss} сек")

