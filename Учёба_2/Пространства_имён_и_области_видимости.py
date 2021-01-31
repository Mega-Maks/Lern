n = int(input())

Dict2 = {'global': []}
Dict3 = {'global': []}


def Whrite_dict(namespase, arg):
    if arg != 'global':
        Dict2[namespase] = [arg] + Dict2[arg]
    else:
        Dict2[namespase] = ['global']


def Serch(arg, namespase):
    while namespase != 'global':
        if arg in Dict3[namespase]:
            print(namespase)
            break
        else:
            namespase = Dict2[namespase][0]
    else:
        if arg in Dict3['global']:
            print('global')
        else:
            print(None)


for i in range(n):
    cmd, namespase, arg = input().split()
    if cmd == 'create':
        Whrite_dict(namespase, arg)
        Dict3[namespase] = []
    elif cmd == 'add':
        Dict3[namespase] += [arg]
    else:
        Serch(arg, namespase)
