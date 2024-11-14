import random


choices = ["rock", "paper", "scissors"]


while 1==1:
    print("Choices: rock, paper, scissors")
    user_choice = input("Enter your choice (or 'exit' to quit): ").lower()
    
    if user_choice == "exit":
        print("Thanks for playing!")
        break
    elif user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose: ", computer_choice)

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
        