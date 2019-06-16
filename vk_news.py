import requests
from bs4 import BeautifulSoup


def get_news():
    url = 'https://news.mail.ru'
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    links = markup.find_all('a', {'class': 'list__text'})

    news = ['{}\nПодробнее по ссылке: {}'.format(link.text, link['href'])
            for link in links
            if 'http' in link['href']]

    news.extend(['{}\nПодробнее по ссылке: '.format(link.text) + url + link['href']
                 for link in links
                 if 'http' not in link['href']])

    return '\n\n'.join(news)
