# number Guesing Game
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low! Try Again.")
    elif guess > secret:
        print("Too high! Try Again.")
    else:
        print("Congratulations! You guessed the number.")