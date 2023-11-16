from datetime import datetime
import math
years = {}
filename = "WeatherData.csv"
f = open('CLLWeatherData.csv','r')
data = f.read().split('\n')
colNames = data[0].split(',')
data = data[1:]
f.close()

max_temp = int(data[0].split(",")[1])
min_temp = int(data[0].split(",")[3])
avg_precipitation = 0


for i in data:
  temp = i.split(",")
  try:

    if int(temp[1]) > max_temp:
      max_temp = int(temp[1])
    if int(temp[3]) < min_temp:
      min_temp = int(temp[3])

    avg_precipitation = float(avg_precipitation) + float(temp[-1])
  except:
    pass
avg_precipitation = round((avg_precipitation / len(data)) , 2)
print(f"3-year maximum temperature: {max_temp} F")
print(f"3-year minimum temperature: {min_temp} F")
print(f"3-year averange Precipitation: {avg_precipitation} F")

month = input("\nEnter a month: ")
year = int(input("Enter a year: "))

avg_low_temp = 0
count = 0
count_of_days_for_humidity = 0
avg_percipitation = 0
for i in data:
    temp = i.split(",")
    date_string = temp[0]
    try:
      date_str = datetime.strptime(date_string, '%m/%d/%Y')
      if date_str.strftime("%B") == month and date_str.year == year:
        avg_low_temp += int(temp[3])
        count += 1

      if int(temp[8]) < 75:
        count_of_days_for_humidity += 1

      avg_percipitation += float(temp[-1])
    except:
      pass

avg_low_temp = avg_low_temp/count
count_of_days_for_humidity = round((count_of_days_for_humidity/len(data)) * 100, 2)
avg_percipitation = round(avg_percipitation/ len(data), 4)

sd_of_percipitation = 0

for i in data:
  temp = i.split(",")
  try:
    sd_of_percipitation += (float(temp[-1]) - avg_percipitation)**2
  except:
    pass

sd_of_percipitation = round(math.sqrt(sd_of_percipitation / float(len(data) - 1)), 4)
print(f"\nFor {month} {year} : ")
print(f"Average low temperature: {avg_low_temp} F")
print(f"Percentage of days with average humidity below 75%: {count_of_days_for_humidity} %")
print(f"Mean daily precipiataion: {avg_percipitation} inches")
print(f"Standard deviation of  daily precipiataion: {sd_of_percipitation} inches")