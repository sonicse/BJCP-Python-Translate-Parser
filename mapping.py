from data import co2

groups_mapping = {
    'Standard American Beer': 'Стандартный американский лагер',
    'International Lager': 'Международный лагер',
    'Czech Lager': 'Чешский лагер',
    'Pale Malty European Lager': 'Светлый солодовый европейский лагер',
    'Pale Bitter European Beer': 'Светлый горький европейский лагер',
    'Amber Malty European Lager': 'Янтарный солодовый европейский лагер',
    'Amber Bitter European Beer': 'Янтарный горький европейский лагер',
    'Dark European Lager': 'Темный европейский лагер',
    'Strong European Beer': 'Крепкий европейский лагер',
    'German Wheat Beer': 'Немецкое пшеничное пиво',
    'British Bitter': 'Британский биттер',
    'Pale Commonwealth Beer': 'Светлое пиво содружества',
    'Brown British Beer': 'Коричневое британское пиво',
    'Scottish Ale': 'Шотландское пиво',
    'Irish Beer': 'Ирландское пиво',
    'Dark British Beer': 'Темное британское пиво',
    'Strong British Ale': 'Крепкое британское пиво',
    'Pale American Ale': 'Светлый американский эль',
    'Amber And Brown American Beer': 'Светлое и коричневое американское пиво',
    'American Porter And Stout': 'Американский портер и стаут',
    'IPA': 'ИПА',
    'Strong American Ale': 'Крепкий американский эль',
    'European Sour Ale': 'Европейский кислый эль',
    'Belgian Ale': 'Бельгийский эль',
    'Strong Belgian Ale': 'Крепкий бельгийский эль',
    'Trappist Ale': 'Траппистский эль',
    'Historical Beer': 'Историческое пиво',
    'American Wild Ale': 'Американский дикий эль',
    'Fruit Beer': 'Фруктовое пиво',
    'Spiced Beer': 'Пиво со специями',
    'Alternative Fermentables Beer': 'Пиво альтернативного брожения',
    'Smoked Beer': 'Копченое пиво',
    'Wood Beer': 'Выдержанное пиво',
    'Specialty Beer': 'Специальное пиво',
}

pb_attr_mapping = {'id': 'id',
                   'name': 'name',
                   'Аромат:': 'aroma',
                   'Внешний вид:': 'appearance',
                   'Вкус:': 'flavor',
                   'Ощущение во рту:': 'mouthfeel',
                   'Описание:': 'impression',
                   'Комментарии:': 'comments',
                   'История:': 'history',
                   'Характерные ингредиенты:': 'ingredients',
                   'Сравнение стилей:': 'comparison',
                   'Характеристики:': 'stats',
                   'OG:': 'og',
                   'FG:': 'fg',
                   'IBUs:': 'ibu',
                   'SRM:': 'srm',
                   'ABV:': 'abv',
                   'CO2:': 'CO2',
                   'Коммерческие примеры:': 'examples',
                   'Теги': 'tags',
                   'Алкоголь по объему': 'abv',
                   'Горечь': 'ibu',
                   'Конечная плотность': 'fg',
                   'Начальная плотность': 'og',
                   'Цвет': 'srm',
                   }

pb_attr_mapping_reversed = {v: k for k, v in pb_attr_mapping.items()}

