a = [int(i) for i in input().split()]
a.sort()
h = 1
m = 1
j = []
c = []
g = []
if len(a) == 1 or len(a) == 0:
    True
else:
    for i in a:
        b = a.count(i)
        if b > 1:
            c += [i]
    if len(c) == 1 or len(c) == 0:
        True
    else:
        l = len(c) - c.count(c[-1])
        g += [c[-1]]
        while m <= l:
            if c[m - 1] != c[m]:
                g += [c[m - 1]]
            m += 1
g.sort()
for i in g:
    print(i, end=' ')