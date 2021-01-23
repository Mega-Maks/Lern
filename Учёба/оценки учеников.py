g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3363_4.txt')
a = g.read().strip().split('\n')
g.close()
print(a)
m = 0
мат = 0
физ = 0
рус = 0
for i in a:
    a[m] = i.split(';')
    мат += float(a[m][1])
    физ += float(a[m][2])
    рус += float(a[m][3])
    a[m] = (int(a[m][1]) + int(a[m][2]) + int(a[m][3])) / 3
    m += 1
print(a)
m = 0
g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3363_4.txt', 'w')
for i in a:
    g.write(str(a[m]))
    g.write('\n')
    m +=1
g.write(str(мат/len(a)))
g.write(' ')
g.write(str(физ / len(a)))
g.write(' ')
g.write(str(рус / len(a)))
g.close()