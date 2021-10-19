# 5.	Продолжить работу над предыдущим заданием. 
# Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
# можно использовать любую подходящую структуру (например, словарь).

class Store:
    def __init__(self, name='', stock=0):
        self.store_dict = {name : stock}
        self.type = name

    def goods_receipt(self, name, count):
        if self.store_dict.get(name):
            self.store_dict[name] += count
            print(f'Товар {name} добавлен на склад в размере {count}, остаток: {self.store_dict[name]}')
        else:
            self.store_dict.setdefault(name, count)
            print(f'Новый товар {name} добавлен на склад в размере {count}')
    
    def goods_send(self, name, count, office):
        if self.store_dict.get(name):
            if self.store_dict[name] >= count:
                self.store_dict[name] -= count
                print(f'Товар {name} отправлен в {office}. На складе: {self.store_dict[name]}')
            else:
                print(f'{name} недостаточно на складе')
        else:
            print(f'{name} нет на складе')
    
    def show_stocks(self):
        return self.store_dict

class OfficeEquipment(Store):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class Printer(OfficeEquipment):
    def __init__(self, name, type, printer_type):
        super().__init__(name, type)
        self.printer_type = printer_type

class Scaner(OfficeEquipment):
    def __init__(self, name, type, scanner_speed):
        super().__init__(name, type)
        self.scanner_speed = scanner_speed

class Xerox(OfficeEquipment):
    def __init__(self, id, name, type, resolution):
        super().__init__(id, name, type)
        self.resolution = resolution

a = Store()
a.goods_receipt('Printer', 4)
a.goods_receipt('Xerox', 2)
a.goods_receipt('Xerox', 7)
a.goods_receipt('Scaner', 2)

a.goods_send('Printer', 1, 'Office 1')
a.goods_send('Xerox', 10, 'Office 2')

print(a.show_stocks())
