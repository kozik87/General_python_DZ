# 4.	Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные 
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...


# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3


# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

from functools import wraps

def val_check(l_func):
    def _val_cheker(func):

        @wraps(func)
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'Wrong val {num}')
                 
        return wrapper
    
    return _val_cheker

@val_check(lambda x: x > 0)

def calc_cube(x):
    return x ** 3

a= calc_cube(4)
a= calc_cube(-1)


