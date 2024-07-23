import csv

i = 0
while i < 10:
    date = input("Date: ")
    temperature = int(input("Temperature(F): "))
    
    with open("nyc_weather.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "temperature"])
        writer.writerow({"date": date, "temperature": temperature})
    i += 1
