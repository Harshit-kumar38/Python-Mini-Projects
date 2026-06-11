print('----Password Strength checker----')

password = input('Enter your password: ')

isUpper = False
isLower = False
isSpecial = False
isNumber = False

Special = '!@#$%^&*'

for char in password:
    if char.isupper():
        isUpper=True

    elif char.islower():
        isLower = True

    elif char in Special:
        isSpecial = True

    elif char.isdigit():
        isNumber = True

if len(password)>8:

    if isNumber == True and isUpper==True and isLower==True and isSpecial==True:
        print('Strong Password')

    else:
        print('Moderate password')

else:
    print('Password length should be atleast 8 characters')
                

                



