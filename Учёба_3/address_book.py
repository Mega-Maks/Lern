import requests as r
import csv
import re
import input_for_contacts as inp


def phone_checker(string):
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
    if people_dict is None:
        people_dict = {}
    if input_dict['V or F']:
        contacts_dict = {
            'First Name': checker(people_dict, 'first_name')
            if input_dict['sp_dict']['inf_dict']['first_name'] else '',

            'Last Name': checker(people_dict, 'last_name')
            if input_dict['sp_dict']['inf_dict']['last_name'] else '',

            'Mobile Phone': people_dict['mobile_phone']
            if input_dict['sp_dict']['inf_dict']['mobile_phone'] and
            phone_checker(checker(people_dict, 'mobile_phone')) else '',

            'Personal Web Page': 'https://vk.com/id{}'.format(people_dict['id'])
            if input_dict['sp_dict']['inf_dict']['id'] and
            checker(people_dict, 'id') != '' else '',

            'Birthday': checker(people_dict, 'bdate')
            if input_dict['sp_dict']['inf_dict']['bdate'] else '',

            'Home City': checker(people_dict['city'], 'title')
            if input_dict['sp_dict']['inf_dict']['city'] and
            checker(people_dict, 'city') != '' else '',

            'Home Country/Region': checker(people_dict['country'], 'title')
            if input_dict['sp_dict']['inf_dict']['country'] and
            checker(people_dict, 'country') != '' else '',

            'Notes': checker(people_dict, 'status')
            if input_dict['sp_dict']['inf_dict']['status'] else ''

        }
    else:
        contacts_dict = {
            'First Name': checker(people_dict, 'first_name')
            if input_dict['sp_dict']['inf_dict']['first_name'] else '',

            'Last Name': checker(people_dict, 'last_name')
            if input_dict['sp_dict']['inf_dict']['last_name'] else '',

            'Mobile Phone': people_dict['mobile_phone']
            if input_dict['sp_dict']['inf_dict']['mobile_phone'] and
               phone_checker(checker(people_dict, 'mobile_phone')) else '',

            'Personal Web Page': 'https://vk.com/id{}'.format(people_dict['id'])
            if input_dict['sp_dict']['inf_dict']['id'] and
               checker(people_dict, 'id') != '' else '',

            'Birthday': checker(people_dict, 'bdate')
            if input_dict['sp_dict']['inf_dict']['bdate'] else '',

            'Home City': checker(people_dict['city'], 'title')
            if input_dict['sp_dict']['inf_dict']['city'] and
               checker(people_dict, 'city') != '' else '',

            'Home Country/Region': checker(people_dict['country'], 'title')
            if input_dict['sp_dict']['inf_dict']['country'] and
               checker(people_dict, 'country') != '' else '',

            'Notes': checker(people_dict, 'status')
            if input_dict['sp_dict']['inf_dict']['status'] else ''

        }
    return contacts_dict


def id_getter(id_or_nn, V_or_F):
    """
    Запрашивает id польтзователя по его прозвищу
    :param id_or_nn: id пользователя или прозвще
    :return: id Пользователя (string)
    """
    if V_or_F:
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
    else:
        pass
    return user_id


def peoples_getter(user_id, V_or_F):
    """
    Запрашивет по id пользователя его данные
    :param user_id: id пользователя
    :return: словарь с данными о ользователях
    """
    if V_or_F:
        method = "friends.get?"
        version = "v=5.52&"
        user_id = "user_id={}&".format(user_id)
        fields = "fields=bdate,city,country,status,contacts&"
        access_token = 'access_token=d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5'
        response_dict = r.get('https://api.vk.com/method/' + method + version + user_id + fields + access_token)
        response_dict = response_dict.json()
        if 'error' in response_dict:
            raise KeyError('https://api.vk.com/method/' + method + version + user_id + fields + access_token)
    else:
        pass
    return response_dict


def csv_writer(input_dict, response_dict):
    """
    Записывает в csv файл данные из словаря
    :param input_dict: словарь со значениями для ввода
    :param response_dict: словарь с данными о людях
    """

    with open('contacts_file.csv', 'w', encoding='utf-8') as w_file:
        if input_dict['V or F']:
            fields = list(contacts_dict_creator(input_dict))
            file_writer = csv.writer(w_file)
            file_writer.writerow(fields)
            only_with_phones = input_dict['sp_dict']['inf_dict']['only_with_phones']

            for people_dict in response_dict['response']['items']:
                if only_with_phones:
                    dict_for_csv = contacts_dict_creator(input_dict, people_dict)
                    if dict_for_csv['Mobile Phone'] != '':
                        file_writer.writerow([dict_for_csv[x] for x in dict_for_csv])
                else:
                    dict_for_csv = contacts_dict_creator(input_dict, people_dict)
                    file_writer.writerow([dict_for_csv[x] for x in dict_for_csv])
        else:
            pass


if __name__ == '__main__':
    input_dict = inp.inputer()
    user_dict = id_getter(input_dict['id or NN'], input_dict['V or F'])
    response_dict = peoples_getter(user_dict['response'][0]['id'], input_dict['V or F'])
    csv_writer(input_dict, response_dict)
