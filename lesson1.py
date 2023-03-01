# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'

for i in st:
    if i.isdigit():
        print(i, end=',')

# #################################################################################
# 2)написати прогу яка вибирає з введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

print()
st = 'as 23 fdfdg544 34'
st1 = ', '.join(''.join(i if i.isdigit() else ' ' for i in st).split())
print(st1)

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
print()
greeting = 'Hello, world'

arr = list(greeting.upper())
print(arr)

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

arr = [i ** 2 for i in range(50) if i % 2 != 0]

print(arr)


#
# function
#
# - створити функцію яка виводить ліст

def func(list):
    print(list)


func([1, 2, 3])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_return(a, b, c):
    max_num = max([a, b, c])
    print(max_num)
    return max_num


max_return(1, 2, 3)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def max_and_min(*args):
    min_num = min(args)
    max_num = max(args)
    print(max_num)
    return min_num


max_and_min(2, 1, 4, 5, 0)


# - створити функцію яка повертає найбільше число з ліста

def max_from_list(list):
    return max(list)


print(max_from_list([1, 3, 2, 5, 3]))


# - створити функцію яка повертає найменьше число з ліста

def min_from_list(list):
    return min(list)


print(min_from_list([1, 3, 2, 5, 3]))


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def join_list(list):
    string = ''
    for number in list:
        string += str(number)

    return string


print(join_list([1, 2, 20]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg(list):
    return sum(list) / len(list)


print(avg([1, 2, 3, 4, 5]))

# ################################################################################################
# 1)Дан list:
list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - знайти мін число
print(min(list1))

#   - видалити усі дублікати
print(list(set(list1)))


#   - замінити кожне 4-те значення на 'X'
def to_x():
    print(['X' if not (i + 1) % 4 else value for i, value in enumerate(list1)])


to_x()


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


def func(x):
    for i in range(x):
        if i == 0 or i == x - 1:
            print('*' * x)
        else:
            print('*' + ' ' * (x - 2) + '*')


func(10)

# 3) вывести табличку множення за допомогою цикла while
i = 1
while i < 10:
    j = 1
    while j < 10:
        res = i * j
        print(f"{res:4}", end='')
        j += 1
    print()
    i += 1
