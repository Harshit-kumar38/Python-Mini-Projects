print('----Password Strength checker----')

password = input('Enter your password: ')

for i in range(0,10):
    if i in password:
        print('Weak')
        

for i in range(65,98):
    if chr(i) in password:
        print('String')
        break