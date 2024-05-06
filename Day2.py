# Udemy 100 Projects in 100 days
# Day 2 Project
# RESTAURANT BILL SPLITTER
# Type Conversion -- F String
print("Welcome to the tip calculator!")
cost = float(input("What was the total bill? "))
tip_rate = int(input("How much tip do you want to give? (5, 10, 15): "))
customers = int(input("How many customers do we need to split the bill for? "))
split = (cost + cost*tip_rate/100)/customers
print(f"Each person pays: £{split:.2f}")
