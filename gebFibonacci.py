def fib(n):
    previous = 0
    current = 1
    for i in range(n):
        yield previous
        new_current = previous + current
        previous = current
        current = new_current


for x in fib(21):
    print(x)
