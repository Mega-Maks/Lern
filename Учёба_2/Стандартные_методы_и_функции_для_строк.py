def Count(s: str, a: str, b: str):

    '''

    :param s: Строка в котрой мы ищем вхождение строки а и заменяем его на строку b
    :param a: Cтрока a
    :param b: Cтрока b
    :return: Минимальное количество замен, при котором в строке s не останется вхожений стороки a
    '''

    count = 0
    chenged = s.replace(a, b)
    while count <= 1000:
        if a in s:
            s = chenged
            chenged = chenged.replace(a, b)
            count += 1
        else:
            break
    return count


count = Count(input(), input(), input())
if count > 1000:
    print('Impossible')
else:
    print(count)
