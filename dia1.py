import json
import requests


def getPersonagens():
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

    response = requests.get(api_url)
    return response.text
    
data = getPersonagens()
print(data)