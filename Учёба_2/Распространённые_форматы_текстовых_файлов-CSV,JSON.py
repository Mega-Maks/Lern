import csv


def dict_writer(key, some_dict):
    '''
    Добовляет в some_dict[key] 1
     :param key: Ключ
     :param some_dict: Словарь
     :return: Словарь
    '''
    if key in some_dict:
        some_dict[key] += 1
    else:
        some_dict[key] = 1
    return some_dict


def count_of_primes():
    '''
    :return: Словарь вида some_dict[prime] == count_of_prime
    '''
    with open('Crimes.csv') as file:
        reader = csv.reader(file)
        some_dict = dict()
        for row in reader:
            if row[2][8:10] == "15":
                some_dict = dict_writer(row[5], some_dict)
    return some_dict


def maximum_in_dict(some_dict):
    '''
    :param some_dict: Словарь с преступлениями
    :return: Вид преступления которое совершили больше всего раз в 2015
    '''
    maximum = 0
    primary_type = None
    for i in some_dict:
        if some_dict[i] > maximum:
            maximum = some_dict[i]
            primary_type = i
    return primary_type


primary_type_dict = count_of_primes()
print(maximum_in_dict(primary_type_dict))
