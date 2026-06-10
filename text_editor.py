print('----Welcome to Our Text Editor----')

print('What you want\n1. Open a Existing file\n2. Create a new file')

choice = int(input('Choose between(1/2): '))

if choice == 1:
    file = input('Enter your file name: ').strip()
    print('What you want to do with this file:\n1. Read this file\n2. Delete older content and add new content\n3. Add new content with existing content ')
    feature = int(input('Enter your choice(1/2/3): '))

    dict = {
        1 : 'r',
        2 : 'w',
        3 : 'a'
    }
    try:
        if feature == 1:
            with open(file,dict[feature]) as f:
                data = f.read()
                print(data)

        elif feature == 2:
            content = input('Enter what you want to enter: ')
            with open(file,dict[feature]) as f:
                f.write(content)
            print('\nYour data added successfully!')    

        elif feature == 3:
            content = input('What you want to add in file: ')
            with open(file,dict[feature]) as f:
                f.write(content)
            print('\nYour data added successfully!')  

    except:  
        print(f'{file} is not found the directory!')  

elif choice == 2:
    new_file = input('Enter the file name: ')
    print('What you want to do with this file: ')
    print('1. Only Create the file\n2. Add new content')
    dict_2 = {
        1 : 'r',
        2 : 'w'
    }

    feature = int(input('What you want(1/2): '))
    if feature == 1:
        with open(new_file,dict_2[feature]) as f:
            f.read()
        print('Your file created successfully')

    elif feature == 2:
        data = input('What you want to add: ')
        with open(new_file,dict_2[feature]) as f:
            f.write(data)
        print('Your data is added Successfully!')    


# I want to add the loop in this tomorrow