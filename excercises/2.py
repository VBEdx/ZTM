# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
# sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

n = int(input('please provide the number factorial should be computed for: '))
factorial=1
for i in range(1, n+1):
    factorial *= i

print(factorial)

print('==== method 2 ====')

def shortFact(x): return 1 if x <= 1 else (x*shortFact(x-1))
print(shortFact(n))