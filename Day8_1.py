# Udemy 100 Projects in 100 days
# Day 8 Learning
# PRIME NUMBER CHECKER
# Skills: Functions, Parameters, Modulus
# Notes:

def prime_checker(number):
    is_prime = True
    for number_to_check in range(2, number):
        if not number_to_check == number:
            if number % number_to_check == 0:
                is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(4)
