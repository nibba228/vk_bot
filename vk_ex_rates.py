import requests
from bs4 import BeautifulSoup


def get_exchange_rate():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    markup = BeautifulSoup(response.content, 'html.parser')

    volute_ids = ['R01235', 'R01239', 'R01035', 'R01820', 'R01775', 'R01010', 'R01350']
    volutes = [markup.find('valute', {'id': volute_id}) for volute_id in volute_ids]
    summary = ['{} ({}) стоит {} ₽'.format(volute.nominal.next_sibling.text,
                                           volute.charcode.text,
                                           volute.value.text)
               for volute in volutes]
    return '\n'.join(summary)


# for volute in markup.find_all('volute'):
#     if volute.name.text == volute_name:
#         id = volute['id']
