i = 0
b = []
a = 0
c = []
while a != 'end':
    a = input()
    if a == 'end':
        break
    else:
        a = [int(i) for i in a.split()]
        b += [i]
        b[i] = a
        i += 1                              #цикл ввода
if a == 'end' and len(b) == 0:
    print()
else:
    n = len(b)
    m = len(b[0])
    c = [[0 for i in range(m)] for j in range(n)]
    l = len(b[0]) - 1
    h = len(b) - 1                          #создание  пустой c и прочее
    for i in range(n):
        for j in range(m):
            if len(b) <= 1 or len(b[0]) <= 1:
                if len(b) == 0 or len(b[0]) == 0:
                    break
                elif len(b) == 1 and len(b[0]) == 1:
                    c[0][0] = b[0][0] * 4
                    break
                elif len(b) == 1:
                    if j == 0:
                        c[0][0] = b[0][1] + (b[0][0] * 2) + b[0][-1]
                    elif j == l:
                        c[0][-1] = b[0][-2] + (b[0][-1] * 2) + b[0][0]
                    else:
                        c[0][j] = b[0][j - 1] + (b[0][j] * 2) + b[0][j + 1]
                elif len(b[0]) == 1:
                    if i == 0:
                        c[0][0] = b[1][0] + (b[0][0] * 2) + b[-1][0]
                    elif i == h:
                        c[-1][0] = b[-2][0] + (b[-1][0] * 2) + b[0][0]
                    else:
                        c[i][0] = b[i - 1][0] + (b[i][0] * 2) + b[i + 1][0]
            elif i == 0 and j == 0:
                c[0][0] = b[0][1] + b[1][0] + b[0][- 1] + b[-1][0]
            elif i == 0 and j == l:
                c[0][-1] = b[0][-2] + b[1][-1] + b[0][0] + b[-1][-1]
            elif i == h and j == 0:
                c[-1][0] = b[0][0] + b[-1][-1] + b[-1][1] + b[-2][0]
            elif i == h and j == l:
                c[-1][-1] = b[0][-1] + b[-1][0] + b[-1][-2] + b[-2][-1]
            elif i == 0:
                c[0][j] = b[-1][j] + b[0][j - 1] + b[0][j + 1] + b[1][j]
            elif i == h:
                c[-1][j] = b[-1][j + 1] + b[-1][j - 1] + b[-2][j] + b[0][j]
            elif j == 0:
                c[i][0] = b[i][j + 1] + b[i + 1][0] + b[i - 1][0] + b[i][-1]
            elif j == l:
                c[i][-1] = b[i][j - 1] + b[i + 1][-1] + b[i - 1][-1] + b[i][0]
            else:
                c[i][j] = b[i + 1][j] + b[i - 1][j] + b[i][j + 1] + b[i][j - 1]                   #заполнение с
for i in range(n):
    for j in range(m):
        if j == l:
            print(c[i][j])
        else:
            print(c[i][j], end=' ')                                                                #вывод