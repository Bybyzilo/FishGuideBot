# Парсер прогноза клёва рыбалки

from bs4 import BeautifulSoup

import aiohttp


async def fishing_forecast():
    ''' Получение прогноза клева с сайта'''

    url = 'https://russian.fishing/forecast/rybalka-rostov-na-donu-758/'

    data = {}
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(url, headers=headers)
        text = await response.text()

        soup = BeautifulSoup(text, 'lxml')


    forecast = soup.find_all('div', class_="forecasting")

    for element in forecast:
        date = element.find(class_="forecast-date").find('i').text

        data[date] = {
		    'day': None,
		    'air_temp': None,
		    'pressure': None,
		    'wind': None,
		    'moon_phase': None,
            'discription': None
	    }

        # Достаёт день недели и суёт в словарь
        day = element.find(class_="forecast-date").find('span').text
        data[date]['day'] = day


        # Достаёт температуру и суёт в словарь
        air_temp = element.find(class_='detailed-forecast').find_all('i')[4].text
        temp = ' '.join(air_temp.split())
        data[date]['air_temp'] = temp


        # Достаёт давление и суёт в словарь
        pressure = element.find(class_='detailed-forecast').find('i').text
        data[date]['pressure'] = pressure


        # Достаёт ветер и суёт в словарь
        wind = element.find(class_='detailed-forecast').find_all('i')[1].text
        data[date]['wind'] = wind


        # Достаёт фазу луны и суёт в словарь но почему то не переводится в текст
        moon_phase = element.find(class_='detailed-forecast').find_all('i')[11]
        moon_phase = str(moon_phase).replace('<i>', '').replace('</i>', '')
        data[date]['moon_phase'] = moon_phase

        # Достаёт сам прогноз
        discription = element.find(class_='forecasting-description').find('span').text
        data[date]['discription'] = discription

    return data