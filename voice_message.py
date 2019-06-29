import os
import gtts


def voice(text):
    vocalised = gtts.gTTS(text, 'ru')
    file = '/home/krieper2004/audio.ogg'
    try:
        vocalised.save(file)
    except IOError:
        os.system('touch {}'.format(file))
        vocalised.save(file)


# def _upload(vk, peer_id, audio):
#     upload_url = vk.docs.getMessagesUploadServer(type='audio_message', peer_id=peer_id)
#     requests.post(url=upload_url['upload_url'], data=audio)
