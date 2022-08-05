dice = int(input("How many dice would you like to roll? "))
side = int(input("How many sides should each die have? "))
from random import randint

while True:
    reply = input("Roll again? (q to quit)")
    print(randint(1,num_sides))
    if reply == "q":
        break


