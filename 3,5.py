def func_count(list_numbers):
    ''' вычисляет сумму цифр из полученного списка'''
    return sum([int(item) for item in list_numbers])

result = '0'
while True:
    numbers = input('Введите числа через пробел\n')
    list_numbers = numbers.split()          # преобразуем список из строки без пробелов

    if 'x' in list_numbers:         # проверяем на налииче спец символа
        indx = list_numbers.index('x')
        del list_numbers[indx:]
        list_numbers.append(result)
        result = func_count(list_numbers)
        print('сумма:', result)
        print('exit')
        break
    list_numbers.append(result)
    result = func_count(list_numbers)
    print('сумма:', result)
