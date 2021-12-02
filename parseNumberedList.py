import json


def dnd_prof():
    with open("dndProffessions.json") as f:
        content = [
            line[line.find('.') + 2:].replace("\n", '')
            for line in f.readlines()
            if line[0] in "0123456789"
        ]

    content = {
        "description": "A list of occupations (jobs that people might have).",
        "professions": content
    }

    writing_file = open("dndProffessions2.json", "+w")
    json.dump(content, fp=writing_file)


def royalties():
    content = """Emperor/Empress
        King/Queen
        Duke/Duchess
        Prince/Princess
        Marquess/Marquise
        Earl or Count/Countess
        Viscount/Viscountess
        Baron/Baroness
        Baronet
        Knight""".splitlines()

    content = {
        "description": "A list of noble possisions in dnd",
        "positions": content
    }

    writing_file = open("nobles.json", "+w")
    json.dump(content, fp=writing_file)


royalties()
