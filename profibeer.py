"""Достаем перевод bjcp с источника profibeer.ru"""

import requests
from bs4 import BeautifulSoup as bs
from utils import read_json, dump_json
import os


URL = 'https://profibeer.ru'
URL_BJCP = '/styles/bjcp/'
PARSER = 'lxml'
data_dir = 'data/profibeer/'


def parse_desc(url):
    r = requests.get(url)
    soup = bs(r.text, PARSER)
    div = soup.find(class_='b-style-el__desc')
    title = div.find(class_='b-style-el__desc-title').text
    # print(title)
    div_text = div.find(class_='editor editor_small')
    l = ['Описание:']
    for p in div_text.find_all('p'):
        l.append(p.text)
    i = iter(l)
    d = dict(zip(i, i))

    tbl = {}
    for row in div_text.findAll('tr'):
        tds = row.find_all('td')
        if tds:
            tbl[tds[0].text] = tds[1].text
    d['Характеристики:'] = tbl

    return title, d


def parse_cat_1(url):
    r = requests.get(url)
    soup = bs(r.text, PARSER)
    div_list = soup.find(class_='b-style-el__list')
    d = {}
    for href in div_list.find_all('a'):
        d[href.text.strip()] = href.attrs['href']
    return d


def parse_cat_2(url):
    r = requests.get(url)
    soup = bs(r.text, PARSER)
    div_list = soup.find_all(class_='b-style-el__list')
    d = {}
    for href in div_list[1].find_all('a'):
        d[href.text.strip()] = href.attrs['href']
    return d


def get_cat2():
    # d = parse_cat_1(URL + BJCP_URL)
    # dump_json(d, 'cat.json')
    cats = read_json(data_dir + 'cat.json')
    for title, url in cats.items():
        d = parse_cat_2(URL + url)
        dump_json(d, data_dir + title + '.json')


def get_styles_desc():
    style = read_json(data_dir + 'IPA.json')
    for title, url in style.items():
        s, d = parse_desc(URL + url)
        dump_json(d, data_dir + 'IPA/' + s + '.json')


def parse_all():
    cats = read_json(data_dir + 'cat.json')
    for cat_title, cat_url in cats.items():
        styles = read_json(data_dir + cat_title + '.json')
        for title, url in styles.items():
            filepath = data_dir + cat_title + '_' + title + '.json'
            if not os.path.exists(filepath):
                style_title, desc = parse_desc(URL + url)
                dump_json(desc, filepath)


def get_all():
    cats = read_json(data_dir + 'cat.json')
    for cat_title, cat_url in cats.items():
        styles = read_json(data_dir + cat_title + '.json')
        for title, url in styles.items():
            style = read_json(data_dir + cat_title + '_' + title + '.json')
            yield title, style


if __name__ == "__main__":
    # parse_all()
    import mapping
    d = dict(get_all())
    for k, v in d.items():
        # if mapping.profibeer_mapping.get(k) == None:
        #     print(k, mapping.profibeer_mapping.get(k))
        print(v)
    pass