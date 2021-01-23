import requests
g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3378_3.txt')
a = g.readline()
g.close()
b = a[8:]
b = b.split('/')
b = '//'.join(b)
b = 'http://'+ b
b = b[0:-1]
print(b)
r = requests.get(b)
r = r.text
print(r)
while r[0] != 'W':
    g = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r)
    print(g.text)
    r = g.text
    print('https://stepic.org/media/attachments/course67/3.6.3/' + r)
print(r)