def main(argv):
   program, *args = argv
   i=0
   with open('sales.csv', "r",  encoding='utf-8') as f:
      if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
         if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(f) if start - 1 <= i < finish))
         else:
            print(*(v for i, v in enumerate(f) if i >= int(argv[1]) - 1 ))
      else:
         print(f.read())

   return 0

if __name__ == '__main__':
   import sys

   exit(main(sys.argv))