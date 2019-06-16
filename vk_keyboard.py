from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def enable_keyboard():
    keyboard = VkKeyboard(True)
    keyboard.add_button('/help', VkKeyboardColor.POSITIVE)
    keyboard.add_button('/news', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/meme', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('/weather', VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()
