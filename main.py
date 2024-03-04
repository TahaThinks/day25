data = []

with open("weather_data.csv") as file:
    for line in file:
        data.append(line.rstrip())

print(data)