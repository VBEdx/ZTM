user_name = input('user name: ')
user_password = input('user password: ')
hidden_password = "*" *len(user_password)
print(f'{user_name}, your password is {hidden_password} is {len(user_password)} letters long')
