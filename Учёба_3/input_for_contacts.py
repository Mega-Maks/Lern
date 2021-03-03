def inputer():
    first_question = bool(int(input(
        'Здравствуйте, это прогрмамма для экспорта контактов из VK или Facebook\n'
        'в CSV формат, пожалуста выберите откуда вы будете экспортировать контакты(1 - VK, 0 - Facebook)\n'
        '(к сожалению Facebook пока недоступен)\n')))

    user_id = input('Введите id пользователя информацию о друзьях когорого хотите узнать или его прозвище'
                    '(в адресной строке на его страничке) ')

    sp_information = bool(int(input('в файл запишется только имя, фамилия и номер телефона(есили он есть),\n '
                                    'а также если номера телефона не будет то контакт не будет занесён,\n'
                                    'если вы хотите занести другие свединия или людей без телефонов то пройдите опрос\n'
                                    '(1 - Да, 0 - Нет)\n')))

    if sp_information:
        print('Будте бдительны программа приниимает только числа не вводите текст')
        sp_dict = {'default': False, 'inf_dict': {
            'only_with_phones': not bool(int(input('Вы хотите выводить людей у которых нет номера телефона?'
                                                   '(1 - Да, 0 - Нет) '))),
            'first_name': True,
            'id': bool(int(input('Вы хотите выводить ссылку на профиль человека?'
                                 '(1 - Да, 0 - Нет) '))),
            'last_name': bool(int(input('Вы хотите выводить фамилию человека?'
                                        '(1 - Да, 0 - Нет) '))),
            'bdate': bool(int(input('Вы хотите выводить дату рождения человека?'
                                    '(1 - Да, 0 - Нет) '))),
            'city': bool(int(input('Вы хотите выводить город человека?'
                                   '(1 - Да, 0 - Нет) '))),
            'country': bool(int(input('Вы хотите выводить страну человека?'
                                      '(1 - Да, 0 - Нет) '))),
            'status': bool(int(input('Вы хотите выводить статус человека?'
                                     '(1 - Да, 0 - Нет) '))),
            'mobile_phone': True
        }}
    else:
        sp_dict = {'default': True, 'inf_dict': {
            'only_with_phones': True,
            'first_name': True,
            'id': False,
            'last_name': True,
            'bdate': False,
            'city': False,
            'country': False,
            'status': False,
            'mobile_phone': True
        }}

    input_dict = {
        'V or F': first_question,
        'id or NN': user_id,
        'sp_dict': sp_dict,
    }
    return input_dict


print('import was ok')
