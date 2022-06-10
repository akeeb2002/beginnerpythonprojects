import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissor ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It is a tie")
    else:
        if is_win(user, computer):
            print("You won!")
        else:
            print("You lost!")


def is_win(player, opponent):
    if(player=='s' and opponent=='p') or (player=='p' and opponent=='r') or (player=='r' and opponent=='s'):
        return True

    return False


play()
