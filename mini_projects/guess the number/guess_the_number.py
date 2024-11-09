import random

# Get the lower and upper bounds for the random number
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enetr upper bound: "))

# Generate a random number between the lower and upper bounds
number_to_guess = random.randrange(lower_bound,upper_bound)

# Ask the user for the number of chances (attempts) they have to guess
chance_count = int(input("Enter chance count: "))
guess_count = 0

while guess_count < chance_count:
    guess_count += 1
    your_guess = int(input("Enter a number: "))

    # Check if the guess is correct
    if your_guess == number_to_guess:
        print(f"You won, the number is {number_to_guess}, you found it right in the {guess_count} attempt")
        exit()
    elif your_guess > number_to_guess:
        print("Your guess is higher")
    else:
        print("Your guess is lower")

# If the loop ends and the number wasn't guessed, print the correct number
print(f"The number is {number_to_guess} better luck next time")


