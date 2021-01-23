a = [int(i) for i in input().split()]
b = []
m = 0
c = 0
l = len(a) - 1
if len(a) == 1:             # Если одно число
    print(a[0])
else:
    while m <= l:           # Больше одного
        if m == 0:          # первое число
            m += 1
            c = a[-1] + a[1]
            b = b + [c]
        elif m == l:        #последнее число
            c = a[0] + a[l - 1]
            b += [c]
            m += 1
        elif m != l and m != 0:     #середина списка
            b += [a[m - 1] + a[m + 1]]
            m += 1
for i in b:
    print(i, end=' ')