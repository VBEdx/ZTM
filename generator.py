def generator_function(num):
    for i in range(num):
        yield i*2 # yield pauses the function

g = generator_function(50)
next(g)
print(next(g))
print(next(g))