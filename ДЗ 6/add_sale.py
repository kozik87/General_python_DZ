def main(argv):
   program, *args = argv
   
   with open('sales.csv', "a",  encoding='utf-8') as f:
       f.write('\n'+ args[0])
       print('Sale Added')

   return 0

if __name__ == '__main__':
   import sys

   exit(main(sys.argv))