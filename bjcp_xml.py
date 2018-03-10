"""
Парсим xml-файл руководства bjcp с источника:
 https://raw.githubusercontent.com/meanphil/bjcp-guidelines-2015/master/styleguide.xml
"""
from lxml import etree
from collections import OrderedDict


def get_childs(el, childs):
    for child in childs:
        try:
            yield next(el.iterchildren(child))
        except StopIteration:
            pass


def get_childs_text(el, childs):
    res = OrderedDict()
    for child in get_childs(el, childs):
        res[child.tag] = child.text
    return res


def get_attrs(el, attrs):
    res = OrderedDict()
    for attr in attrs:
        res[attr] = el.get(attr)
    return res


def parse_xml(filename='data/styleguide.xml'):
    with open(filename, 'rb') as f:
        data = etree.fromstring(f.read())
        for el in data.iter('styleguide'):
            return parse_styleguide(el)


def parse_styleguide(el):
    # print(el.tag)
    classes = OrderedDict()
    for child in el.iterchildren('class'):
        k, v = parse_class(child)
        classes[k] = v
    return classes


def parse_class(el):
    # print(el.tag, el.get('type'))
    categories = OrderedDict()
    for child in el.iterchildren('category'):
        k, v = parse_category(child)
        categories[k] = v
    return el.get('type'), categories


def parse_category(el):
    childs = get_childs_text(el, ['revision', 'name', 'notes'])
    # print(el.tag, el.get('id'), childs)
    subcategories = []
    for child in el.iterchildren('subcategory'):
        subcategories.append(parse_subcategory(child))
    return (el.get('id'), childs['name']), subcategories


def parse_subcategory(el):
    childs = get_childs_text(el, ['name', 'aroma', 'appearance', 'flavor', 'mouthfeel', 'impression', 'comments', 'history',
                             'ingredients', 'comparison', 'examples', 'tags'])
    # print(el.tag, childs)
    childs['id'] = el.get('id')
    childs['stats'] = parse_stats(next(el.iterchildren('stats')))
    return childs


def parse_stats(el):
    res = {}
    childs = get_childs(el, ['ibu', 'og', 'fg', 'srm', 'abv'])
    for child in childs:
        if child.get('flexible') == 'false':
            res[child.tag] = get_childs_text(child, ['low', 'high'])
        else:
            res[child.tag] = {'flexible': True}
    # print(res)
    return res


if __name__ == "__main__":
    parse_xml()