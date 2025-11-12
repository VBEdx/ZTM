from functools import reduce
from itertools import accumulate

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(str.capitalize, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))
# print(list(zip(my_strings, my_numbers.sort()))) ==> sorts the list and returns None
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def greater_50(x):
    return x > 50

print(list(filter(greater_50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accum(acc, x):
    return acc + x

print(reduce(accum, scores, reduce(accum, my_numbers, 0)))

print(reduce(accum, my_numbers + scores))

# using lambda function
print(reduce(lambda acc, x: acc + x, my_numbers, 0))
print(reduce(lambda acc, x: acc + x, my_numbers)) # without zero

# exercises

my_list = [5,4,3]
print(list(map(lambda x: x**2, my_list)))

a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key = lambda x: x[1])
print(a)

some_list = ['a', 'b', 'c', 'd', 'i', 'a', 'g', 'd', 'b']

duplicates = list({item for item in some_list if some_list.count(item)>1})
print(duplicates)