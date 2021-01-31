namespace_dict = {'global': []}
arguments_dict = {'global': []}


def create_or_namespace(namespace, arg, some_dict):
    '''
    Добовляет в namespace_dict[namespace] arg
     :param namespace: Имя пространства
     :param arg: Имя переменной
     :param some_dict: Словарь вида arguments_dict[namespace] == [namespace, namespace...]
     :return: namespace_dict
    '''
    if namespace in some_dict:
        some_dict[namespace] += [arg]
    else:
        some_dict[namespace] = [arg]
    return some_dict


def search_namespace(arg, namespace, arguments_dict, namespace_dict):
    '''
    Поиск по словарям
     :param arg: Имя переменной
     :param namespace: Имя пространства
     :param arguments_dict: Словарь вида arguments_dict[namespace] == [arg, arg...]
     :param namespace_dict: Словарь вида arguments_dict[namespace] == [namespace, namespace...]
    '''
    while namespace != 'global':
        if arg in arguments_dict[namespace]:
            print(namespace)
            break
        else:
            namespace = namespace_dict[namespace][0]
    else:
        if arg in arguments_dict['global']:
            print('global')
        else:
            print(None)


def add_namespace(namespace, arg, arguments_dict):
    '''
    Добовляет в arguments_dict[namespace] arg
     :param namespace: Имя пространства
     :param arg: Имя переменной
     :param arguments_dict: Словарь вида arguments_dict[namespace] == [arg, arg...]
    :return: arguments_dict
    '''
    if namespace in arguments_dict:
        arguments_dict[namespace] += [arg]
    else:
        arguments_dict[namespace] = [arg]
    return arguments_dict


for i in range(int(input())):
    cmd, namespace, arg = input().split()
    if cmd == 'create':
        namespace_dict = create_or_namespace(namespace, arg, namespace_dict)
    elif cmd == 'add':
        arguments_dict = create_or_namespace(namespace, arg, arguments_dict)
    elif cmd == 'get':
        search_namespace(arg, namespace, arguments_dict, namespace_dict)

# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b


