import random

number = random.randint(1,100)
while True :
    guess = int(input("Guess the number between 1 to 100: "))
    if guess > number :
        print("Too high!")
    elif guess < number :
        print("Too low!")
    else :
        print("Congratulations! You guessed the number")
        break
