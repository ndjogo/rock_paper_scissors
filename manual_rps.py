
import random
computer_choice = []
def get_computer_choice(): 
    answer = random.choice(["Rock", "Paper", "Scissors"])
    computer_choice.append(answer)


user_choice = []
def get_user_choice():
    print("Please enter your choice:")
    answer = input() 
    user_choice.append(answer)
    
get_computer_choice()
get_user_choice() 

def get_winner(computer_choice, user_choice):

    if computer_choice[0] == "Rock" and user_choice[0] == "Rock":
        print ("This is a draw")
    elif computer_choice[0] == "Rock" and user_choice[0] == "Scissors":
        print ("The computer wins")
    elif computer_choice[0] == "Rock" and user_choice[0] == "Paper":
        print ("The user wins")
    elif computer_choice[0] == "Paper" and user_choice[0] == "Rock":
        print ("The computer wins")
    elif computer_choice[0] == "Paper" and user_choice[0] == "Scissors":
        print ("The user wins")
    elif computer_choice[0] == "Paper" and user_choice[0] == "Paper":
        print("This is a draw")
    elif computer_choice[0] == "Scissors" and user_choice[0] == "Rock":
        print ("The user wins")
    elif computer_choice[0] == "Scissors" and user_choice[0] == "Scissors":
        print ("This game is a draw")
    elif computer_choice[0] == "Scissors" and user_choice[0] == "Paper":
        print("The computer wins") 

    print( f"The computer's choice was:{computer_choice[0]} " )
    print( f"The user's choice was: {user_choice[0]}" )


get_winner(computer_choice, user_choice)
