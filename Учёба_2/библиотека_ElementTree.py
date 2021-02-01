from xml.etree import ElementTree


def init(xml_input, file_name):
    '''
    :param xml_input: input XML string
    :param file_name: file name for write
    :return: root
    '''
    with open(file_name, 'w') as xml:
        xml.write(xml_input)
    tree = ElementTree.parse(file_name)
    root = tree.getroot()
    return root


def counter(level_number, root, some_dict):
    '''
    :param level_number: level number
    :param root: up root
    :param some_dict: {'red': some_number, "green": some_number, 'blue': some_number}
    :return: some_dict
    '''
    some_dict[root.attrib['color']] += level_number
    for elem in root.findall('cube'):
        counter(level_number + 1, elem, some_dict)
    return some_dict


def dict_printer(some_dict):
    '''
    Печатает словарь some_dict
    :param some_dict: Словарь
    '''
    for key in some_dict:
        print(some_dict[key], end=' ')


def general_function(xml_input):
    '''
    Генеральная функция которая вызывает все остальные функции
    :param xml_input: input XML string
    '''
    root = init(xml_input, 'XML.xml')
    count_dict = counter(1, root, {'red': 0, "green": 0, 'blue': 0})
    dict_printer(count_dict)


general_function(input())
