import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ("rock", "paper", "scissors"):
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_again():
    return input("Do you want to play again? (y/n): ").lower() == "y"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScores - You: {user_score}, Computer: {computer_score}\n")

        if not play_again():
            break

    print("Thank you for playing Rock-Paper-Scissors!")

if __name__ == "__main__":
    main()
