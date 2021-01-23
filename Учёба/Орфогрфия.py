a = int(input())
b = set()
for i in range(a):
    b.add(input().lower())
a = int(input())
output = set()
for i in range(a):
    c = input().lower().split()
    for j in c:
        if not (j in b):
            output.add(j)
for i in output:
    print(i)