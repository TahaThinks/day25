import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperatues = []
    for row in data:
        temperatues.append(int(row[1]))

    print(temperatues)