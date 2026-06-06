import random

computer = random.choice([1,-1,0])

print('----Stone Paper Scissor----')
print('Stone --> S')
print('Paper --> P')
print('Scissor --> Sc')

print()

youStr = input("Enter your choice: ").strip()

youDict = {
    'S': -1,
    'P': 0,
    'Sc': 1
}
reverseDict ={-1 : 'Stone', 0: 'Paper' , 1 : 'Scissor'}

if youStr not in youDict:
    print("Invalid Choice")
    exit()

you = youDict[youStr]

print(f"You choose {reverseDict[you]} and computer choose {reverseDict[computer]}")


if (you==computer):
    print("Draw!")

else:
    if(you == -1 and computer == 0):
        print("You Lose!")
    elif(you == -1 and computer == 1):
        print("You Win!")
    elif(you == 0 and computer == -1):
        print("You Win!")
    elif(you == 0 and computer == 1):
        print("You Lose!")
    elif(you == 1 and computer == -1):
        print("You Lose!")
    elif(you == 1 and computer == 0):
        print("You Win!")
    else:
        print("Something gone wrong!")                            


