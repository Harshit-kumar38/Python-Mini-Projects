import random
print("----Welcome to the dice rolling game----")

print("Do you want to roll the dice?(y/n)")
a = input("Choose: ").lower()

if(a!='y' and a!='n'):
    print("Invalid Choice!")

else:

    if (a == 'y'):
        count=0
        while (a == 'y'):
            print(f'{random.randint(1,6),random.randint(1,6)}')
            print("Do you want to play again!")
            a = input("")
            count+=1
            
    print(f"You rolled the dice {count} times")
    print("Thanks for Playing!")            