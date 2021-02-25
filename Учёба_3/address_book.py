import requests as r
import csv
import re


def check_string(string):
    phone = re.sub(r'\b\D', '', string)
    clear_phone = re.sub(r'[\ \(]?', '', phone)
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$',string):
        return bool(string)
    else:
        return False


def dict_checker(dict, key):
    try:
        dict[key]
        return True
    except KeyError:
        return False


def checker(some_dict, value):
    try:
        return some_dict[value]
    except KeyError:
        return ''


def name_transform(vk_dict=dict):
    """
    Превращяет ключ VK в значение для CSV файла
     :param vk_dict: Принимает на вход словарь из ВК
     :return: Словарь cо значениями подходящими для составления CSV файла
    """
    # nickname, domain, sex, bdate, city, country, timezone, photo_50,
    # photo_100, photo_200_orig, has_mobile, contacts, education, online,
    # relation, last_seen, status, can_write_private_message, can_see_all_posts,
    # can_post, universities

    # First Name,Middle Name,Last Name,Title,Suffix,Nickname,Given Yomi,
    # Surname Yomi,E-mail Address,E-mail 2 Address,E-mail 3 Address,
    # Home Phone,Home Phone 2,Business Phone,Business Phone 2,Mobile Phone,
    # Car Phone,Other Phone,Primary Phone,Pager,Business Fax,Home Fax,Other Fax,
    # Company Main Phone,Callback,Radio Phone,Telex,TTY/TDD Phone,IMAddress,Job Title,
    # Department,Company,Office Location,Manager's Name,Assistant's Name,Assistant's Phone,
    # Company Yomi,Business Street,Business City,Business State,Business Postal Code,Business Country/Region,
    # Home Street,Home City,Home State,Home Postal Code,Home Country/Region,Other Street,Other City,Other State,
    # Other Postal Code,Other Country/Region,Personal Web Page,Spouse,
    # Schools,Hobby,Location,Web Page,Birthday,Anniversary,Notes

    pass
    Phone_val = checker(vk_dict, 'mobile_phone')
    google_contacts_dict = {
        'First Name': checker(vk_dict, 'first_name'),
        'Last Name': checker(vk_dict, 'last_name'),
        'Mobile Phone': Phone_val ,

    }
    return google_contacts_dict


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

method = "friends.get?"
version = "v=5.52&"
user_id = "user_id={}&".format(input("Введите id Пользователя данные о друзьях которого хотите запистать "))
fields = """fields=contacts&"""
access_token = 'access_token=d708f3bfd708f3bfd708f3bfe1d77e62a7dd708d708f3bfb73c21bf739970498293c9f5'
json_dict = r.get('https://api.vk.com/method/' +
                  method + version + user_id + fields + access_token
                  )

response_dict = json_dict.json()
dict_for_csv = name_transform()
print('count = ', response_dict['response']['count'])
print()

with open('contacts_file.csv', 'w', encoding='utf-8') as w_file:
    fields = [x for x in dict_for_csv]
    file_writer = csv.writer(w_file)
    file_writer.writerow(fields)
    for people_dict in response_dict['response']['items']:
        dict_for_csv = name_transform(people_dict)
        if check_string(dict_for_csv['Mobile Phone']):
            file_writer.writerow([dict_for_csv[x] for x in dict_for_csv])
        # else:
            # dict_for_csv['Mobile Phone'] = ''
            # file_writer.writerow([dict_for_csv[x] for x in dict_for_csv])
