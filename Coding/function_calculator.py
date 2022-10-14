# Function Calculator

def addition(a, b):
    print(a + b)


def subtraction(a, b):
    print(a - b)


def multiplication(a, b):
    print(a * b)


def division(a, b):
    print(a / b)


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

repeat = input("Do you want to continue? yes or no: ")
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





