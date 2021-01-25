import requests

api_url = 'http://numbersapi.com/{}/math?json'

with open('dataset_24476_3.txt') as g:
    List = g.read().split('\n')

print(List)

for i in List:
    res = requests.get(api_url.format(i))
    if res.json()['found']:
        print('Interesting')
    else:
        print('Boring')