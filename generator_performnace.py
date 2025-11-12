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
def long_time(n):
    print(f'method with generators (embedded in range)')
    for i in range(n):
        i**2

@performance
def long_time2(n):
    print(f'method with list')
    for i in list(range(n)):
        i**2

long_time(100000000)
long_time2(100000000)