def find_group(data, category, subcategory, group):
    # Проверяем, существует ли категория
    if category in data:
        # Проверяем, существует ли подкатегория в категории
        if subcategory in data[category]:
            # Проверяем, существует ли группа в подкатегории
            if group in data[category][subcategory]:
                return category, subcategory, group
            else:
                return category, subcategory, None
        else:
            return category, None, None
    else:
        return None, None, None

# '','','','','','','','','','','','','','','','','','','','','',
data = {
    'Варгеймы': {
        'Warhammer 40.000': ['Adeptus Astartes: Space Marines', 'Adeptus Astartes: Black Templars', 'Adeptus Astartes: Blood Angels',
                             'Adeptus Astartes: Dark Angels', 'Adeptus Astartes: Deathwatch','Adeptus Astartes: Grey Knights',
                             'Adeptus Astartes: Space Wolves', 'Adepta Sororitas' ,'Adeptus Custodes','Adeptus Mechanicus',
                             'Astra Militarum','Inquisition', 'Imperial Knights','Chaos Daemons','Chaos Space Marines',
                             'Chaos Knights','Thousand Sons', 'Death Guard','World Eaters','Dark Eldar','Eldar','Harlequins',
                             'Tyranids','Genestealer Cults', 'Necrons','Orks','Tau Empire','Leagues of Votann','Horus Heresy',
                             'Necromunda','Kill Team','Adeptus Titanicus', 'Legions Imperialis','Battlefleet Gothic',
                             'Aeronautica Imperialis','Террейн Warhammer 40.000','Литература Warhammer 40.000',
                             'Аксессуары Warhammer 40.000'],
        'Warhammer Age of Sigmar': ['Stormcast Eternals', 'Cities of Sigmar','Fyreslayers','Kharadron Overlords',
                                    'Lumineth Realm-lords','Idoneth Deepkin','Sylvaneth','Seraphon',
                                    'Slaves to Darkness','Blades of Khorne','Disciples of Tzeentch','Hedonites of Slaanesh',
                                    'Maggotkin of Nurgle','Skaven','Flesh-Eater Courts','Soulblight Gravelords','Nighthaunt',
                                    'Ossiarch Bonereapers','Gloomspite Gitz', 'Ogor Mawtribes','Orruk Warclans','Sons of Behemat',
                                    'Warhammer Underworlds','Warcry','Террейн Age of Sigmar','Литература Age of Sigmar','Аксессуары Age of Sigmar','','','','','','','','','','','','','','',],
        'Террейн':['SciFi террейн','Fantasy террейн'],
        'BattleTech':['None'],
        'Аксессуары':['Кубы','Шаблоны','Датакарты','Декали','Базы','Прочие игровые аксессуары','','','',],
        'Sci-Fi миниатюры':['Sci-Fi миниатюры','Фэнтези миниатюры'],
        'Авторские варгеймы':['Гидрофилия','TechDusk','Древняя Механика','Фронтир: Далекие Звезды',''],
        'Прочие игры с миниатюрами':['None'],


    },
    'Стендовые модели': {
        'Военная техника': ['None'],
        'Военная авиация': ['None'],
        'Гражданская техника':['None'],
        'Гражданская авиация':['None'],
        'Флот':['None'],
        'Пехота и кавалерия':['None'],
        'Бюсты':['None'],
        'Диорамы':['None'],
        'Дополнения к моделям':['None'],
        'Прочие стендовые модели':['None']
    },
    'Настольные игры': {
        'Стратегические игры': ['None'],
        'Кооперативные игры': ['None'],
        'Карточные игры':['None'],
        'Детективные игры':['None'],
        'Экономические игры':['None'],
        'Игры для вечеринок':['None'],
        'Настольные игры для детей':['None'],
        'Аксессуары для настольных игр':['None'],
    },
    'Ролевые игры': {
        'Миниатюры для ролевых игр': ['None'],
        'Dungeons & Dragons': ['None'],
        'Pathfinder':['None'],
        'Прочие НРИ':['None'],
        'Аксессуары для ролевых игр':['None'],
    },
    'Экшен-фигурки': {
        'Экшен-фигурки': ['JOYTOY Warhammer','JOY TOY Infinity'],
        'Dungeons & Dragons': ['None'],
        'McFarlane':['None'],
        'Прочие экшен-фигурки':['None'],
    },
    'Печать 3D миниатюр':['None']
}