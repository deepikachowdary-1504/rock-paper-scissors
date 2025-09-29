import random

print("*********_ Welcome to the Rock Paper Scissors Game _*********")
print("Enter 0 for Rock ✊")
print("Enter 1 for Paper ✋")
print("Enter 2 for Scissors ✌️")

# List to map numbers to emojis
choices = ["✊ Rock", "✋ Paper", "✌️ Scissors"]

user_choice = int(input("Enter your choice: "))

if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid choice, you lose.")
else:
    computer_choice = random.randint(0, 2)
    print("You chose:", choices[user_choice])
    print("Computer chose:", choices[computer_choice])

    if user_choice == computer_choice:
        print("It is a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win!")
