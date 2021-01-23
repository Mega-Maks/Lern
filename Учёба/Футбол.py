Dict = dict()
def create_Dict(str):
    '''
    Принимает Строку и возвращает Словарь
    '''
    str = str.split(';')
    str[1] = int(str[1])
    str[3] = int(str[3])
    if str[1] > str[3]:
        if (str[0] in Dict) == False:
            Dict[str[0]] = [1, 1, 0, 0, 3]
        else:
            Dict[str[0]][0] += 1
            Dict[str[0]][1] += 1
            Dict[str[0]][4] += 3
        if (str[2] in Dict) == False:
            Dict[str[2]] = [1, 0, 0, 1, 0]
        else:
            Dict[str[2]][0] += 1
            Dict[str[2]][3] += 1
    elif str[3] > str[1]:
        if (str[2] in Dict) == False:
            Dict[str[2]] = [1, 1, 0, 0, 3]
        else:
            Dict[str[2]][0] += 1
            Dict[str[2]][1] += 1
            Dict[str[2]][4] += 3
        if (str[0] in Dict) == False:
            Dict[str[0]] = [1, 0, 0, 1, 0]
        else:
            Dict[str[0]][0] += 1
            Dict[str[0]][3] += 1
    else:
        if (str[0] in Dict) == False:
            Dict[str[0]] = [1, 0, 1, 0, 1]
        else:
            Dict[str[0]][0] += 1
            Dict[str[0]][2] += 1
            Dict[str[0]][4] += 1
        if (str[2] in Dict) == False:
            Dict[str[2]] = [1, 0, 1, 0, 1]
        else:
            Dict[str[2]][0] += 1
            Dict[str[2]][2] += 1
            Dict[str[2]][4] += 1
    return Dict
n = int(input())
for i in range(n):
    create_Dict(input())
for i in Dict:
    print(i, ':', sep='', end='')
    for j in Dict[i]:
        print(j, end=' ')
    print()