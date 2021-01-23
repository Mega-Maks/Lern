List = []
with open('C:\\Users\\Ryzhk\\PycharmProjects\\Учёба\\Учёба_2\\text') as t:
    List += [t.readline().rstrip()]
    for i in t:
        List += [i.rstrip()]
List = List[-1:0:-1] + [List[0]]
with open('C:\\Users\\Ryzhk\\PycharmProjects\\Учёба\\Учёба_2\\text_2', 'w') as t:
    for i in List:
        t.write(i + '\n')