pb_style_mapping = {
    'Калифорнийское обычное': 'California Common',
    'Гозе': 'Gueuze',

    'Английский портер': 'English Porter',
    'Бельгийский темный крепкий эль': 'Belgian Dark Strong Ale',
    'Британский браун-эль': 'British Brown Ale',
    'Кентуккское обычное': 'Kentucky Common',
    'Гродзисское пиво': 'Piwo Grodziskie',
    'Международный темный лагер': 'International Dark Lager',
    'Ви-хэви': 'Wee Heavy',
    'Двойной IPA': 'Double IPA',
    'Фламандский коричневый эль': 'Oud Bruin',
    'Бельгийский золотой крепкий эль': 'Belgian Golden Strong Ale',
    'Лучший биттер': 'Best Bitter',
    'Аргентинский IPA': 'Argentine Styles X2. IPA Argenta',
    'Особый IPA: красный': 'Red IPA',
    'Венский лагер': 'Vienna Lager',
    'Фруктовое пиво': 'Fruit Beer',
    'Британский золотой эль': 'British Golden Ale',
    'Американский стаут': 'American Stout',
    'Берлинер-вайссе': 'Berliner Weisse',
    'Американский амбер-эль': 'American Amber Ale',
    'Бреттовое пиво': 'Brett Beer',
    'Чешский темный лагер': 'Czech Dark Lager',
    'Ординарный биттер': 'Ordinary Bitter',
    'Пиво с альтернативными сахарами': 'Alternative Sugar Beer',
    'Особое дикое пиво': 'Wild Specialty Beer',
    'Американское пшеничное пиво': 'American Wheat Beer',
    'Светлый бок (Майбок)': 'Light side (Maibok)',
    'Американский пейл-эль': 'American Pale Ale',
    'Осеннее сезонное пиво': 'Autumn Seasonal Beer',
    'Британский крепкий эль': 'British Strong Ale',
    'Чешский янтарный лагер': 'Czech Amber Lager',
    'Пиво с альтернативным зерном': 'Alternative Grain Beer',
    'Особый IPA': 'Special IPA',
    'Немецкий экспортный хеллес': 'German Helles Exportbier',
    'Пиво с пряностями, травами, овощами': 'Spice, Herb, or Vegetable Beer',
    'Бельгийский трипель': 'Belgian Tripel',
    'Роггенбир': 'Roggenbier',
    'Фламандский красный эль': 'Flanders Red Ale',
    'Лондонский браун-эль': 'London Brown Ale',
    'Витбир (Бланш)': 'Witbier',
    'Пиво с фруктами и пряностями': 'Fruit and Spice Beer',
    'Международный светлый лагер': 'International Pale Lager',
    'Старый эль': 'Old Ale',
    'Лихтенхайнер': 'Lichtenhainer',
    'Немецкий ляйхтбир': 'German Leichtbier',
    'Тропический стаут': 'Tropical Stout',
    'Немецкий пилз': 'German Pils',
    'Ирландский красный эль': 'Irish Red Ale',
    'Имперский стаут': 'Imperial Stout',
    'Бьер-де-гард': 'Bière de Garde',
    'Траппистский обычный эль': 'Trappist Single',
    'Американский лагер': 'American Lager',
    'Овсяный стаут': 'Oatmeal Stout',
    'Фруктовый ламбик': 'Fruit Lambic',
    'Блонд-эль': 'Blonde Ale',
    'Особый IPA: коричневый': 'Special IPA: brown',
    'Бельгийский блонд-эль': 'Belgian Blond Ale',
    'Вайсбир': 'Weissbier',
    'Американский легкий лагер': 'American Light Lager',
    'Итальянский виноградный эль': 'Italian Grape Ale',
    'Айсбок': 'Eisbock',
    'Особое копченое пиво': 'Specialty Smoked Beer',
    'Мюнхенский хеллес': 'Munich Helles',
    'Гёз': 'Göz',
    'Сэзон': 'Saison',
    'Крепкий биттер': 'Strong Bitter',
    'Сладкий стаут': 'Sweet Stout',
    '«Досухозаконный» лагер': 'Pre-Prohibition Lager',
    'Крим-эль': 'Cream Ale',
    'Американский IPA': 'American IPA',
    'Ирландский стаут': 'Irish Stout',
    'Доппельбок': 'Doppelbock',
    'Раухбир': 'Rauchbier',
    'Международный янтарный лагер': 'International Amber Lager',
    'Зимнее сезонное пиво': 'Winter Seasonal Beer',
    'Шварцбир': 'Schwarzbier',
    'Мюнхенский дункель': 'Munich Dunkel',
    'Выдержанное в дереве пиво': 'Wood-Aged Beer',
    'Кислое пиво смешанного брожения': 'Mixed-Fermentation Sour Beer',
    '«Досухозаконный» портер': 'Pre-Prohibition Porter',
    'Особое фруктовое пиво': 'Specialty Fruit Beer',
    'Сахти': 'Sahti',
    'Бельгийский дуббель': 'Belgian Dubbel',
    'Чешский светлый лагер': 'Czech Pale Lager',
    'Шотландский крепкий эль': 'Scottish Heavy',
    'Английский барливайн': 'English Barleywine',
    'Фестбир': 'Festbier',
    'Кёльш': 'Kölsch',
    'Английский IPA': 'English IPA',
    'Темный майлд': 'Dark Mild',
    'Вайценбок': 'Weizenbock',
    'Светлый келлербир': 'Pale Kellerbier',
    'Темный бок': 'Dunkles Bock',
    'Особый IPA: ржаной': 'Special IPA: Rye IPA',
    'Пшеничное вино (витвайн)': 'Wheatwine',
    'Американский браун-эль': 'American Brown Ale',
    'Особое выдержанное в дереве пиво': 'Specialty Wood-Aged Beer',
    'Альтбир': 'Altbier',
    'Ирландский экстра-стаут': 'Irish Extra Stout',
    'Янтарный келлербир': 'Amber Kellerbier',
    'Классическое копченое пиво': 'Classic Style Smoked Beer',
    'Австралийский игристый эль': 'Australian Sparkling Ale',
    'Особый IPA: черный': 'Special IPA: black',
    'Американский барливайн': 'American Barleywine',
    'Шотландский экспортный эль': 'Scottish Export',
    'Мэрцен': 'Märzen',
    'Американский портер': 'American Porter',
    'Бельгийский пейл-эль': 'Belgian Pale Ale',
    'Ламбик': 'Lambic',
    'Зарубежный экстра-стаут': 'Foreign Extra Stout',
    'Чешский светлый премиум-лагер': 'Czech Premium Pale Lager',
    'Американский крепкий эль': 'American Strong Ale',
    'Шотландский легкий эль': 'Scottish Light',
    'Особый IPA: бельгийский': 'Specialty IPA: Belgian IPA',
    'Пампасный золотой эль': 'Pampas Golden Ale',
    'Балтийский портер': 'Baltic Porter',
    'Темный вайсбир (Дункельвайцен)': 'Dunkles Weissbier',
    'Особый IPA: белый': 'Specialty IPA: White IPA',
}

