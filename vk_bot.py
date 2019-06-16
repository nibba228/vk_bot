import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import random

from vk_news import get_news
from vk_keyboard import enable_keyboard
from vk_memes import get_meme
from vk_weather import get_weather


if __name__ == '__main__':
    TOKEN = 'b1d0871366298b0af1290675423f38c05d57c63296eb409ce866b646fbbdda6ce506c14d2ad959baa312c'
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    greeting = '''
Вот что я умею:
    /help - сводка по командам
    
    /news - новости
    
    /meme - мем
    
    /weather <город> - погода на сегодня.
     Название города пишется по-английски, с дефисами вместо пробелов, без учета регистра. 
     По умолчанию Москва
    '''

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            random_id = get_random_id()
            user_id = event.user_id
            msg = event.text.lower()
            if msg == '/help':
                vk.messages.send(user_id=user_id,
                                 random_id=random_id,
                                 message=greeting,
                                 keyboard=enable_keyboard())
            if msg == '/news':
                vk.messages.send(user_id=user_id,
                                 random_id=random_id,
                                 message=get_news(),
                                 keyboard=enable_keyboard())
            if msg == '/meme':
                vk.messages.send(user_id=user_id,
                                 random_id=random_id,
                                 attachment=get_meme(random.choice(['-171240129', '-72495085'])),
                                 keyboard=enable_keyboard())
            if '/weather' in msg:
                vk.messages.send(user_id=user_id,
                                 random_id=random_id,
                                 message=get_weather(msg[8:].strip()),
                                 keyboard=enable_keyboard())
            else:
                vk.messages.send(user_id=user_id,
                                 random_id=random_id,
                                 message='''
                                 Я не понимаю то, что вы написали.
                                 Отправьте /help, чтобы увидеть сводку по командам
                                         ''',
                                 keyboard=enable_keyboard())
