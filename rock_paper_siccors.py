import random
import getpass

# dataset
data = {
        "paper": "rock",
        "scissors": "paper",
        "rock": "scissors"
    }

# Conditions
def result_analysis(choice_1, choice_2):
    if ((choice_1 in data) and (choice_2 in data)):
        if(choice_1 == choice_2):
            print("Its a tie")
        elif(data[choice_1] == choice_2):
            print(f"{player_1} wins!")
        else:
            print(f"{player_2} wins!")
    else:
        print("invalid input")


# working
play = 1
while(play):

    mode= int(input("enter no. of players [ 1 , 2 ]"))

    if(mode == 2):
        player_1 = input("Enter Player 1 name : ")
        player_2 = input("Enter Player 2 name : ")

        choice_1 = getpass.getpass((f"{player_1} Enter your choice [ rock, paper, scissors ]")).strip().lower()
        choice_2 = getpass.getpass((f"{player_2} Enter your choice [ rock, paper, scissors ]")).strip().lower()

        result_analysis(choice_1, choice_2)

    else:
        player_1 = input("Enter Player 1 name : ")
        player_2 = "Computer"

        choice_1 = getpass.getpass((f"{player_1} Enter your choice [ rock, papper, scissors ]")).strip().lower()
        choice_2 = random.choice(list(data.keys()))

        result_analysis(choice_1, choice_2)

    play = int(input("If you want to play type '1' otherwise '0'"))
print("Thanks For Playing!!")

