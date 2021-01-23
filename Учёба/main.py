i = 0
a = 0
while i < 5:
    print('*')
    a += 1
    if i % 2 == 0:
        print('**')
        a += 2
    if i > 2:
        print('***')
        a += 3
    i = i + 1
print(a)