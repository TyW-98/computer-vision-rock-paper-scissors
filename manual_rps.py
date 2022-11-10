import random

def get_computer_choice():
    comp_choice = random.choice(["rock","paper","scissors"])
    return comp_choice

def get_user_choice():
    choice = input("Rock, Paper or Scissors? : ")
    return choice

def get_winner(user_choice,computer_choice):
    
    if user_choice == "scissors" and computer_choice== "paper":
        print("You won!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == computer_choice:
        print("It is a tie!")
    else:
        print("You lost")
        
def play():
    comp_choice = get_computer_choice()
    print(comp_choice)
    user_choice = get_user_choice()
    print(user_choice)
    get_winner(user_choice,comp_choice)

play()