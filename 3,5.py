'''
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
 При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
  ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых
  чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

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
