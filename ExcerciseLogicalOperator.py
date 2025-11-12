from multiprocessing.reduction import duplicate

is_magician = input("are you magician ?").strip().lower() =="yes"
is_expert = input("are you expert ?").strip().lower() == "yes"

if is_magician and is_expert:
    print("You are master magician")
elif is_magician and not is_expert:
    print("at least you are getting there")
else:
    print("You need magic power")

counter = 0
my_list = [1,2,3,4,5,4,3,5,6,7,6,5]

for _ in my_list:
    counter += 1
print(counter)

#Exercise!
picture = [ [0,0,0,1,0,0,0],
      [0,0,1,1,1,0,0],
      [0,1,1,1,1,1,0],
      [1,1,1,1,1,1,1],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0]]

print('\n')

for row in picture:
    print('\n', end='')
    for col in row:
        if col == 0:
            print(' ', end='')
        elif col == 1:
            print('*', end='')


some_list = ['a', 'b', 'c', 'b', 'e', 'f', 'a', 'b', 'i', 'j']

duplicate_list = []
for item in some_list :
    if some_list.count(item) > 1 and item not in duplicate_list:
        duplicate_list.append(item)
print(duplicate_list)