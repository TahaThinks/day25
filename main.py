import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp[0]
# monday_temp_f = (monday_temp_c * 9/5) + 35
# print(monday_temp_f)

# Create a datafame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

raw_data = pandas.read_csv("squirrel_raw_data.csv")
squirrels_fur_color = raw_data["Primary Fur Color"]
# print(squirrels_fur_color)
cinnamon = 0
black = 0
gray = 0

for squirrel_fur_color in squirrels_fur_color:
    if squirrel_fur_color == "Gray":
        gray += 1
    elif squirrel_fur_color == "Cinnamon":
        cinnamon += 1
    elif squirrel_fur_color == "Black":
        black += 1

color_dict = {
    "Fur Color":["grey", "red", "black"],
    "Count": [gray, cinnamon, black]
}

colors_count = pandas.DataFrame(color_dict)
colors_count.to_csv("squirrel_count.csv")