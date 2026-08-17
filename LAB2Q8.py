import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

max_attempts = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.")

while attempts < max_attempts:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Correct! 🎉")
        print("You guessed the number in", attempts, "attempt(s).")
        break

# If all attempts are used
if attempts == max_attempts and guess != secret_number:
    print("\nSorry! You have used all 7 attempts.")
    print("The correct number was:", secret_number)