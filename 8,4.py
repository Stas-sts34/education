'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
 А также класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других
 данных, можно использовать любую подходящую структуру (например, словарь).
 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
 пользователем данных. Например, для указания количества принтеров, отправленных на склад,
 нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

'''


class Warehouse:
    '''
    склад хранения оргтехники
    '''
    def __init__(self, name):
        self.name = name
        self.warehouse = {                      # словарь для данных склада
            'склад': self.name
        }

    def add_warehouse(self, product, count):            # метод добавление/оприходывание товара на склад
        if self.warehouse.get(product['устройство']) == None:
            self.warehouse[product['устройство']] = int(count)
            return self.warehouse
        else:
            self.warehouse[product['устройство']] += int(count)
            return self.warehouse

    def give_from_warehouse(self, other, product, count):       # метод перемещение товаров со склада на склад
        try:
            result = self.warehouse[product['устройство']] - int(count)
            if result < 0:
                print('невозможно выгрузить больше, чем есть на складе')
            else:
                self.warehouse[product['устройство']] = result
                if other.warehouse.get(product['устройство']) == None:
                    other.warehouse[product['устройство']] = int(count)
                    return other.warehouse
                else:
                    other.warehouse[product['устройство']] += int(count)
                    return other.warehouse

        except TypeError:
            print(' не правильно ввели данные')


    def get_warehouse(self):
        return self.warehouse



class Office_equipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.item = {'устройство': self.name,
                     'цена': self.price,
                     }

    @property
    def get_price(self):
        return self.item

    @get_price.setter
    def get_price(self, price):
        self.item['цена'] = price

    def get_item(self):
        return self.item


class Printer(Office_equipment):
    def printer_speed(self, speed):
        self.speed = speed
        self.item['скорость печати'] = self.speed
        return self.item


class Scanner(Office_equipment):
    def scanner_speed(self, speed):
        self.speed = speed
        self.item['скорость сканирования'] = self.speed
        return self.item


class Xerox(Office_equipment):
    def xerox_speed(self, speed):
        self.speed = speed
        self.item['скорость копирования'] = self.speed
        return self.item


p = Printer('hp', 125)
s = Scanner('canon', 300)
p.printer_speed(5)      # устанавливаем свойство скорости печати
p.get_price=100         # устанавливаем цену
x=Xerox('sams', 200)
print('товар ',p.get_item())


warehouse = Warehouse('основной')       # создаем склад 1
skl = Warehouse('коммерч')              # создаем склад 2
warehouse.add_warehouse(p.get_item(), 12)   # добавляем товар и кол-во
warehouse.add_warehouse(s.get_item(), 10)   # добавляем товар и кол-во
skl.add_warehouse(x.get_item(), 5)          # перемещаем на другой склад
print('склады до', warehouse.get_warehouse(), skl.get_warehouse())
warehouse.give_from_warehouse(skl, p.get_item(), 3)     # еще перемещаем
warehouse.give_from_warehouse(skl, s.get_item(), 5)     # еще перемещаем
print('склады после', warehouse.get_warehouse(), skl.get_warehouse())
skl.give_from_warehouse(warehouse, s.get_item(),2)      # перемещаем обратно на основной склад
print('склады end', warehouse.get_warehouse(), skl.get_warehouse())