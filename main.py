import random
import time
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def start_the_game(diff):
    random_number = random.randint(1, 100)
    print("The game starts now.")
    attempts = diff
    number_isnt_guessed = True
    start = time.time()
    while number_isnt_guessed:
        print("Enter your guess:")
        guessed_num_input = input().strip()
        
        try:
            guessed_num = int(guessed_num_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guessed_num > random_number:
            attempts -= 1
            print(f"Incorrect! The number is less than {guessed_num}\nNumber of attempts left: {attempts}")
            if attempts == 0:
                print(f"\nSorry, you've run out of attempts. The number was {random_number}.")
                print("Would you like to try again?")
                tryagain()
                number_isnt_guessed = False
        elif guessed_num < random_number:
            attempts -= 1
            print(f"Incorrect! The number is greater than {guessed_num}\nNumber of attempts left: {attempts}")
            if attempts == 0:
                print(f"\nSorry, you've run out of attempts. The number was {random_number}.")
                print("Would you like to try again?")
                tryagain()
                number_isnt_guessed = False
        else:
            end = time.time()
            
            print(f"Congratulations! You guessed the correct number in {diff - attempts} attempts.\n it took you {end - start}")

def diff_selector():
    while True:
        print("\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
        choice = input().strip()
        
        if choice == "1":
            start_the_game(10)
            break
        elif choice == "2":
            start_the_game(5)
            break
        elif choice == "3":
            start_the_game(3)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def tryagain():
    while True:
        print("\n1. Yes\n2. No")
        choice = input().strip()
        if choice == "1":
            diff_selector()
            break
        elif choice == "2":
            print("Goodbye!")
            exit()
        else:
            print("Please enter a valid choice (1 or 2).")

diff_selector()