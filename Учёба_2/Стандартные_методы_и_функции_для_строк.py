s = input()
a = input()
b = input()
Chenged = s.replace(a, b)
Count = 0
while Count <= 1000:
    if a in s:
        s = Chenged
        Chenged = Chenged.replace(a, b)
        Count += 1
    else:
        break
if Count > 1000:
    print('Impossible')
else:
    print(Count)