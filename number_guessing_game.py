import random
from colorama import Fore, Style, init


init(autoreset=True)


def get_difficulty():
    print("Choose difficulty: Easy (10 guesses), Medium (7 guesses), Hard (5 guesses)")
    while True:
        choice = input("Enter difficulty (easy/medium/hard): ").lower()
        if choice == "easy":
            return 10
        elif choice == "medium":
            return 7
        elif choice == "hard":
            return 5
        else:
            print(Fore.RED + "Invalid choice, try again.")


def play_game():
    secret_number = random.randint(1, 100)
    max_guesses = get_difficulty()
    guess_count = 0


    print(Fore.YELLOW + f"\nI'm thinking of a number between 1 and 100. You have {max_guesses} guesses. Good luck!\n")


    while guess_count < max_guesses:
        try:
            guess = int(input(Fore.CYAN + "Enter your guess: "))
            guess_count += 1


            if guess < secret_number:
                print(Fore.BLUE + "Too low! Try again.")
            elif guess > secret_number:
                print(Fore.BLUE + "Too high! Try again.")
            else:
                print(Fore.GREEN + f" Correct! The number was {secret_number}.")
                print(Fore.GREEN + f"You guessed it in {guess_count} tries.\n")
                return
            
            print(Fore.MAGENTA + f"Guesses left: {max_guesses - guess_count}")

        except ValueError:
            print(Fore.RED + "Please enter a valid number.")


    print(Fore.RED + f" Sorry, you're out of guesses. The number was {secret_number}.\n")


def main():
    print(Fore.YELLOW + "Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input(Fore.YELLOW + "Play again? (yes/no): ").lower()
        if again != "yes":
            print(Fore.YELLOW + "Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()