# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from typing import Callable


def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        return todo_list

    return get_all, add_todo


x = notebook()

x[1]('washing')
print(x[0]())
x[1]('playing')
print(x[0]())


# 2) протипізувати перше завдання

def notebook() -> tuple[Callable[[str], None], Callable[[], list]]:
    todo_list: list[str] = []

    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list:
        return todo_list

    return add_todo, get_all


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
print()


def sum_of_digits(some_x: int) -> str:
    arr_numbers: list[str] = []

    ltg = len(str(some_x))
    compare_num: str = '0'

    while ltg > 0:
        num = some_x % 10 ** ltg
        number = f"{str(num)[0] + '0' * len(str(num)[1:])}"

        if number == compare_num:
            ltg -= 1
            continue
        else:
            compare_num = number
            arr_numbers.append(number)

            ltg -= 1

    return " + ".join(arr_numbers)


print(sum_of_digits(7054243504))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій
print()


def decor(func):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(f"count: {count}")
        func()
        print("*" * 20)

    return inner


@decor
def func1():
    print("func1")


@decor
def func2():
    print("func2")


func1()
func2()

func1()
func1()

func2()
