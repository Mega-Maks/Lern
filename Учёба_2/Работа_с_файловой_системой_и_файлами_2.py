import os.path
os.chdir('main')
file_ways_set = set()
with open('text_2', 'w') as file:
    for a, b, c in os.walk('.'):
        print(a)
        print(b)
        print(c)
        for i in c:
            if i[-1] == 'y':
                file_ways_set.add('main' + a[1:] + '\n')
    print(file_ways_set)
    print(sorted(file_ways_set))
    for way in sorted(file_ways_set):
        file.write(way)
