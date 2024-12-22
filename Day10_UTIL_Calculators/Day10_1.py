# Udemy 100 Projects in 100 days
# Day 10 Learning
# LEAP YEAR & DAYS OF MONTH
# Skills: Functions, Return, DocString
# Notes: Evolution of previous leap year calculator

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Take year and month and return number of days in month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


days = days_in_month(2020, 2)
print(days)

days = days_in_month()
