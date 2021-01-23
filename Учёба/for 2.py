a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\t', end='')
left = []
right = []
for i in range(a, b + 1):
    left += [i]
for i in range(c, d + 1):
    right += [i]
def count(x):
    x = str(x)
    x = x.rjust(5)
    return x.count(' ')
# Функция для исчисления промежутков
for i in right:
    print(i, end=(count(i) * ' '))
print()
for i in left:
    print(i, end=((count(i) - 1) * ' '))
    m = 0
    while m <= (len(right) - 1):
        print(i * right[m], end=(count(i * right[m]) * ' '))
        m += 1
    print()