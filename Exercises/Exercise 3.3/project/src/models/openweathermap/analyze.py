import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('agg')


def build_chart(data, city='unknown'):
    day_temps = [day_forecast.temp_day for day_forecast in data]
    night_temps = [day_forecast.temp_night for day_forecast in data]
    day_offsets = list(range(len(day_temps)))
    day_labels = [day_forecast.week_day for day_forecast in data]
    ndays = len(day_temps)

    plt.plot(day_offsets, day_temps, marker='o', color='darkblue', label='day')
    plt.plot(day_offsets, night_temps, marker='o', color='darkblue', label='night')
    plt.fill_between(day_offsets, night_temps, day_temps, color='lightblue')
    plt.xticks(day_offsets, day_labels)
    plt.ylim(0, 35)
    plt.grid()
    plt.legend()
    plt.title(f'Forecast at {city} for the comming {ndays} days')
    plt.savefig('src/flask/static/chart.png')
    plt.close()
