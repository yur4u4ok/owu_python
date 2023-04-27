import threading

print(threading.current_thread().name)

# def show(n):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#
#
# thread1 = threading.Thread(target=show, args=(5,), name='thr-1')
# thread2 = threading.Thread(target=show, args=(8,), name='thr-2')
#
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
#
# print("MAIN")


count = 0


def inc():
    with threading.Lock():
        global count
        count += 1
        print(count)


threads = []
for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()
