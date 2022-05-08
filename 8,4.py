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
        self.warehouse_name = name

        self._warehouse = {                      # словарь для данных склада

        }

    def add_product(self, product, count: int):            # метод добавление/оприходывание товара на склад
        count = int(count)
        if not self._warehouse.get(product.name):
            self._warehouse[product.name] = count
            return self._warehouse
        else:
            self._warehouse[product.name] += count
            return self._warehouse

    def give_from_warehouse(self, other, product, count):       # метод перемещение товаров со склада на склад
        count = int(count)
        try:
            result = self._warehouse[product.name] - count
            if result < 0:
                print('невозможно выгрузить больше, чем есть на складе')
            else:
                self._warehouse[product.name] = result
                other.add_product(product, count)

        except TypeError:
            print(' не правильно ввели данные')


    def get_warehouse(self):
        return self._warehouse            # можно ли так возвращать словарь?



class OfficeEquipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        # self.item = {'устройство': self.name,
        #              'цена': self.price,
        #              }

    def __getitem__(self, item):            # для упрощения добавления объектов на склад
        return self.__dict__[item]

    def __setitem__(self, key, value):      # можно и так устанавливать цену
        self.__dict__[key] = value

    def __str__(self):
        return f'{self.__dict__}'

    @property
    def set_price(self):
        return self.price

    @set_price.setter
    def set_price(self, price):
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    def __str__(self):
        return f'{self.name, self.price, self.speed}'

    def printer_speed(self, speed):
        self.speed = speed
        # self.item['скорость печати'] = self.speed
        # return self.speed


class Scanner(OfficeEquipment):
    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    def __str__(self):
        return f'{self.name, self.price, self.speed}'

    def scanner_speed(self, speed):
        self.speed = speed
        # self.item['скорость сканирования'] = self.speed
        # return self.speed


class Xerox(OfficeEquipment):
    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    def __str__(self):
        return f'{self.name, self.price, self.speed}'

    def xerox_speed(self, speed):
        self.speed = speed
        # self.item['скорость копирования'] = self.speed
        # return self.speed


p = Printer('hp', 125, 5)
s = Scanner('canon', 300, 5)
p.printer_speed(6)      # устанавливаем свойство скорости печати
p.set_price = 100         # устанавливаем цену
p.price = 99    # по другому устанавливаем цену ( как вариант так можно? )
x=Xerox('sams', 200, 5)
print('товар ', p, s, x)


warehouse = Warehouse('основной')       # создаем склад 1
skl = Warehouse('коммерч')              # создаем склад 2
# print(p)

warehouse.add_product(p, 12)   # добавляем товар и кол-во
warehouse.add_product(s, 5)
warehouse.add_product(x, 1)
print(warehouse.get_warehouse())
# print(warehouse.__dict__)
warehouse.add_product(s, 10)   # добавляем товар и кол-во
print(warehouse.get_warehouse())
skl.add_product(x, 5)          # перемещаем на другой склад
print('склады до', warehouse.get_warehouse(), skl.get_warehouse())
warehouse.give_from_warehouse(skl, p, 3)     # еще перемещаем
warehouse.give_from_warehouse(skl, s, 5)     # еще перемещаем
print('склады после', warehouse.get_warehouse(), skl.get_warehouse())
skl.give_from_warehouse(warehouse, s,2)      # перемещаем обратно на основной склад
print('склады end', warehouse.get_warehouse(), skl.get_warehouse())
