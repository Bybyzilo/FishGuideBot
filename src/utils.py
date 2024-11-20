# Дополнительные функции и методы для работы с ботом

from bs4 import BeautifulSoup

import aiohttp


async def fishing_forecast():
    """ Получение прогноза клева с сайта 
    Не пытайся понять, что за пи**ец тут написано, я его сделал используя костыыли
    """

    url = 'https://rybalku.ru/prognoz/ru/rostov%20oblast/rostov-on-don/temernik'

    data = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(url, headers=headers)
        text = await response.text()

        soup = BeautifulSoup(text, 'lxml')


    data_elements = soup.select(".grid__header.grid__nav__list__item.grid__nav__list--desk_current > time")
    for i in data_elements:
        data[i['datetime']] = {
            'date': i.next.strip(),
            'air_temp': [],
            'water_temp': [], 
            'cloudiness': [], 
            'pressure': [],
            'humidity': []
        }


    air_temp = soup.find_all('div', class_="grid__by_hiding")
    o = -1
    for i in air_temp:
        temp_el = i.find_all(class_="temperature")
        if temp_el: 
            o += 1
        
        for j in temp_el:
            date = list(data.keys())[o]
            data[date]['air_temp'].append(j.find(class_='cel').text.strip())



    water_temp = soup.select('.grid__by_hiding.temperature')
    for k, i in enumerate(water_temp):
        date = list(data.keys())[k]

        for j in i.find_all(class_='cel'):
            data[date]['water_temp'].append(j.text.strip())


    subcol = soup.select('.grid__subcol.grid__by_hiding')

    cloudiness = subcol[15:20]
    for k, i in enumerate(cloudiness):
        date = list(data.keys())[k]

        for kj, j in enumerate(i.find_all('div')):
            if kj % 2 == 0:
                data[date]['cloudiness'].append(j.text.strip())
        
        

    pressure = subcol[25:30]
    for k, i in enumerate(pressure):
        date = list(data.keys())[k]

        divs = i.find_all(class_="mmhg")
        for k in divs:
            data[date]['pressure'].append(k.text.strip())


    humidity = subcol[30:35]
    for k, i in enumerate(humidity):
        date = list(data.keys())[k]

        for kj, j in enumerate(i.select('div > div')):
            if kj % 2 == 0:
                data[date]['humidity'].append(j.text.strip())

    return data