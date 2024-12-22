# Udemy 100 Projects in 100 days
# Day 10 Project
# CALCULATOR
# Skills: Functions, Recursion, Dictionary
# Notes:

# Define basic arithmetic functions
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# create a dictionary that will be used to convert a user selected symbol to one of the functions defined above
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# create a string of the operator options which will be used as a prompt
operator_str = ""
for key in operations:
    operator_str += key
    operator_str += " "

# Define calculator function
# Asks user for first number
# We use a while loop for operator + second number, the while loop supports using an answer as base for next calc
# A user may decide to start over, so we exit the loop and use function recursion to start again
def calculator():
    num1 = float(input("What's the first number? :"))

    to_continue = True

    while to_continue:
        operator = input(f"Please choose the operation from ( {operator_str}): ")
        num2 = float(input("What's the second number? :"))
        calc_function = operations[operator]
        answer = calc_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calc. : ") == "y":
            num1 = answer
        else:
            to_continue = False
            calculator()


# Start the calculator
calculator()
