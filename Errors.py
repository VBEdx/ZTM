my_logs = []
while True:
    try:
        age = input('What is your age? : ')
        10/int(age)
    except ValueError:
        print('Sorry, try to enter a number.')
    except ZeroDivisionError as err:
        print(f'Sorry, try to enter a number greater than zero. \n{err}')
    else:
        print(f'Your age is {age}, thank you')
        break
    finally:
        # this executes no matter what
        # good use of it is keep ing logs
        my_logs.append(age)

print(my_logs)
