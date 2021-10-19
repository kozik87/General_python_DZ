# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:

from utils import currency_rates

def main(argv):
   program, *args = argv
   result = currency_rates(args[0])
   print(f'результат: {result}')

   return 0

if __name__ == '__main__':
   import sys

   exit(main(sys.argv))
