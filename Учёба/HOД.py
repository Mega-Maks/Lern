a = int(input())
b = int(input())
y = a
x = b
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(int((x * y) / b))