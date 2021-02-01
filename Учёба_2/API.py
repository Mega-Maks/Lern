import requests


def opener(file_name):
    '''
    Открывает файл file_name
    :param file_name: Имя файла
    :return: Лист с чилами
    '''
    with open(file_name) as g:
        number_list = g.read().split('\n')
    return number_list


def responses(number_list, api_url):
    '''
    Узнаёт для каждого числа в number_list есть ли о нём интерестный математический факт
    :param number_list: Лист с чилами
    :param api_url: Ссылка
    :return: Лист с ответами
    '''
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
