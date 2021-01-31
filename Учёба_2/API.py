import requests


def opener(file_name):
    with open(file_name) as g:
        number_list = g.read().split('\n')
    return number_list


def responses(number_list, api_url):
    answer_list = []
    for number in number_list:
        res = requests.get(api_url.format(number))
        if res.json()['found']:
            print('Interesting')
            answer_list.append('Interesting')
        else:
            print('Boring')
            answer_list.append('Boring')
    return answer_list


number_list = opener('dataset_24476_3.txt')
responses(number_list, 'http://numbersapi.com/{}/math?json')
