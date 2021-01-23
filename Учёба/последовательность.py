a = int(input())
i = 1
c = []
while i <= a :
    m = 1
    while m <= i and m <= a:
        c += [i]
        m += 1
    i += 1
j = 0
while j < a:
    print(c[j], end=' ')
    j += 1

