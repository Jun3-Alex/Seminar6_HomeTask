# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
'''
a1 = int(input(f'Введите первый элемент прогрессии: '))
d = int(input(f'Введите шаг прогрессии: '))
n = int(input(f'Введите количество элементов прогрессии: '))

def arithm_prog(a1, d, n):
    prog_list = list()
    an = 0
    for i in range(1, n + 1):
        an = a1 + (i - 1) * d
        prog_list.append(an)
    return prog_list

print(arithm_prog(a1, d, n))
'''

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
'''
def generate_list(n):
    list_ = []
    for i in range(n):
        elements = int(input(f'Введите элемент массива: '))
        list_.append(elements)
    return list_

def index_of_range(list_1, minimum, maximum):
    if minimum < maximum:
        index_list = []
        for i in range(len(list_1)):
            if minimum <= list_1[i] <= maximum:
                index_list.append(i)
        return index_list
    else:
        print(f'Введите корректные границы диапозона.')

n = int(input(f'Введите количество элементов массива: '))
list_1 = generate_list(n)

minimum = int(input(f'Задайте минимум диапозона: '))
maximum = int(input(f'Задайте максимум диапозона: '))

print(f'Индексы элементов входящих в диапозон:{index_of_range(list_1, minimum, maximum)}')
'''
