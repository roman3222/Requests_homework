import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
superhero = requests.get(url).text
hero = json.loads(superhero)
intelligence_hero = {}


for heroes in hero:
    if heroes.get('name') == 'Captain America':
        intelligence_hero['Captain America'] = heroes['powerstats']['intelligence']
    if heroes.get('name') == 'Thanos':
        intelligence_hero['Thanos'] = heroes['powerstats']['intelligence']
    if heroes.get('name') == 'Hulk':
        intelligence_hero['Hulk'] = heroes['powerstats']['intelligence']
print('Самым умным супергероем является:', max(intelligence_hero.keys()))