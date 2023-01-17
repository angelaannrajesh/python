# 11 Jan
# Number Guesser for Computer to guess

def computer_guess(x):
    low = 1
    high = x # creating boundaries for guessing
    feedback = "" # we do this to not have the computer return a empty string
    while feedback != "c" :# while feedback is not c for correct 
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f"Is guess too high(H), too low(L), or correct (C)").lower()
        if feedback == "H":
            high = guess-1
        elif feedback == "L":
            low = guess+1
        
print("Yay, the computer guessed your number")
    