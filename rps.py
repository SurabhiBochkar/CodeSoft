import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_Aky_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, Aky_choice):
    if user_choice == Aky_choice:
        return "tie"
    elif (
        (user_choice == "rock" and Aky_choice == "scissors")
        or (user_choice == "scissors" and Aky_choice == "paper")
        or (user_choice == "paper" and Aky_choice == "rock")
    ):
        return "user"
    else:
        return "Aky"

user_score = 0
Aky_score = 0

while True:
    print("Rock-Paper-Scissors Game")
    user_choice = get_user_choice()
    Aky_choice = get_Aky_choice()

    print(f"You chose: {user_choice}")
    print(f"Aky chose: {Aky_choice}")

    result = determine_winner(user_choice, Aky_choice)
    if result == "user":
        user_score += 1
        print("You win this round!")
    elif result == "Aky":
        Aky_score += 1
        print("Aky wins this round!")
    else:
        print("It's a tie!")

    print(f"User Score: {user_score}, Aky Score: {Aky_score}")

    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")