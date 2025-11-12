from functools import reduce

def multiply_2(x):
    return x * 2

 # map
print(list(map(multiply_2, [1,2,3,4])))

# filter
def greater_2(x):
    return x > 2
def only_odd(x):
    return x % 2 == 1

print(list(filter(greater_2, [1,2,3,4])))
print(list(filter(only_odd, [1,2,3,4])))

# zip, takes two iterables and combines to a tuple

names = ['vadim', 'ben', 'charlie']
surnames = ['belotcaci', 'watkin', 'sheen']
farher_names = ['valeriu', 'henry', 'will']

print(list(zip(names, surnames)))

print(list(zip(names, surnames, farher_names)))

# reduce
my_list = [1, 2, 3,8, 13]

def accumulator(acc, x):
    return acc + x

print(reduce(accumulator, my_list, 0))
