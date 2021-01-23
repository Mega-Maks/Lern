a = int(input())
m = 1
b = []
s = set()
d = dict()
c = []
while m <= a:
    b += [int(input())]
    m += 1
for i in b:
    s.add(i)
for i in s:
    d[i] = f(i)
for i in b:
    print(d[i])

