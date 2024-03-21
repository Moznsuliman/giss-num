
import random

def game():
    is_even: bool = random.choice([True, False])
    number_to_guess: int = random.randint(1, 10) if is_even else random.randint(11, 20)
    guess = None
    attempts = 0

    while guess not in (number_to_guess, (number_to_guess - 1) if is_even else (number_to_guess + 1)):
        guess = int(input(f"Guess an even number between 1 and 10 or an odd number between 11 and 20: "))
        attempts += 1
        if guess not in (number_to_guess, (number_to_guess - 1) if is_even else (number_to_guess + 1)):
            if guess % 2 != is_even:
                print("Incorrect parity!")
            elif guess < (number_to_guess - 1) if is_even else (number_to_guess - 1):
                print("Too low!")
            else:
                print("Too high!")
    
    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    game()