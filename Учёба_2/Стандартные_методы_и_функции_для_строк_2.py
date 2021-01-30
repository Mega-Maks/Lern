def Count(s: str, t: str):
    '''

    :param s: Строка в которой мы ищем количество вхождений строки t
    :param t: Строка t
    :return:
    '''
    index = 0
    count = 0

    while index != len(s):
        if s.count(t, index) > 0:
            count += 1
            index += s.index(t, index) - index + 1
        else:
            break
    return count


print(Count(input(), input()))
