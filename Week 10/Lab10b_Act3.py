####################################################################
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# I have not given or received any unauthorized aid on this assignment.
# Class and Section: ENGR 102 556
# Assignment: Lab10b_Act3
# Name: Francis Gabriel Anos
# Date: 11/15/21
####################################################################

weather_data = open('CLLWeatherData.csv','r')

month = input("Please enter a month:")
year = input("Please enter a year:")

def output(print):
    print("3-year maximum temperature:", tempmax,'"F')
    print("3-year minimum temperature:", min_temp, " F")
    print("3-year average daily precipitation: ", round((totalprecip / dcount), 3), " in.")
    print("Percentage of >=90% Humidity: ", round(((100 * precip_90) / dcount), 1), " % of days")
    print("Percentage when precipitation was 0: ", round(((100 * precip_zero) / dcount), 1),
          " % of days")
    print("Average Temperature for last 3 yrs: ", round(avg_temp / dcount, 2), " F")
    print("Average Dew Point for last 3 yrs: ", round(avg_dew / dcount, 2), " units")
    print("Average Humidty for last 3 yrs: ", round(avg_humid / dcount, 2), " units")
    print("Average Pressure for last 3 yrs: ", round(avg_pressure / dcount, 2), " units")

tempmax = 0
tempmin = 1000
totalprecip = 0
precip_90 = 0
precip_zero = 0
dcount = -1

with open(weather_data) as f:
    for line in f:
        dcount += 1
        data = line.split(",")
        if dcount == 0:
            continue

        avg_temp = 0
        avg_dew = 0
        avg_humid = 0
        avg_pressure = 0

        avg_temp += float(data[2])
        avg_dew += float(data[5])
        avg_humid += float(data[8])
        avg_pressure += float(data[11])

        tempmax2 = float(data[1])
        tempmin2 = float(data[3])
        precipitation = float(data[-1])
        if precipitation == 0:
            precip_zero += 1
        elif float(data[7]) >= 90:
            precip_90 += 1
            totalprecip += precipitation
        if tempmax < tempmax2:
            tempmax = tempmax2
        if tempmin > tempmin2:
            tempmin = tempmin2

output(print)