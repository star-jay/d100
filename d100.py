import tracery
import json
from tracery.modifiers import base_english
import random


def d100():
    return random.randrange(1, 100)


def new_object(name, tags):
    return dict(name=name)


# put your grammar here as the value assigned to "rules"
rules = json.loads(open("grammar.json").read())

# load the JSON data from files downloaded from corpora project
names_data = json.loads(open("firstNames.json").read())
occupation_data = json.loads(open("dndProffessions2.json").read())

# set the values for "name" and "profession" rules with corpora data
rules["name"] = names_data["firstNames"]
rules["profession"] = occupation_data["professions"]

# create a grammar object from the rules
grammar = tracery.Grammar(rules)
# add pre-programmed modifiers
grammar.add_modifiers(base_english)
# print ten random outputs
for i in range(10):
    print(grammar.flatten("#origin#"))
