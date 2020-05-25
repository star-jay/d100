import json

with open("dndProffessions.json") as f:
    content = [
        line[line.find('.') + 2:].replace("\n", '').replace("/", '')
        for line in f.readlines()
        if line[0] in "0123456789"
    ]

content = {
    "description": "A list of occupations (jobs that people might have).",
    "professions": content
}


writing_file = open("dndProffessions2.json", "+w")
json.dump(content, fp=writing_file)
