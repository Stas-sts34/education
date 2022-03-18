import pprint


# n = int(input('сколько позиций надо внести?'))
product = []
dict = {}

# for i, _ in enumerate(range(n), 1):
#     name = input('введите название товара')
#     price = int(input('введите цену товара'))
#     number = int(input('введите кол-во товара'))
#     unit = input('введите ед.измерения')
#     globals()[f'dict{i}'] = {}
#     globals()[f'dict{i}']['название'] = name
#     globals()[f'dict{i}']['цена'] = price
#     globals()[f'dict{i}']['количество'] = number
#     globals()[f'dict{i}']['eд'] = unit
#     tuple = i, globals()[f'dict{i}']
#     product.append(tuple)

product = [(1, {'название': 'q', 'цена': 2, 'количество': 2, 'eд': 'q'}), (2, {'название': 'w', 'цена': 2, 'количество': 2, 'eд': 'w'})]
total_dict = {name for name in product}
total_list = []
for i in product:
    # total_dict['название'] = [name for name in i[1]['название']]
    total_list.append(i[1]['название'])

print(total_dict, total_list)
    # for j in i[1]:
    #     print(j)




# pprint.pprint(product)
# print(product)
# print(product[0] is product[1])
