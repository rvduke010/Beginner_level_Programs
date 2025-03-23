import random
def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(player,computer):
    if player== computer:
        return "tie match"
    elif (player=='rock'and computer=='scissors') or \
         (player=='scissors'and computer=='paper') or \
         (player=='paper' and computer=='rock'):
        return "you won"
    else:
        return("computer win")

def rock_paper_scissors():
    print("welcome to game ")
    choices=['rock','paper','scissors']
    while True:
        player_choice=input("Enter your choice [type quit if want exit]:").lower()
    

        if player_choice == "quit":
            print('thanks for playing')
            break
        elif player_choice not in choices:
            print('Invalid answer,try again')
            continue
        
        computer_choice = get_computer_choice()
        print(f'computer choice:{computer_choice}')
        print(determine_winner(player_choice,computer_choice))

rock_paper_scissors()


