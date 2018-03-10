import json
import io
import bjcp_xml
import math


def read_json(filename='dump.json'):
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj


def groups_xml_io(styleguide):
    strings = io.StringIO()
    strings.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')
    groups_str = '<string-array name="group_ids">\n'
    for cat, cat_styles in styleguide['beer'].items():
        cat_str = '<string name = "type_{id}">{id}. {name}</string>\n'.format(id=cat[0], name=cat[1])
        # print(cat[1])
        strings.write(cat_str)
        group_str = '<string-array name="type_{}_group">\n'.format(cat[0])
        for style in cat_styles:
            style_str = '<string name = "type_{id}">{id}. {name}</string>\n'.format(id=style['id'], name=style['name'])
            strings.write(style_str)
            group_str += '\t<item>type_{}</item>\n'.format(style['id'])
        group_str += '</string-array>'
        strings.write(group_str)
        groups_str += '\t<item>type_{}</item>\n'.format(cat[0])
    groups_str += '</string-array>\n'
    strings.write(groups_str)
    strings.write('</resources>')
    strings.seek(0)
    return strings


def bjcp_xml_io(styleguide):
    strings = io.StringIO()
    strings.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n')
    for cat_styles in styleguide['beer'].values():
        for style in cat_styles:
            strings.write('<string name="type_{id}_detail" formatted="false"><![CDATA[\n'.format(id=style['id']))
            if 'name_org' in style:
                strings.write('<h1>{id}. {name} - {name_org}</h1>\n'.format(id=style['id'], name=style['name'],
                                                                            name_org=style['name_org']))
            else:
                strings.write('<h1>{id}. {name}</h1>\n'.format(id=style['id'], name=style['name']))
            if 'aroma' in style:
                strings.write('<b>Аромат:</b> {}<br><br>\n'.format(style['aroma']))
            if 'appearance' in style:
                strings.write('<b>Внешнее описание:</b> {}<br><br>\n'.format(style['appearance']))
            if 'flavor' in style:
                strings.write('<b>Вкус:</b> {}<br><br>\n'.format(style['flavor']))
            if 'mouthfeel' in style:
                strings.write('<b>Ощущения во рту:</b> {}<br><br>\n'.format(style['mouthfeel']))
            if 'impression' in style:
                strings.write('<b>Описание:</b> {}<br><br>\n'.format(style['impression']))
            if 'comments' in style:
                strings.write('<b>Комментарии:</b> {}<br><br>\n'.format(style['comments']))
            if 'history' in style:
                strings.write('<b>История:</b> {}<br><br>\n'.format(style['history']))
            if 'ingredients' in style:
                strings.write('<b>Состав:</b> {}<br><br>\n'.format(style['ingredients']))
            if 'comparison' in style:
                strings.write('<b>Сравнение стилей:</b> {}<br><br>\n'.format(style['comparison']))
            if 'stats' in style:
                strings.write('<b>Параметры:</b><br>\n')
                stats = style['stats']
                if 'og' in stats:
                    strings.write('<b>OG:</b> {}<br>\n'.format(print_low_high(stats['og'])))
                if 'fg' in stats:
                    strings.write('<b>FG:</b> {}<br>\n'.format(print_low_high(stats['fg'])))
                if 'ibu' in stats:
                    strings.write('<b>IBUs:</b> {}<br>\n'.format(print_low_high(stats['ibu'])))
                if 'srm' in stats:
                    strings.write('<b>SRM:</b> {}<br>\n'.format(print_low_high(stats['srm'])))
                if 'abv' in stats:
                    strings.write('<b>ABV:</b> {}<br>\n'.format(print_low_high(stats['abv'])))
                if 'co2' in stats:
                    strings.write('<b>CO2:</b> {}<br>\n'.format(stats['co2']))
                strings.write('<br>\n')
            if 'examples' in style:
                strings.write('<b>Коммерческие примеры:</b> {}<br><br>\n'.format(style['examples']))
            if 'tags' in style:
                strings.write('<b>Теги:</b> {}<br>\n'.format(style['tags']))
            strings.write(']]></string>\n')
            if 'stats' in style and 'srm' in style['stats'] and 'low' in style['stats']['srm']\
                and 'high' in style['stats']['srm']:
                strings.write('''<integer-array name="type_{id}_detail_srm">
        <item>{low}</item>
        <item>{high}</item>
    </integer-array>'''.format(id=style['id'], low=int(math.ceil(float(style['stats']['srm']['low']))),
                               high=int(math.ceil(float(style['stats']['srm']['high'])))))
    strings.write('</resources>')
    strings.seek(0)
    return strings


