import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from news import get_news
from keyboard import enable_keyboard
from memes import get_meme
from weather import get_weather
from exchange_rates import get_exchange_rate, get_char_codes
from downloading import download_audio

# TODO: попробовать узнать погоду с помощью кнопки геолокации
# TODO: попробовать сделать голосовуху робота с указанным сообщением с помощью gtts
# TODO: загружать видео, фильмы или что-то вроде того
# TODO: реализовать множественное скачивание музыки,
#  если одновременно с командой скинуто более 1 аудиозаписи


if __name__ == '__main__':
    TOKEN = '<Token>'
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    summary = '''
Вот что я умею:
    /help - сводка по командам
    
    /news - новости
    
    /meme - мем
    
    /weather <город> - погода на сегодня.
     Название города пишется по-английски, с дефисами вместо пробелов, без учета регистра. 
     По умолчанию Москва.
     Например, получить информацию о погоде в Лос Анджелесе: /weather los-angeles
     
     /ex-rate - получить курсы основных валют
     /ex-rate <XXX> - получить информацию по 1 валюте при помощи её чаркода, чем XXX и является.
     Например, получить информацию о Евро: /ex-rate EUR
                            ↓↓↓
     /chars - получить чаркоды валют
     
     /aud - скачать прикреленные к команде аудиозаписи, это может занять некоторое время.
    '''

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            random_id = get_random_id()
            user_id = event.user_id
            msg = event.text.lower()

            kwargs = {'user_id': user_id,
                      'random_id': random_id}

            if msg in ('/help', 'начать'):
                vk.messages.send(message=summary, keyboard=enable_keyboard(),
                                 **kwargs)
            if msg == '/news':
                vk.messages.send(message=get_news(), **kwargs)
            if msg == '/meme':
                vk.messages.send(attachment=get_meme('-165800926'),
                                 **kwargs)
            if '/weather' in msg:
                vk.messages.send(message=get_weather(msg[8:].strip()), **kwargs)
            if '/ex-rate' in msg:
                vk.messages.send(message=get_exchange_rate(msg[9:].strip().upper()),
                                 **kwargs)
            if msg == '/chars':
                vk.messages.send(message=get_char_codes(), **kwargs)
            if msg == '/aud':
                vk.messages.send(message=download_audio(vk, user_id),
                                 **kwargs)
            else:
                vk.messages.send(message='''Я не понимаю то, что вы написали.
                                 Отправьте /help, чтобы увидеть сводку по командам''',
                                 **kwargs)
