import requests
from pprint import pprint
from datetime import datetime


def wind_rose(wind_direction):
    if 0 < wind_direction <= 22.5:
        rose = 'N'
    elif 22.5 < wind_direction <= 67.5:
        rose = 'NE'
    elif 67.5 < wind_direction <= 112.5:
        rose = 'E'
    elif 112.5 < wind_direction <= 157.5:
        rose = 'SE'
    elif 157.5 < wind_direction <= 202.5:
        rose = 'S'
    elif 202.5 < wind_direction <= 247.5:
        rose = 'SW'
    elif 247.5 < wind_direction <= 292.5:
        rose = 'W'
    elif 292.5 < wind_direction <= 337.5:
        rose = 'NW'
    elif 292.5 < wind_direction <= 360:
        rose = 'N'
    return rose


def get_daily_forecasts(city, days = 14):

    url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
    url += '?appid=d1526a9039658a6f76950cff21823aff'
    url += '&units=metric'
    url += '&mode=json'
    url += '&lang=nl'
    url += f'&cnt={days}'
    url += '&q=' + city

    print(url)

    response = requests.get(url)

    print(response.status_code)

    data = response.json()

    pprint(data)

    daily_forecast = []
    for day_forecast in data['list']:
        dt = datetime.fromtimestamp(day_forecast['dt'])
        temp = day_forecast['temp']['day']
        min_temp = day_forecast['temp']['min']
        max_temp = day_forecast['temp']['max']
        wind_speed = round((day_forecast['speed']/0.836)**(2/3), 1)   # W = 0.836B ** (3/2) => B = (W / 0.836) ** (2/3)
        wind_degrees = day_forecast['deg']
        wind_direction = wind_rose(day_forecast['deg'])

        print(dt, min_temp, temp, max_temp, wind_speed, wind_degrees, wind_direction)

        daily_forecast.append({'dt': dt,
                               'min_temp': min_temp,
                               'max_temp': max_temp,
                               'temp': temp,
                               'wind_speed': wind_speed,
                               'wind_degrees': wind_degrees,
                               'wind_direction': wind_direction})

    return daily_forecast


daily_forecast = get_daily_forecasts(city='Lemmer', days=14)

pprint(daily_forecast)
