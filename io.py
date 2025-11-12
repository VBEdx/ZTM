my_file = open("test.txt")

print(my_file.read())
my_file.seek(0) # moves the cursor to beginning
print(my_file.read())
my_file.seek(0)
print(my_file.readline()) # reads 1st line
print(my_file.readline()) # reads 2nd line
print(my_file.readline()) # 3rd line

my_file.seek(0)
print(my_file.readlines()) # list of lines
my_file.close()

with open("test.txt", mode='r+') as f:
    # read and write mode, where the cursor is set to zero
    text = f.write('hey, it\'s me, writing a sentence in the file')
    print(text)

with open("test.txt", mode='a') as f:
    # opens the file in append mode
    text = f.write('hey, it\'s me, writing a sentence in the file')
    print(text)


try:
    with open("test2.txt", mode='r') as f:
        print(f.read())
except FileNotFoundError as err:
    print('file does not exist')
    print(err)
except IOError as err:
    # issues with IO operations
    print(err)

