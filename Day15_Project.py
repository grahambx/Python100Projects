# Udemy 100 Projects in 100 days
# Day 15 Project
# COFFEE MACHINE
# Skills: Functions, Modules, Dictionary, Constants
# Notes: Pasted into both Copilot and Gemini for critique: well-structured, functional etc.
# My blind output now very similar in approach to course


# Global immutable constant
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Global mutable variable
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


def generate_report():
    """Returns current resources in coffee machine"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: ${resources["money"]:.2f}")


def check_resources(drink):
    """checks sufficient resources in coffee machine for the drink selected. Returns Bool"""
    missing_resources = []
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if amount > resources[ingredient]:
            missing_resources.append(ingredient)
    if missing_resources:
        print(f"Sorry there is not enough {' and '.join(missing_resources)}.")
        return False
    else:
        return True


def get_money():
    """Requests money from user, returns amount as float"""
    value = 0.00
    print("Please insert coins.")
    value += int(input("How many quarters?: ")) * 0.25
    value += int(input("How many dimes?: ")) * 0.10
    value += int(input("How many nickles?: ")) * 0.05
    value += int(input("How many pennies?: ")) * 0.01
    return value


def update_resources(drink):
    """removes used resources for given drink and adds money value"""
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    resources["money"] += MENU[drink]["cost"]


def coffee_machine():
    in_use = True
    while in_use:
        operation = input("What would you like? (espresso/latte/cappuccino):")
        if operation == "report":
            generate_report()
        elif operation == "off":
            in_use = False
        elif operation in ("espresso", "latte", "cappuccino"):
            if check_resources(operation):  # check enough resources for given drink
                # get money from customer and calculate provisional change
                amount_paid = get_money()
                change = amount_paid - MENU[operation]["cost"]
                if change >= 0:  # if customer has paid enough
                    update_resources(operation)
                    if change != 0:  # if customer paid exact amount
                        print(f"Here is ${change:.2f} dollars in change")
                    print(f"Here is your {operation} ☕. Enjoy!")
                else:
                    print("Sorry that is not enough money. Money refunded.")


coffee_machine()
