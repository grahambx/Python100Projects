# Udemy 100 Projects in 100 days
# Day 16 Project
# COFFEE MACHINE - OOP VERSION
# Skills: OOP, Modules, Libraries, Classes, Objects
# Notes: Pasted into both Copilot and Gemini for critique: well-structured, functional etc.
# My blind output now very similar in approach to course


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

in_use = True
while in_use:
    drink = input(f"What would you like? ({menu.get_items()}): ")
    if drink == 'off':
        in_use = False
    elif drink == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
            else:
                print("Sorry that's not enough money. Money refunded.")
