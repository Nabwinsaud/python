import random
chars='abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123490!@,&#'
print('Passsword:::::::generator:::')
length=int(input('Enter the length of password:'))

for i in range(length):
    password=''
    password=random.choice(chars)
    print(password,end='')




