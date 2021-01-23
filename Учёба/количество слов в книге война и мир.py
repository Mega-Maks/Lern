s = set()
a = input().lower().split()
for i in a:
    s.add(i)
for i in s:
    print(i, end=' ')
    print(a.count(i))
