import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

"""
This code scrap 10 days weather for Warsaw and make a table with the informations.
Also saves it into a .csv file.
"""



# Make connection with URL.
page = requests.get("https://www.worldweatheronline.com/warsaw-weather/pl.aspx")
soup = BeautifulSoup(page.content, "html.parser")

# Catch container that have containers with needed information.
containers = soup.find(class_="weather_tb tb_day tb_days_10")

# Take all names, dates, descriptions of each day.
day_Name = containers.find_all(class_="wh_day_week")
day_Date = containers.find_all(class_="wh_date")
day_Description = containers.find_all(class_="wh_light")

days = [" "]
descriptions = [" "]

# Selecting each day with it's date and add it to list 'days' and description to different list 'descriptions'.
for k, v in enumerate(day_Name):
    name = v
    for a in range(1):
        day = day_Date[k]
        for b in range(1):
            descr = day_Description[k]

    fusion = name.text + " " + day.text
    days.append(fusion)
    descriptions.append(descr.text)

# Write 2 lists to .csv file as 2 rows.
with open("weather.csv", "w", newline="") as file:
    thewriter = csv.writer(file)
    thewriter.writerow(days)
    thewriter.writerow(descriptions)


# Writing every parameter from table from website to .txt file.
rows = containers.find(class_="tb_content")

with open("weather_10_days.txt", "w") as file:
    for row in rows.find_all("div"):
        for cell in row.find_all(class_="tb_cont_item"):
            file.write(cell.text + ",")
        file.write("+")

# Separate each day and make list of days parameters
with open("weather_10_days.txt", "r") as file:
    data = file.read()
    x = data.split("+++++++++++++++")

# Add each day parameters as a row
with open("weather.csv", "a", newline="") as file:
    thewriter = csv.writer(file)

    x.pop(-1)
    for k, v in enumerate(x):
        z = x[k].split(",")
        z.pop(-1)
        thewriter.writerow(z)

# Using pandas open .csv file and make a table.
df = pd.read_csv("weather.csv", sep=",",  encoding='latin-1')
print(df.head())

# Save as a final .csv file.
df.to_csv("weather.csv")



