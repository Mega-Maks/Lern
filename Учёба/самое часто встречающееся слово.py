g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3363_3.txt')
a = g.read().strip()
g.close()
print(a)
s = set()
c = a.split()
max = 0
maximum = c[0]
mmax = []
for i in c:
    s.add(i)
for i in s:
    if c.count(i) > max:
        max = c.count(i)
        maximum = i
for i in s:
    if c.count(i) == max:
        mmax += [i]
        mmax.sort()
g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3363_3.txt', 'w')
g.write(mmax[0])
g.write(' ')
g.write(str(max))
g.close()
