# Jan 11
# Rock Paper Scissor

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissor: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won !"

    return "You lost! "

def is_win(player,opponent):
    # return true if player wins
    if(player == "r" and opponent == "s" or player == "s" and opponent == "p" \
    or player == "p" and opponent == "r"):
         return True

print(play())