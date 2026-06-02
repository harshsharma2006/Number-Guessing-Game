import random

def start_game():
    print("\n--- Welcome to the Number Guessing Game ---")
    print("Computer ne 1 se 100 ke beech ek number soch liya hai.")
    print("Kya aap use guess kar sakte hain?\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Apna number guess karein (1-100): "))
            attempts += 1


            if user_guess == secret_number:
                print(f"Badhai ho! Aapne {attempts} attempts mein sahi number pakad liya!")
                print(f"Secret Number tha: {secret_number}")
                break
            
            elif user_guess > secret_number:
                print("Too High! (Number should be smaller))")
            
            else:
                print("Too Low! (Number should be bigger)")

        except ValueError:
            print("Error: Only Numbers are allowed!!")

start_game()