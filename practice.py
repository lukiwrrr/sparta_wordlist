import requests

api_key = '9d82104e-b3fd-4cdf-906b-8c395fcaa8f8'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)