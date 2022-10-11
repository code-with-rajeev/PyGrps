import threading
print(threading._allocate_lock().__dict__)
def x():
    for i in range(10):
        print(4)
y = threading.Thread(target = x)
y.start()