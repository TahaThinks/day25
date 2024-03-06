import pandas

data = pandas.read_csv("weather_data.csv")
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
data_dict = {
    "students":["Amy", "James", "Angela"],
    "scores":[76, 56, 65]
}