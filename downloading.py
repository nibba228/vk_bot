import vk_api
import requests
from bs4 import BeautifulSoup


def download_audio(vk, dialog_id):  # пока только с одной песней
    try:
        audios = vk.messages.getHistory(peer_id=dialog_id,
                                        count=1)
        attachments_count = 0
        attachments_indices = []
        attachments = audios['items'][0]['attachments']
        
        for attachment in attachments:
            if attachment['type'] == 'audio':
                attachments_count += 1
                attachments_indices.append(attachments.index(attachment))

        if attachments_count == 0:
            raise vk_api.VkApiError

        titles = [audios['items'][0]['attachments'][i]['audio']['title']
                  for i in attachments_indices]
        
        artists = [audios['items'][0]['attachments'][i]['audio']['artist']
                   for i in attachments_indices]
    except vk_api.VkApiError:
        return 'Нет подходящего вложения'

    urls = ['https://mp3-tut.com/search?query=' + titles[i] + ' ' + artists[i]
            for i in range(len(attachments_indices))]
    
    responses = [requests.get(urls[i]) for i in range(len(urls))]
    
    markups = [BeautifulSoup(responses[i].content, 'html.parser')
               for i in range(len(responses))]

    audio_tags = [markups[i].find_all('div', {'class': 'audio-list-entry'})[0]
                  for i in range(len(markups))]

    links = [audio_tags[i].find('div', {'class': 'download-container'}).find('a')['href']
             for i in range(len(audio_tags))]

    short_links = [vk.utils.getShortLink(url=links[i], private=0)['short_url']
                   for i in range(len(links))]

    messages = ['''Вот твоя ссылка на скачивание "{} - {}": {}.
                Если название песни при загрузке отличается, то,
                поверь, содержимое - нет.'''.format(artists[i], titles[i], short_links[i])
                for i in range(len(titles))]

    return '\n\n'.join(messages)
