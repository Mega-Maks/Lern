import requests as r
import csv
import re
import input_for_contacts as inp

# 7770392
# view-source:https://oauth.vk.com/blank.html
# #access_token=a94dd2e3e0f8cd200bde00db6e49f7435faf2ddac98c464e84fac476023c4438927d06d5fc2f9c52397a4
# &expires_in=86400
# &user_id=181002310
# серверный ключ доступа = d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5

# https://api.vk.com/method/
# friends.get?
# v=5.52&
# user_id=181002310&
# fields=has_mobile,contacts&
# access_token=d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5

# https://api.vk.com/method/
# users.get?
# v=5.52&
# user_ids=mihapil&
# access_token=d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5


def check_string(string):
    """
    проверяем является ли строка номером телефона
    """
    phone = re.sub(r'\b\D', '', string)
    clear_phone = re.sub(r'[\ \(]?', '', phone)
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone):
        return True
    else:
        return False


def checker(some_dict, key):
    """
    Проверяеот есть ли в some_dict ключ key
    :param some_dict: Словарь
    :param key: Ключ
    :return: Если ключа нет то '', а если есть то key
    """
    try:
        return some_dict[key]
    except KeyError:
        return ''


def contacts_dict_creator(input_dict, people_dict=None):
    """
    Превращяет ключ VK в значение для CSV файла
     :param people_dict: Принимает на вход словарь из ВК
     :param input_dict: Словарь со значениями
     :return: Словарь cо значениями подходящими для составления CSV файла
    """
    print(input_dict)
    if people_dict is None:
        people_dict = {}
    contacts_dict = {
        'First Name': checker(people_dict, 'first_name')
        if input_dict['sp_dict']['inf_dict']['first_name'] else '',

        'Last Name': checker(people_dict, 'last_name')
        if input_dict['sp_dict']['inf_dict']['last_name'] else '',

        'Mobile Phone': checker(people_dict, 'mobile_phone')
        if input_dict['sp_dict']['inf_dict']['mobile_phone'] else '',

        'Personal Web Page': 'https://vk.com/{}'.format(people_dict['id'])
        if input_dict['sp_dict']['inf_dict']['id'] else '',

        'Birthday': checker(people_dict, 'bdate')
        if input_dict['sp_dict']['inf_dict']['bdate'] else '',

        'Home City': checker(people_dict[checker(people_dict, 'city')], 'title')
        if input_dict['sp_dict']['inf_dict']['city'] else '',

        'Home Country/Region': checker(people_dict[checker(people_dict, 'country')], 'title')
        if input_dict['sp_dict']['inf_dict']['country'] else '',

        'Notes': checker(people_dict, 'status')
        if input_dict['sp_dict']['inf_dict']['status'] else ''

    }
    return contacts_dict


def id_getter(id_or_nn):
    """
    Запрашивает id польтзователя по его прозвищу
    :param id_or_nn: id пользователя или прозвще
    :return: id Пользователя (string)
    """
    method = "users.get?"
    version = "v=5.52&"
    user_id = "user_ids={}&".format(id_or_nn)
    fields = "fields=bdate,city,country,status&"
    access_token = 'access_token=d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5'
    user_id = r.get('https://api.vk.com/method/' + method + version + user_id + fields + access_token)
    user_id = user_id.json()
    if 'error' in user_id:
        link = 'https://vk.com/{}'.format(id_or_nn)
        raise KeyError('Вы неверно указали id пользователя убедитесть что по ссылке ' + link +
                       ' этот пользователь доступен')
    return user_id


def peoples_getter(user_id):
    method = "friends.get?"
    version = "v=5.52&"
    user_id = "user_id={}&".format(user_id)
    fields = "fields=bdate,city,country,status&"
    access_token = 'access_token=d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5'
    response_dict = r.get('https://api.vk.com/method/' + method + version + user_id + fields + access_token)
    response_dict = response_dict.text
    print(response_dict)
    return response_dict


def csv_writer(input_dict, response_dict):
    """
    Записывает в csv файл данные из словаря
    :return:
    """

    with open('contacts_file.csv', 'w', encoding='utf-8') as w_file:

        fields = list(contacts_dict_creator(input_dict))
        file_writer = csv.writer(w_file)
        file_writer.writerow(fields)
        only_with_phones = input_dict['sp_dict']['inf_dict']['only_with_phones']
        print(response_dict)

        for people_dict in response_dict['response']['items']:
            if only_with_phones:
                dict_for_csv = contacts_dict_creator(input_dict, people_dict)
                print(dict_for_csv)
            else:
                dict_for_csv = contacts_dict_creator(input_dict, people_dict)
                print(dict_for_csv)


if __name__ == '__main__':
    input_dict = inp.inputer()
    user_id = id_getter(input_dict['id or NN'])
    response_dict = peoples_getter(user_id)
    csv_writer(input_dict, response_dict)
