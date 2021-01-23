Dict = {11: [], 10: [], 9: [], 8: [], 7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
def Read(Str):
    a = Str.split('\t')
    a[0] = int(a[0])
    a[2] = int(a[2])
    Str = [a[0]] + [a[2]]
    return Str
g = open('C:\\Users\\Ryzhk\\Downloads\\dataset_3380_5.txt')
for i in g:
    Dict[Read(i)[0]] += [Read(i)[1]]
g.close()
for i in  range(1, 12):
    if Dict[i] == []:
        print(i, '-')
    else:
        print(i, end=' ')
        print(sum(Dict[i])/len(Dict[i]))