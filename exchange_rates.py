import requests
from bs4 import BeautifulSoup


def get_exchange_rate(volute_char_code):
    """
    :param volute_char_code: чаркод требуемой валюты, может быть пустой строкой,
     при этом выведется информация о некоторых важных валютах
    :return: str
    """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    if len(volute_char_code) != 3:
        # востребованные валюты
        volute_ids = ['R01235', 'R01239', 'R01035', 'R01820', 'R01775', 'R01010', 'R01350']
        volutes = [markup.find('valute', {'id': volute_id}) for volute_id in volute_ids]
        result = ['{} ({}) стоит {} ₽'.format(volute.nominal.next_sibling.text,
                                              volute.charcode.text,
                                              volute.value.text) for volute in volutes]
        return '\n'.join(result)
    else:
        for volute in markup.find_all('valute'):
            if volute.charcode.text == volute_char_code:
                return '{} ({}) стоит {} ₽'.format(volute.nominal.next_sibling.text,
                                                   volute.charcode.text,
                                                   volute.value.text)
        else:
            return 'Неправильный чаркод'


def get_char_codes():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    volutes = markup.find_all('valute')

    char_codes = [volute.charcode.text for volute in volutes]
    names = [volute.nominal.next_sibling.text for volute in volutes]

    result = ['{} - {}'.format(name, char_code) for char_code, name in zip(char_codes, names)]
    result.sort()

    return '\n'.join(result)
