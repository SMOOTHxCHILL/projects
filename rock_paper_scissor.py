import random
choices = ('r', 'p', 's')
while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices :
        print("Invalid input")
    
    computer_choice = random.choice(choices)
    print(f"You chose {user_choice} and computer chose {computer_choice}")
    if user_choice == computer_choice :
        print("Tie!")
    elif ((user_choice == 'r' and computer_choice == 's') or      (user_choice == 's' and computer_choice == 'p') or      (user_choice == 'p' and computer_choice == 'r')) :
            print("You win!")
    else  :
        print("You lose!")
        
    input_continue = input("Wanna continue?(y/n): ").lower()
    if input_continue == 'y' :
        continue
    elif input_continue == 'n' :
        print("Byee!")
        break
