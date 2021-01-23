a = 0
for i in range(1, 51):
    for j in range(1, 101):
        a += 2 ** (j * i)
print(a)