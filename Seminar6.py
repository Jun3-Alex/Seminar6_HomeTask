# Задача №39. Общее обсуждение
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
'''
def generate_list(n):
    list_ = []
    for i in range(n):
        elements = int(input(f'Введите элемент массива: '))
        list_.append(elements)
    return list_

def difference(list_1, list_2):
    list_ = []
    for i in list_1:
        if i not in list_2:
            list_.append(i)
    return list_

n = int(input(f'Введите количество элементов первого массива: '))
list_1 = generate_list(n)
m = int(input(f'Введите количество элементов первого массива: '))
list_2 = generate_list(m)
list_3 = difference(list_1,list_2)
print(list_3)
'''
# Задача №41. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
'''
def generate_list(n):
    list_ = []
    for i in range(n):
        elements = int(input(f'Введите элемент массива: '))
        list_.append(elements)
    return list_
def bigger_neighbor(list_1):
    count = 0
    # for i in list_1:
    #     if i == 0:
    #         if list_1[i] > list_1[len(list_1) - 1] and list_1[i] > list_1[i + 1]:
    #             count +=1
    #     if i == len(list_1):
    #         if list_1[i] > list_1[i - 1] and list_1[i] > list_1[0]:
    #             count += 1
    #     if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1]:
    #         count += 1
    for i in range(1, len(list_1) - 1):
        if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1]:
            count += 1
    return count

n = int(input(f'Введите количество элементов массива: '))
list_1 = generate_list(n)

count = bigger_neighbor(list_1)
print(count)
'''
# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
'''
def generate_list(n):
    list_ = []
    for i in range(n):
        elements = int(input(f'Введите элемент массива: '))
        list_.append(elements)
    return list_

def duet_friends(list_1):
    count = 0
    for i in range(len(list_1) - 1):
        for j in range(i + 1, len(list_1)):
            if list_1[i] == list_1[j]:
                count += 1
    return count

n = int(input(f'Введите количество элементов массива: '))
list_1 = generate_list(n)

print(duet_friends(list_1))
'''


# Задача №45. Общее обсуждение
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:  Вывод:
# 300    220 284

'''
def get_summ(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += i
    return count


k = 300
for num_1 in range(1, k):
    num_2 = get_summ(num_1)
    sum_del_num_2 = get_summ(num_2)
    
    if (num_1 == sum_del_num_2) and (num_1 != num_2) and (num_1 < num_2):
        print(num_1, num_2)
'''
