import vk_api
import random


def get_meme(group_id):
    token = '2a94d2a62a94d2a62a94d2a6022afffb4822a942a94d2a67792bba51eb064fbd042261e'
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    notes_count = int(vk.wall.get(owner_id=group_id)['count'])
    offset = random.randint(1, notes_count + 1)
    posts = vk.wall.get(owner_id=group_id,
                        offset=offset,
                        count=5)

    for post in posts['items']:
        if post.get('attachments') and post['attachments'][0]['type'] == 'photo':
            return 'photo{}_{}'.format(group_id, post.get('attachments')[0]['photo']['id'])
        else:
            return 'photo-183016592_456239064'
