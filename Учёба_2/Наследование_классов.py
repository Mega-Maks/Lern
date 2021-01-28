def Input(input_str):
    '''
    :param input: str формата '[намиенование класса]:[родитель(и) класса]'
    :return: Лист с назваиями классов (input_list[0] == Ребёнок; input_list[1:] == Родитель(и))
    '''
    input_list = input_str.split()
    if input_list.count(":"):
        input_list.pop(input_list.index(':'))
    return input_list


def init(count_of_inputs):
    '''
    :param count_of_inputs: Количество вводов
    :return: Cловарь с деревом классов вида(dict[Ребёнок] == Родитель)
    '''
    class_dict = {}
    for i in range(count_of_inputs):
        input_list = Input(input())
        # Запись словаря:
        if len(input_list) == 1:  # Только ребёнок
            if input_list[0] in class_dict:
                class_dict[input_list[0]] += ['']
            else:
                class_dict[input_list[0]] = ['']
        else:  # Ребёнок и родитель(и)
            if input_list[0] in class_dict:
                if class_dict[input_list[0]] == ['']:
                    class_dict[input_list[0]] = input_list[1:]
                else:
                    class_dict[input_list[0]] += input_list[1:]
            else:
                class_dict[input_list[0]] = input_list[1:]
    return class_dict


def Serch(parent, chaild, class_dict):
    '''
    Ищет в словаре(class_dict) родителя(parent) от ребёнка(chaild)

    :param parent: Родитель
    :param chaild: Ребёнок
    :param class_dict: Словарь
    :return: 'Yes'/'No'
    '''
    if chaild not in class_dict:
        return 'No'
    elif chaild == parent:
        return 'Yes'
    else:
        if class_dict[chaild] == ['']:
            return 'No'
        elif parent in class_dict[chaild]:
            return 'Yes'
        else:
            for parent in class_dict[chaild]:
                return Serch(parent, chaild, class_dict)
        return 'No'


count_of_inputs = int(input())
class_dict = init(count_of_inputs)

for i in range(int(input())):
    input_list = input().split()
    print(Serch(input_list[0], input_list[1], class_dict))