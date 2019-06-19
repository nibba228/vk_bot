from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def enable_keyboard():
    # для погоды
    # param geo_button=False

    keyboard = VkKeyboard(False)

    keyboard.add_button('/help', VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    # if geo_button:
    #     keyboard...

    keyboard.add_button('/meme', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/news', VkKeyboardColor.PRIMARY)
    keyboard.add_line()

    keyboard.add_button('/weather', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/ex-rate', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/chars', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/aud', VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
