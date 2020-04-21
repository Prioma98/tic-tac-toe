import pandas
import requests
from bs4 import BeautifulSoup
page=requests.get('https://forecast.weather.gov/MapClick.php?lat=33.9425&lon=-118.409#.XnrX9PkzbIU')
soup=BeautifulSoup(page.content,'html.parser')
# print(soup)
week_forecast_all=soup.find(id='seven-day-forecast-body')
print(week_forecast_all)
week_forecast=soup.find_all(class_="tombstone-container")
# print(week_forecast)
# print(week_forecast[0])
# print(week_forecast[0].find(class_="period-name").get_text())
# print(week_forecast[0].find(class_="short-desc").get_text())
# print(week_forecast[0].find(class_="temp").get_text())

item_1=[items.find(class_="period-name").get_text()for items in week_forecast]
item_2=[items.find(class_="short-desc").get_text()for items in week_forecast]
item_3=[items.find(class_="temp").get_text()for items in week_forecast]

weather_stuff=pandas.DataFrame(
  {"period":item_1,
  "short_descriptions":item_2,
  "temperature":item_3
})
#print(weather_stuff)

weather_stuff.to_csv("web_scraping:)")