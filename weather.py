import requests
from bs4 import BeautifulSoup
from yandex.Translater import Translater


def get_weather(city):
    token = '<your_token>'

    if city != '':
        translator = Translater(token, city, 'ru', 'en')
        translated = translator.translate().lower().replace(' ', '-')
    else:
        translated = 'moscow'

    url = 'https://yandex.ru/pogoda/' + translated
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    try:
        weather_in_city = markup.find_all('div', {'class': 'main-title__title-wrap'})[0].text\
                          + ':'
    except IndexError:
        return 'Неправильный параметр команды'

    temperature = markup.find('span', {'class': 'temp__value'}).text + '°'

    weather_condition = markup.find('div', {'class': 'link__condition'}).text

    feels_like = markup.find('dt', {'class': 'term__label'}).text
    feels_like_temperature = markup.find_all('span', {'class': 'temp__value'})[1].text + '°'
    sense = feels_like + ' ' + feels_like_temperature

    humidity = 'Влажность: ' + markup.find_all('dd', {'class': 'term__value'})[3].text

    pressure = 'Давление: ' + markup.find_all('dd', {'class': 'term__value'})[-2].text

    try:
        # может быть 'Штиль', а не направление ветра
        wind_direction = markup.find('abbr', {'class': 'icon-abbr'})['title']
    except TypeError:
        wind_direction = 'Ветер: '

    # просто красиво форматирую вывод
    wind_condition = markup.find_all('dd', {'class': 'term__value'})[2].text.strip('СЮЗВ') +\
        wind_direction[7:].title()
    wind = wind_direction[:7] + wind_condition

    return '\n'.join((weather_in_city, weather_condition, temperature,
                      sense, humidity, pressure, wind))
