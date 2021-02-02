def reader():
    '''
    Читает файл и записывает его посточно в лист
    :return: list
    '''
    list_with_input_data = []
    with open('C:\\Users\\Ryzhk\\PycharmProjects\\Учёба\\Учёба_2\\text') as file:
        list_with_input_data += [file.readline().rstrip()]
        for string in file:
            list_with_input_data += [string.rstrip()]
    print(list_with_input_data)
    return list_with_input_data


def flipper(some_list: list):
    '''
    Переворачивает лист
    :param some_list: list
    :return: flip_list
    '''
    print(some_list)
    some_list = some_list[-1:0:-1] + [some_list[0]]
    return some_list


def writer():
    '''
    Записывает в файл text_2 превёрнутый лист
    '''
    with open('C:\\Users\\Ryzhk\\PycharmProjects\\Учёба\\Учёба_2\\text_2', 'w') as file:
        for string in list_with_output_data:
            file.write(string + '\n')


list_with_input_data = reader()
list_with_output_data = flipper(list_with_input_data)
writer()
