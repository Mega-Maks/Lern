a = int(input())
b = int(input())
c = int(input())
d = []
d += [a, b, c]
e = sorted(d, reverse=True)
d = e
print(d[0])
print(d[2])
print(d[1])