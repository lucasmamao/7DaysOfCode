import json
import requests
from googletrans import Translator


def getPersonagens():
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'
    response = requests.get(api_url)
    data = json.loads(response.text)
    return data
    
def traduzir(data):
    translator = Translator()

    for personagem in data:
        text = personagem['name']
        tradução=translator.translate(text,src='en',dest='pt')
        personagem['name']= tradução.text
        print(personagem['name'])
        if('affiliation' in personagem):
            text = personagem['affiliation']
            tradução=translator.translate(text,src='en',dest='pt')
            personagem['affiliation']= tradução.text
            print(personagem['affiliation'])
        else:
            print("sem chave")
    return data
Personagens=getPersonagens()
Tradução=traduzir(Personagens)
print(Tradução)
