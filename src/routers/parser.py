import requests
from bs4 import BeautifulSoup

from config import URL


fish_weather = requests.get(URL)

soup = BeautifulSoup(fish_weather.text, 'html.parser')

# блоки температуры по дням
''' Today '''

# for temp in soup.find_all('div', class_='temperature'):
    # температура по часам
    # temp_2 =
    # temp_8 =
    # temp_14 =
    # temp_20 =

''' Tomorrow '''

#

''' On five day'''

#