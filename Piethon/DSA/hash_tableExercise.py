# 1. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#       i. What was the average temperature in first week of Jan
#      ii. What was the maximum temperature in first 10 days of Jan

# Figure out data structure that is best for this problem
arr = []

with open("nyc_weather.csv","r") as file:
    for line in file:
        tokens = line.split(",")
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature. Ignore the row")
print(arr)

# 1st week = 7 days = arr[0:7]
avg = sum(arr[0:7])/len(arr[0:7])
print("Average temperature in first week:", avg)

# 1st ten days of Jan = arr[0:10]
print("Maximum temperature in 1st 10 days:", max(arr[0:10]))

# The best data structure to use was a List because all we wanted was access of temperateure elements
