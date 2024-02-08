import random
randomNumber = random.randint(1, 100)

print("Guess the Number Game!!!")
print("I am thinking of a number between 1 and 100.")
print(randomNumber)
while True:
    guess = int(input("What is your first guess?"))
    if (guess == randomNumber):
        print("You guessed it!")
        answer = input("Do you want to play again? y - n >")
        if (answer == "y"):
            randomNumber = random.randint(1, 100)
        else:
            break
    elif (guess > randomNumber):
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

print("Goodbye!")