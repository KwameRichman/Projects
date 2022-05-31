import random

logo = ("""   _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\
                                                                                                      
                                                                                                      """)

print(logo)
print("Welcome to Richman's Number Guessing Game!!!\n\n ")
choice = input("Choose a difficulty level. Type 'easy' or 'hard': ")
print("\n\nI'm thinking of a number between 1 and 100\n\n")

the_number = random.randint(1,100)
#print(the_number)
attempts = 0
end_of_game = False

if choice == 'easy':
    attempts += 10
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts += 5
    print(f"You have {attempts} attempts remaining to guess the number")

while not end_of_game:
    guessed_number = int(input("Make a guess: "))
    if the_number == guessed_number:
        end_of_game = True
        print("AWESOME! You guessed right. You WIN!!! =D")
    elif guessed_number > the_number:
        attempts -= 1
        print("Too high!")
        if attempts == 0:
            end_of_game = True
            print(f"I had {the_number} in mind. You've run out of guesses. You LOSE!!! =(")
        else:
            print("Guess again.\n")
            print(f"You have {attempts} attempts remaining to guess the number.")
    elif guessed_number < the_number:
        attempts -= 1
        print("Too low!")
        if attempts == 0:
            end_of_game = True
            print(f"I had {the_number} in mind. You've run out of guesses. You LOSE!!! =(")
        else:
            print("Guess again.\n")
            print(f"You have {attempts} attempts remaining to guess the number.")
            