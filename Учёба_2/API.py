import requests

api_url = 'http://numbersapi.com/{}/math?json'
number = input()

with open('API') as g:
    List = g.read().split('\n')

res = requests.get(api_url.format(number))

if res.json()['found']:
    print('Interesting')
else:
    print('Boring')