a = input()
c = 1
m = 1
j = ''
l = len(a) - 1
while m <= l:
    if a[m] == a[m - 1]:
        c += 1
    else:
        j += a[m-1] + str(c)
        c = 1
    m += 1
j += a[m - 1] + str(c)
print(j)