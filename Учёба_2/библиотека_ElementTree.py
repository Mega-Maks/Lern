from xml.etree import ElementTree


def init(xml_input, file_name):
    with open(file_name, 'w') as xml:
        xml.write(xml_input)
    tree = ElementTree.parse(file_name)
    root = tree.getroot()
    return root


def counter(var, root, some_dict):
    if root.findall('cube') == []:
        some_dict[root.attrib['color']] += var
    else:
        some_dict[root.attrib['color']] += var
        for elem in root.findall('cube'):
            counter(var + 1, elem, some_dict)
    return some_dict


def dict_printer(some_dict):
    for key in some_dict:
        print(some_dict[key], end=' ')


def general_function(xml_input):
    root = init(xml_input, 'XML.xml')
    count_dict = counter(1, root, {'red': 0, "green": 0, 'blue': 0})
    dict_printer(count_dict)


general_function(input())
