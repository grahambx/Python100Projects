# Udemy 100 Projects in 100 days
# Day 25 Learning
# INTRO TO PANDAS
# Skills: Pandas, Csv
# Notes:

import pandas

data = pandas.read_csv("2018_squirrel_data.csv")                    # convert a csv to a dataframe
cinnamon_rows = len(data[data["Primary Fur Color"] == "Cinnamon"])  # restrict color filtered rows and use len to count
gray_rows = len(data[data["Primary Fur Color"] == "Gray"])
black_rows = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {                                                       # create a dict in desired format
    "Fur Colour": ["Gray", "Red", "Black"],
    "Count": [gray_rows, cinnamon_rows, black_rows]
}

df = pandas.DataFrame(data_dict)                                    # convert the dict to a dataframe
df.to_csv("squirrel_count.csv")                                     # convert and save the dataframe to csv
