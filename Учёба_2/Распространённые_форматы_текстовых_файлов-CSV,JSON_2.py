import json


def dict_writer(key, value, some_dict):
    '''

    :param key: Ключ
    :param value: Значение
    :param some_dict: Словарь в которйн надо добавить значене
    :return:
    '''
    if key in some_dict:
        some_dict[key] += [value]
    else:
        some_dict[key] = [value]


def counter(parent_name, some_dict, set_of_child):
    '''

    :param parent_name: Имя родителя
    :param some_dict: Словарь для поиска
    :param set_of_child:
    :return:
    '''
    if parent_name in some_dict:
        for parent in some_dict[parent_name]:
            set_of_child.add(parent)
            counter(parent, some_dict, set_of_child)
    return len(set_of_child)


def create_class_dict(list_of_dicts: list):
    '''

    :param list_of_dicts: Лист со словарями
    :return: Словарь вида key == [parent] / value == [child]
    '''
    some_dict = {}
    for elem in list_of_dicts:
        for child in elem['parents']:
            dict_writer(child, elem['name'], some_dict)
    return some_dict

def add_class_with_empty_childs(list_with_dicts: list, some_dict):
    '''
    Добовляет в словарь классы не имеющие детей
     :param list_with_dicts: Лист со словорями формата key == 'name': value == class name,
      key == 'parents': value == class parents
    :param some_dict: Словарь с классами которые не имеют детей
    :return: Словарь с классами у которых нет детей
    '''
    for Dict in list_with_dicts:
        if Dict["name"] not in some_dict:
            some_dict[Dict["name"]] = []
    return some_dict


def count_printer(dict_with_classes: dict, Print=True):
    '''
    Выводит данные в формате [имя класса : сколько у него детей + 1]
     :param dict_with_classes: Словарь с классами
     :param Print: По умолчанию печатет, Если False, то не выводит данные
    '''
    answer_list = []
    for parent_name in sorted(dict_with_classes):
        count = counter(parent_name, dict_with_classes, set())
        if Print:
            print(parent_name, ':', count + 1)
        answer_list.append([parent_name, ':', count + 1])
    return answer_list


def opener(string):
    '''

    :param string: Строка формата JSON
    :return: Лист со словарями
    '''
    with open('file.json', 'w') as json_file:
        json_file.write(string)

    with open('file.json') as json_file:
        json_list = json.load(json_file)
    return json_list


def test_block():
    if usual_test():
        print('usual_test - OK')
    else:
        print('usual_test - Fail')
    if global_test():
        print('global_test - OK')
    else:
        print('global_test - Fail')
    if global_test2():
        print('global_test2 - OK')
    else:
        print('global_test2 - Fail')


def usual_test():
    answer = [['A', ':', 3],
              ['B', ':', 1],
              ['C', ':', 2]]
    json_list = '''[{"name": "A", "parents": []},
                    {"name": "B", "parents": ["A", "C"]},
                    {"name": "C", "parents": ["A"]}]'''
    json_list = opener(json_list)
    dict_with_classes = create_class_dict(json_list)
    dict_with_classes = add_class_with_empty_childs(json_list, dict_with_classes)
    answer_list = count_printer(dict_with_classes, Print=False)
    if answer_list == answer:
        return True
    else:
        return False


def global_test():
    answer = [['A', ':', 5],
              ['B', ':', 1],
              ['C', ':', 4],
              ['D', ':', 2],
              ['E', ':', 1],
              ['F', ':', 3]]
    json_list = '''[{"name": "B", "parents": ["A", "C"]},
                    {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []},
                    {"name": "D", "parents":["C", "F"]},
                    {"name": "E", "parents":["D"]},
                    {"name": "F", "parents":[]}]'''
    json_list = opener(json_list)
    dict_with_classes = create_class_dict(json_list)
    dict_with_classes = add_class_with_empty_childs(json_list, dict_with_classes)
    answer_list = count_printer(dict_with_classes, Print=False)
    if answer_list == answer:
        return True
    else:
        return False


def global_test2():
    answer = [['A', ':', 10],
              ['B', ':', 5],
              ['C', ':', 5],
              ['D', ':', 4],
              ['E', ':', 1],
              ['F', ':', 2],
              ['G', ':', 1],
              ['TH', ':', 1],
              ['V', ':', 2],
              ['W', ':', 1],
              ['X', ':', 5],
              ['Y', ':', 3],
              ['Z', ':', 3],
              ['ZY', ':', 2],
              ['ZZZ', ':', 3]]
    json_list = """[{"name": "G", "parents": ["ZZZ"]}, 
                     {"name": "TH", "parents": ["ZZZ"]},
                     {"name": "G", "parents": ["ZY"]}, 
                     {"name": "G", "parents": ["F"]}, 
                     {"name": "A", "parents": []}, 
                     {"name": "B", "parents": ["A"]}, 
                     {"name": "C", "parents": ["A"]}, 
                     {"name": "D", "parents": ["B", "C"]},
                     {"name": "E", "parents": ["D"]}, 
                     {"name": "F", "parents": ["D"]}, 
                     {"name": "X", "parents": []},
                     {"name": "Y", "parents": ["X", "A"]},
                     {"name": "Z", "parents": ["X"]},
                     {"name": "V", "parents": ["Z", "Y"]},
                     {"name": "W", "parents": ["V"]}]"""
    json_list = opener(json_list)
    dict_with_classes = create_class_dict(json_list)
    dict_with_classes = add_class_with_empty_childs(json_list, dict_with_classes)
    answer_list = count_printer(dict_with_classes, Print=False)
    if answer_list == answer:
        return True
    else:
        return False


def general_function():
    json_list = opener(input())
    dict_with_classes = create_class_dict(json_list)
    dict_with_classes = add_class_with_empty_childs(json_list, dict_with_classes)
    answer_list = count_printer(dict_with_classes)


general_function()