import json

with open('questions.json','r') as f:
    data = json.load(f)

print('----Quiz game----')

category = list(data.keys())
print('Available Categories: ')

for i , section in enumerate(category,start=1):
    print(f'{i}.{section}')

choice = int(input('Choose your category: '))
selected = category[choice-1]

difficulties = list(data[selected].keys())
print("\nAvailable Difficulty Levels:")

for i, level in enumerate(difficulties, start=1):
    print(f"{i}. {level}")

diff_choice = int(input("\nChoose difficulty level: "))
selected_difficulty = difficulties[diff_choice - 1]

questions = data[selected][selected_difficulty]

score = 0
print('----Start Quiz----')
for q in questions:
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], start=1):
        q["options"] = ["Mumbai", "Delhi", "Chennai", "Kolkata"]
        print(f"{i}. {option}")


    answer = int(input("Enter your answer (1-4): "))

    selected_option = q["options"][answer - 1]

    print("You selected:", repr(selected_option))
    print("Correct answer:", repr(q["answer"]))

    if selected_option.strip().lower() == q["answer"].strip().lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", q["answer"]) 

print("\n---- QUIZ COMPLETED ----")  
print(f"Your Score: {score}/{len(questions)}")
percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%") 


if percentage >= 80:
    print('Excellent!')

elif percentage >=60:
    print('Good!')

else:
    print('Please Improve yourself in this subject!')

print('Thanks for Playing!')    


#In this code there are many error should to improve


