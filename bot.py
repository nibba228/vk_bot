import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from news import get_news
from keyboard import enable_keyboard
from memes import get_meme
from weather import get_weather
from exchange_rates import get_exchange_rate, get_char_codes
from downloading import download_audio
from films import get_genre_names, get_film


# TODO: попробовать узнать погоду с помощью кнопки геолокации
# TODO: попробовать сделать голосовуху робота с указанным сообщением с помощью gtts
# TODO: добавить возможность пересылать сообщения


def main():
    token = 'token'
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    summary = '''
Вот что я умею:
    /help - сводка по командам

    /n - новости

    /m - мем

    /w - получить сведения о погоде в Москве
    (Команды с /w пока могут не работать)
    /w <город> - погода на сегодня. Это может занять некоторое время.

    /exr - получить курсы основных валют

    /exr <XXX> - получить информацию по 1 валюте при помощи её чаркода, чем XXX и является.
    Например, получить информацию о Евро: /exr EUR
                            ↓↓↓
    /c - получить чаркоды валют

    /a - скачать прикреленные к команде аудиозаписи, это может занять некоторое время.
    
    /f <жанр> - случайный фильм с таким жанром
    /f жанры - показывает все доступные жанры
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

            elif msg == '/n':
                vk.messages.send(message=get_news(), **kwargs)

            elif msg == '/m':
                vk.messages.send(attachment=get_meme('-157645793'),
                                 **kwargs)

            elif '/w' in msg:
                vk.messages.send(message=get_weather(msg[8:].strip()), **kwargs)

            elif '/exr' in msg:
                vk.messages.send(message=get_exchange_rate(msg[9:].strip().upper()),
                                 **kwargs)

            elif msg == '/c':
                vk.messages.send(message=get_char_codes(), **kwargs)

            elif msg == '/a':
                vk.messages.send(message=download_audio(vk, user_id),
                                 **kwargs)
            elif msg == '/f жанры':
                vk.messages.send(message=get_genre_names(), **kwargs)
            elif '/f' in msg:
                vk.messages.send(message=get_film(msg[2:].strip()), **kwargs)
            else:
                vk.messages.send(message='''Я не понимаю то, что вы написали.
                                 Отправьте /help, чтобы увидеть сводку по командам''',
                                 **kwargs)


main()