def print_low_high(d):
    if 'low' in d and 'high' in d:
        return '{low} - {high}'.format(**d)
    else:
        return 'варьируется'


"""
<string name="type_1A_detail" formatted="false"><![CDATA[
<h1>1A. Легкий американский лагер - Lite (лайт) American Lager</h1>
<b>Аромат:</b>Запах солода слабый или отсутствует, хотя если он есть, то может быть зерновым, сладким или кукурузоподобным. Аромат хмеля либо отсутствует, либо ощущается его легкое, пряное или цветочное присутствие. Низкие уровни дрожжевого характера (зеленые яблоки, диметилсульфид или фруктовость) необязательны, но приемлемы. Диацетила нет.<br><br>
<b>Внешнее описание:</b> Цвет от очень светлого соломенного до светло-желтого. Белая, пенистая шапка («голова») редко отличается длительной пеностойкостью. Очень прозрачное.<br><br>
<b>Вкус:</b> Искристый и сухой вкус с незначительным уровнем зерновой или кукурузоподобной сладости. Вкус хмеля отсутствует или слабый. Уровень хмелевой горечи низкий. Баланс может варьироваться от слегка солодового до слегка горького, но довольно близок к уравновешенному. Высокий уровень карбонизации может вызвать незначительную кислотность или ощущение сухого «пощипывания». Вкус диацетила отсутствует. Фруктовый привкус отсутствует.<br><br>
<b>Ощущения во рту:</b> (полнота вкуса и уровень карбонизации*): Очень легкое «тело» из-за применения высокого процентного содержания добавок, таких как рис или кукуруза. Очень высокая карбонизация с ощущением незначительного углекислого покалывания на языке. Может казаться водянистым.<br><br>
<b>Общее впечатление:</b> Хорошо освежающее и жаждоутоляющее.<br><br>
<b>Комментарии:</b> Пиво с пониженной плотностью и пониженным содержанием калорий по сравнению со стандартными международными лагерами. Наличие сильного вкуса является недостатком. Рассчитано на привлечение самых широких слоев разнообразной публики.<br><br>
<b>Состав: </b>Двух- или шестирядный ячмень с высоким процентом (до 40%) добавок в виде риса или кукурузы.<br><br>
<b>Параметры:</b><br>
<b>OG:</b> 1.028 - 1.040<br>
<b>FG:</b> 0.998 - 1.008 <br>
<b>IBUs:</b> 8 - 12<br>
<b>SRM:</b> 2 - 3<br>
<b>ABV:</b> 2.8 - 4.2%<br>
<b>CO2:</b> 2.50 - 2.80<br><br>
<b>Коммерческие примеры:</b> Bitburger Light, Sam Adams Light, Heineken Premium Light, Miller Lite, Bud Light, Coors Light, Baltika #1 Light, Old Milwaukee Light, Amstel Light]]></string>
    <integer-array name="type_1A_detail_srm">
        <item>2</item>
        <item>3</item>
    </integer-array>"""

if __name__ == "__main__":
    import mapping
    import profibeer
    import notabenoid
    # style = read_json('data/profibeer/IPA_Американский IPA.json')
    # l = layout_app(style)
    # print(l)

    styleguide = bjcp_xml.parse_xml()
    pb = dict(profibeer.get_all())
    nb = {style['name']: style for style in notabenoid.get_styles_gen()}
    mapping.co2_mapping(styleguide)
    mapping.source_mapping_pb(styleguide, pb)
    mapping.source_mapping_pb(styleguide, nb)
    # strs = groups_xml_io(styleguide)
    strs = bjcp_xml_io(styleguide)
    # with open('groups.xml', 'w+') as fh:
    with open('bjcp.xml', 'w+') as fh:
        fh.write(strs.read())
    # print(strs.read())

    mapping.group_mapping(styleguide)
    strs = groups_xml_io(styleguide)
    with open('groups.xml', 'w+') as fh:
        fh.write(strs.read())
    # print(strs.read())
