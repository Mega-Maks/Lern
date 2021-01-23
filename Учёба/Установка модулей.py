import requests
g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3378_2.txt')
a = g.read()
g.close()
b = a[8:]
b = b.split('/')
b = '//'.join(b)
b = 'http://'+ b
b = b[0:-1]
r = requests.get(b)
print(r.text)
print(r.text.count('\n'))
