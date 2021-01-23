a = int(input())
b = int(input())
s = 0
k = 0
while a % 3 != 0:
    a += 1
for i in range(a, b + 1, 3):
    s += i
    k += 1
print(s / k)