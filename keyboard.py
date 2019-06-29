from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def enable_keyboard(geo_button=False):
    # для погоды
    # param geo_button=False

    keyboard = VkKeyboard(False)

    keyboard.add_button('/help', VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    keyboard.add_button('/m', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/n', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/f жанры', VkKeyboardColor.PRIMARY)
    keyboard.add_line()

    keyboard.add_button('/w', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/exr', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/c', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/a', VkKeyboardColor.PRIMARY)

    # if geo_button:
    #     keyboard.keyboard['buttons'].append([{
    #         'action': {
    #             'type': 'location',
    #             'payload': '{"buttons": "1"}'
    #         }
    #     }])

    return keyboard.get_keyboard()
