import vk_api
import requests
from bs4 import BeautifulSoup


def download_audio(vk, dialog_id):  # пока только с одной песней
    try:
        audios = vk.messages.getHistory(peer_id=dialog_id, count=1)
        
        attachments_count = 0
        for counter in audios['items'][0]['attachments']:
            if counter['type'] == 'audio':
                attachments_count += 1

        if attachments_count == 0:
            raise vk_api.VkApiError

        title = audios['items'][0]['attachments'][0]['audio']['title']
        artist = audios['items'][0]['attachments'][0]['audio']['artist']
    except vk_api.VkApiError:
        return 'Нет подходящего вложения'

    url = 'https://mp3-tut.com/search?query=' + title + ' ' + artist
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    audio = markup.find_all('div', {'class': 'audio-list-entry'})[0]

    link = audio.find('div', {'class': 'download-container'}).find('a')['href']

    short_link = vk.utils.getShortLink(url=link, private=0)['short_url']

    message = '''Вот твоя ссылка на скачивание "{} - {}": {}.
                Если название песни при загрузке отличается, то,
                поверь, содержимое - нет.'''.format(artist, title, short_link)

    return message
