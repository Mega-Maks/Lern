a = input()
P = True
l = 0
m  = -1
for i in a:
    if a[l] != a[m]:
        P = False
    l += 1
    m -= 1
if P == True:
    print('палиндром')
else:
    print('непалиндром')