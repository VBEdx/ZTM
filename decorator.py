from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(end - start)
        return result
    return wrapper


@performance
def my_func():
    for i in range(100000000):
        i*5

my_func()