profibeer_mapping_reversed = {v: k for k, v in pb_style_mapping.items()}


def test_mapping(styleguide):
    styles = []
    for cat in styleguide['beer'].values():
        for style in cat:
            styles.append(style['name'])
    print(styles)

    # d = dict(profibeer.get_all())
    # for k, v in d.items():
    #     if mapping.profibeer_mapping.get(k) == None:
    #         print(k, mapping.profibeer_mapping.get(k))
    not_finded = []
    for title in pb_style_mapping.values():
        if title not in styles:
            print(title)
            not_finded.append(title)
    print(len(not_finded))


def source_mapping_pb(styleguide, pb):
    for cat in styleguide['beer'].values():
        for style in cat:
            style_name = style['name']
            style_key = profibeer_mapping_reversed.get(style_name)
            if not style_key:
                continue
            pb_style = pb.get(style_key)
            if not pb_style:
                continue
            pb_style['name'] = style_key
            merge_style(style, pb_style)
            style['name_org'] = style_name


def merge_style(style, new):
    for attr in style.keys():
        new_attr = pb_attr_mapping_reversed[attr]
        if attr == 'stats':
            # merge_style(style[attr], new[new_attr])
            continue
        try:
            style[attr] = new[new_attr]
        except Exception as e:
            # print(style['name'], e)
            pass


def co2_mapping(styleguide):
    for cat in styleguide['beer'].values():
        for style in cat:
            if style['name'] in co2.co2 and 'stats' in style:
                style['stats']['co2'] = co2.co2[style['name']]


def group_mapping(styleguide):
    beer = styleguide['beer']
    keys = list(beer.keys())
    for cat in keys:
        if cat[1] in groups_mapping:
            cat_new = (cat[0], groups_mapping[cat[1]])
            beer[cat_new] = beer[cat]
            del beer[cat]


if __name__ == "__main__":
    import bjcp_xml
    import profibeer

    styleguide = bjcp_xml.parse_xml()
    profibeer_data = dict(profibeer.get_all())
    notabenoid_data = None

    # parse_all()
    # d = dict(get_all())
    # for k, v in d.items():
    #     if mapping.profibeer_mapping.get(k) == None:
    #         print(k, mapping.profibeer_mapping.get(k))
    # source_mapping_pb(styleguide, profibeer_data)
    group_mapping(styleguide)
    pass
