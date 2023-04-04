MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# getting the user deposit as well as their bet
def deposit():
    # continuosly asking using for the deposit amount until they give a valid amount
    while True:
        amount = input("What would you like to deposit? $")
        # checking if amount is number
        if amount.isdigit(): # isdigit is telling us if its a valid whole number
            # we need a numeric value for our deposit becuase its string  by default
            amount = int(amount)
            # checking if number is greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount
# collecting bet from user 
def get_number_lines():
       # continuosly asking using for the deposit amount until they give a valid amount
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
        # checking if amount is number
        if lines.isdigit(): # isdigit is telling us if its a valid whole number
            # we need a numeric value for our deposit becuase its string  by default
            lines = int(lines)
            # checking if number is greater than 0
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def main():
    balance = deposit()
    lines = get_number_lines()   
    print(balance,lines)                                                                                                                                                           

main()            
                