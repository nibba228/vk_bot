import requests
import random
import re
from bs4 import BeautifulSoup
from pprint import pprint


def get_genre_values():
    url = 'https://afisha.tut.by/online-cinema/?'
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    genre_values = [genre['value'] for genre in markup.find('select', {'class': 'multiple-select'}).find_all('option')]
    return genre_values


def get_genre_names():
    url = 'https://afisha.tut.by/online-cinema/?'
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    genre_names = [genre.text.lower()
                   for genre in markup.find('select', {'class': 'multiple-select'}).find_all('option')] + \
                  [markup.find_all('span')[-1].text]
    return '\n'.join(genre_names[:-1])


def get_film(genre):
    genre_values = get_genre_values()
    genre_names = get_genre_names().split('\n')
    genres_values = dict(zip(genre_names, genre_values))

    try:
        url = 'https://afisha.tut.by/online-cinema/?&tag[]=' + genres_values[genre.lower()]
    except KeyError:
        return 'Неправьлиный параметр'

    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    films = [film.a['href'] for film in markup.find_all('li', {'class': 'lists__li'})]

    random_film = random.choice(films)

    url = random_film
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    # TODO: image
    name_pattern = '.*"(.*)"'

    try:
        name = markup.find('h1', {'id': 'event-name'}).text + '\n'
    except AttributeError:
        name = 'Фильм не найден'
    try:
        duration = 'Длительность: ' + markup.find('td', {'class': 'duration'}).text + '\n\n'
    except AttributeError:
        duration = ''
    try:
        raw_genres = [genre.a.text for genre in markup.find('td', {'class': 'genre'}).find_all('p')]
        genres = 'Жанры: ' + (', '.join(raw_genres)) + '\n' if len(raw_genres) == 1 else raw_genres[0] + '\n'
    except AttributeError:
        genres = 'Жанры: ' + genre + '\n'
    rate = 'Рейтинг IMDb: ' + markup.find('td', {'class': 'IMDb'}).text[14:17] + '\n'

    description = markup.find('div', {'id': 'event-description'}).h2.next_sibling + '\n'

    message = name + duration + genres + rate
    message += 'О фильме\n' + description.replace('\t', '').replace('                ', '') if description != '' \
        else 'Описание не найдено'

    return message
