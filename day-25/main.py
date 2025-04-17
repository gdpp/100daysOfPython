# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data["temp"].to_list()

# print(temp_list)

# print(sum(temp_list) / len(temp_list))

# print(data['temp'].mean())

import pandas

data = pandas.read_csv('squirrels.csv')

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")