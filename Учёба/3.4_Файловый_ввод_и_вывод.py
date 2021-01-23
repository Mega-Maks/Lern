g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3363_2.txt')
a = g.readline()
g.close()
print(a)
c = ''
symbol = 0
count = '0'
for i in a:
    if i.isalpha():
        c += str(symbol) * int(count)
        symbol = i
        count = ''
    else:
        count += i
c += str(symbol) * int(count)
print(c)
g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3363_2.txt', 'w')
g.write(c)
g.close()