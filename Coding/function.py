def odd_even(a,b):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(odd_even(6,7))

# Question 5
# Write a function that takes two strings and then do the following operations
# Replace all the occurrences of first character in the string of greater length with the first character of smaller string.
# Note if length of both strings are equal then take first string as longer string.
# Replace both lower case and upper case occurrences

def string(a,b):


string("Dog","Lemon")
#
if repeat == "yes":
    num_1 = int(input("Enter your first number: "))
    operator = input("Enter the operator which are:\nadd\nsubtract\nmultiply\ndivide\n")
    num_2 = int(input("Enter your second number: "))

    if operator == "add":
        addition(num_1, num_2)
    elif operator == "subtract":
        subtraction(num_1, num_2)
    elif operator == "multiply":
        multiplication(num_1, num_2)
    elif operator == "divide":
        division(num_1, num_2)
if repeat == "no":
    print("Thank you for using the calculator ")
