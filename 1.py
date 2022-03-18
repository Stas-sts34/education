
n = int(input('сколько позиций надо внести?'))
product = []
dict = {}

for i, _ in enumerate(range(n), 1):
    name = input('введите название товара')
    price = int(input('введите цену товара'))
    number = int(input('введите кол-во товара'))
    unit = input('введите ед.измерения')
    globals()[f'dict{i}'] = {}
    globals()[f'dict{i}']['название'] = name
    globals()[f'dict{i}']['цена'] = price
    globals()[f'dict{i}']['количество'] = number
    globals()[f'dict{i}']['eд'] = unit
    tuple = i, globals()[f'dict{i}']
    product.append(tuple)


total_dict = {}
total_name = []
total_price = []
total_number = []
total_unit = []
for i in product:
    total_name.append(i[1]['название'])
    total_price.append(i[1]['цена'])
    total_number.append(i[1]['количество'])
    total_unit.append(i[1]['eд'])

total_dict['название'] = total_name
total_dict['цена'] = total_price
total_dict['количество'] = total_number
total_dict['ед'] = total_unit

print(total_dict)






