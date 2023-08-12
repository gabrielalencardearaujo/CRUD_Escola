import json
from manager_json import writeJSON

def readFile():
    with open('database/ESCOLA.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())
