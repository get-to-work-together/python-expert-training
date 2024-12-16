import requests

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')


class DayForecast:

    def __init__(self, day_forecast):
        self.dt = day_forecast['dt']
        self.day = datetime.fromtimestamp(self.dt)
        self.day_formatted = self.day.strftime('%d %B')
        self.week_day = self.day.strftime('%a')
        self.temp_day = round(day_forecast['temp']['day'])
        self.temp_night = round(day_forecast['temp']['night'])
        self.weather = day_forecast['weather'][0]['description']
        self.wind_speed = day_forecast['speed']
        self.wind_direction = day_forecast['deg']

    def __str__(self):
        return f'{self.week_day} {self.day_formatted} {self.temp_day} {self.temp_night} {self.weather} {self.wind_speed} {self.wind_direction}'

    def as_dict(self):
        return self.__dict__

    @property
    def wind_rose(self):
        if 0 < self.wind_direction <= 22.5:
            rose = 'N'
        elif 22.5 < self.wind_direction <= 67.5:
            rose = 'NE'
        elif 67.5 < self.wind_direction <= 112.5:
            rose = 'E'
        elif 112.5 < self.wind_direction <= 157.5:
            rose = 'SE'
        elif 157.5 < self.wind_direction <= 202.5:
            rose = 'S'
        elif 202.5 < self.wind_direction <= 247.5:
            rose = 'SW'
        elif 247.5 < self.wind_direction <= 292.5:
            rose = 'W'
        elif 292.5 < self.wind_direction <= 337.5:
            rose = 'NW'
        elif 292.5 < self.wind_direction <= 360:
            rose = 'N'
        return rose

def get_data(city, days=14):

    # openweathermap api
    url = "http://api.openweathermap.org/data/2.5/forecast/daily"
    url += "?appid=d1526a9039658a6f76950cff21823aff"
    url += "&units=metric"
    url += "&mode=json"
    url += "&lang=nl"
    url += f"&cnt={days}"
    url += "&q=" + city

    # print(url)

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    else:
        return None


def get_formatted_data(city, days=14):

    data = get_data(city, days)

    daily_forecasts = []
    for day_forecast in data['list']:
        daily_forecasts.append(DayForecast(day_forecast))

    return daily_forecasts



if __name__ == '__main__':

    data = get_formatted_data('Soesterberg', 7)

    for day_forecast in data:
        print(day_forecast)
