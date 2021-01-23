import os.path
os.chdir('main')
Set = set()
with open('C:\\Users\\Ryzhk\\PycharmProjects\\Учёба\\Учёба_2\\text_2', 'w') as g:
    for a, b, c in os.walk('.'):
        for i in c:
            if i[-1] == 'y':
                Set.add('main' + a[1:] + '\n')
    print(Set)
    print(sorted(Set))
    for i in sorted(Set):
        g.write(i)