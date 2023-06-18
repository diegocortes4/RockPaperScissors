import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("Your choice (1-3): "))
    computer_choice = random.randint(1, 3)

    print("You chose:", get_choice_name(user_choice))
    print("Computer chose:", get_choice_name(computer_choice))

    result = determine_winner(user_choice, computer_choice)
    print(result)

def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"
    else:
        return "Invalid choice"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Play the game
play_game()
