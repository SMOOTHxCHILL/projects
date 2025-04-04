import random
while True :
    x = input("Roll the dice (y/n): ").lower()
    if x == 'y' :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif x == 'n' :
        print("Thanks for playing")
        break
    else :
        print("Invalid choice!")
