from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def enable_keyboard():
    # для погоды
    # param geo_button=False

    keyboard = VkKeyboard(False)

    keyboard.add_button('/help', VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    # if geo_button:
    #     keyboard...

    keyboard.add_button('/m', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/n', VkKeyboardColor.PRIMARY)
    keyboard.add_line()

    keyboard.add_button('/w', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/exr', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/c', VkKeyboardColor.PRIMARY)
    keyboard.add_button('/a', VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
