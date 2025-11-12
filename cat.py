
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Meow, my name is {self.name}, {self.age} years old and I am 🐈."

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Sally', 2)
cat2 = Cat('Jim', 3)
cat3 = Cat('Ben', 2.5)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):

    oldest = args[0]

    for cat in args[1:]:
        if cat.age > oldest.age:
            oldest = cat

    return oldest

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(oldest_cat(cat1, cat2, cat3))


