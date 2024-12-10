import random

print("חיפוש בינארי")

setMIN = 0
setMAX = 100
secretNumber = random.randint(setMIN, setMAX)

counter = 0
correct = False

print("Start guessing!")

while not correct:
    try:
        numGuessed = int(input(f"Throw a number between {setMIN} and {setMAX}: "))
        counter += 1

        if numGuessed < secretNumber:
            print("Greater")
        elif numGuessed > secretNumber:
            print("Lower")
        else:
            correct = True
    except ValueError:
        print("Please enter a valid number.")

print(f"VICTORY! You guessed the number in {counter} guesses.")