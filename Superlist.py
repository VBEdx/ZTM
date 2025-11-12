class Superlist(list):
    def __len__(self):
        return 1000

a = Superlist()
a.append(1)
a.append(5)
a.append(8)
print(a)
print(len(a))
print(isinstance(a, list))
