import requests
API = 'de55a68d68c3fdb19405af987bc3c026'
api_url = 'http://numbersapi.com/random/year?json'
number = input()
params = {
    'number': number,
    'appid': API,
    'type': 'math',
    'json': 'true'
}

with open('API') as g:
    List = g.read().split('\n')

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.text)