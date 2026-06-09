print('----Currency Converter----')

curr = True
while curr:
    amount = int(input('Enter the amount in INR: '))
    print('Choose the in which you want to convert(USD/EUR/CAD):')
    change = input('Choose: ')


    if change.lower() == 'usd':
        print(f'Your amount in USD : {amount*95.40}')

    elif change.lower() == 'eur':
        print(f'Your amount in EUR : {amount*110.16}')  

    elif change.lower() == 'cad':
        print(f'Your amount in CAD : {amount*68.31}')   

    print('Do you want to convert more: (y/n)')
    d = input('Choose: ')
    if d.lower() == 'y':
        curr = True
    else:
        curr = False
print("Thank You!")            
    


