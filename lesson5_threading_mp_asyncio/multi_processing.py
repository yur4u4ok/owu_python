import math
import multiprocessing
import time
from multiprocessing import freeze_support


def decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


def worker(num):
    return str(math.sqrt(math.sqrt(num / 2) * 5)) + 'H'


@decor
def write_file():
    with open('file1.txt', 'w') as file:
        for i in range(10000000):
            res = worker(i)
            print(res, file=file)


write_file()


# @decor
# def mp():
#     count = multiprocessing.cpu_count()
#     print(count)
#
#     with multiprocessing.Pool(count) as p:
#         numbers = range(10000000)
#         with open('file2.txt', 'w') as file:
#             res = p.map(worker, numbers)
#             for item in res:
#                 print(item, file=file)
#
#
# if __name__ == '__main__':
#     mp()
