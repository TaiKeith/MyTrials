# 2.  nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#       i. What was the temperature on Jan 9?
#      ii. What was the temperature on Jan 4?

#  Figure out data structure that is best for this problem
weather_dict = {}

with open("nyc_weather.csv","r") as file:
    for line in file:
        tokens = line.split(",")
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            ("Invalid temperature. Ignore the row")

print(weather_dict)

print(weather_dict["Jan 9"])
print(weather_dict["Jan 4"])

# The data structure best for use is a Dictionary because we want access to key,value pairs looking up elements by day key with a complexity of O(1)
