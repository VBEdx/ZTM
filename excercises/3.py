# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the
# following input is supplied to the program: 8

n = int(input('provide a integer number: '))

my_dic = {i: i**2 for i in range(1, n+1)}
print(my_dic)