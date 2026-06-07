import random

print('----Welcome to the Number Guessing Game----')
computer = random.randint(1,100)
# computer = 100

print('Choose a number between 1 and 100')
num = int(input("Enter: "))

if num not in range(1,101):
    print("Invalid Choice!")

else:    
    count = 1
    while(num != computer):
        if num > computer:
            print("Too High!")
            num = int(input("Enter:")) 

        elif num < computer:
            print("Too low!")   
            num = int(input("Enter:"))    

        count+=1       
            
    print("You guess it right!")
    print(f"You take {count} attempts for guess the right number")
    print("Thanks for Playing!")
                


