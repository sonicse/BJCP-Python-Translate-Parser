import requests
from bs4 import BeautifulSoup as bs
import utils
import re


PARSER = 'lxml'
URL = 'http://notabenoid.org'
data_dir = 'data/notabenoid/'
title_pattern = re.compile(r'(?P<id>\S+)\.\s(?P<name>[\w|\s]+)\s\((?P<name_org>[\w|\s]+)\)')


class Client:
    _instance = None

    @staticmethod
    def get_instance():
        if Client._instance is None:
            Client._instance = requests.Session()
            form = {'login[login]': 'login(change to yuors)', 'login[pass]': 'password (change to yours)'}
            Client._instance.post(URL, data=form)
        return Client._instance


def chapter_gen():
    r = Client.get_instance().get(URL + '/book/60552')
    soup = bs(r.text, PARSER)
    table = soup.find(id='Chapters')
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        title = row.find('td', class_='t').text
        perc = row.find('td', class_='r')
        if perc:
            perc = perc.text
        link = row.find('a', class_='act')
        if link:
            link = link.attrs['href']
        yield title, perc, link


def get_style(title, perc, link):
    r = Client.get_instance().get(URL + link)
    soup = bs(r.text, PARSER)
    rows = soup.find('div', class_='span8').find_all('p')
    data = {}
    for row in rows:
        txt = row.text
        index = txt.find(':')
        title = txt[0: index + 1]
        content = txt[index + 1:]
        data[title] = content
    return data


def validate_style(style_data):
    checks = ['Общее впечатление:', 'Аромат:', 'Внешний вид:', 'Вкус:', 'Ощущение во рту:', 'Комментарии:',
              'История:', 'Характерные ингредиенты:', 'Сравнение стилей:', 'Коммерческие примеры:', 'Теги:']
    for check in checks:
        if check not in style_data:
            # print(check)
            return False
    return True


def dump_chapters():
    """Сохраняем оглавление руководства"""
    data = {}
    for title, perc, link in chapter_gen():
        data[title] = (perc, link)
        utils.dump_json(data, data_dir + 'items.json')


def dump_styles_raw():
    """Сохраняем данные стилей (не обработанные)"""
    data = utils.read_json(data_dir + 'items.json')
    for title, (perc, link) in data.items():
        perc = float(perc[0:perc.find('%')])
        if perc == 100.0:
            print(title, perc, link)
            data = get_style(title, perc, link)
            validate_style(data)
            utils.dump_json(data, data_dir + title + '_raw.json')


def validate_styles():
    data = utils.read_json(data_dir + 'items.json')
    for title, (perc, link) in data.items():
        perc = float(perc[0:perc.find('%')])
        if perc == 100.0:
            print(title, perc, link)
            data = utils.read_json(data_dir + title + '_raw.json')
            validate_style(data)


def get_styles_gen():
    data = utils.read_json(data_dir + 'items.json')
    for title, (perc, link) in data.items():
        perc = float(perc[0:perc.find('%')])
        if perc == 100.0:
            # print(title, perc, link)
            data = utils.read_json(data_dir + title + '_raw.json')
            if validate_style(data):
                g = re.search(title_pattern, data[''])
                if g:
                    if g.group('id'):
                        data['id'] = g.group('id')
                    if g.group('name'):
                        data['name'] = g.group('name')
                    if g.group('name_org'):
                        data['name_org'] = g.group('name_org')
                else:
                    pass
                yield data


if __name__ == "__main__":
    # dump_styles_raw()
    # title = '5B. Kölsch'
    # perc = '100% (15 / 15)'
    # link = '/book/60552/285753/ready'
    # data = get_style(title, perc, link)
    for style in get_styles_gen():
        print(style)