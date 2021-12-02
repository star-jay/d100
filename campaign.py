import d100

races = [
    ''
]


def gen_player_character():
    character = dict(
        gender=d100.pick('mf'),
        race=d100.pick(races),
        cclass=d100.pick(classes),

    )
    return character
