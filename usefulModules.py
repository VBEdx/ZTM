from collections import Counter, defaultdict, OrderedDict
import pdb

li = [1,2,3,4,5,6,7,7,]
print(Counter(li))
sentence = 'blah blah blah thinking about learning python'
print(Counter(sentence))

dictionary = defaultdict(int, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
dictionary2 = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

print(dictionary['z'])
print(dictionary2['z'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d2= OrderedDict()
d2['c'] = 2
d2['d'] = 1

print(d==d2)

d_regular = {'c': 3, 'a': 1, 'b': 2}
d_regular2 = {'c': 3, 'b': 2, 'a': 1}
print(d_regular == d_regular2)

def add(a,b):
    pdb.set_trace()
    return a + b

add(1,'2')
