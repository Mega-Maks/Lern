n = int(input())
Dict2 = {'global': []}
Dict3 = {'global': []}
def Whrite_dict(namesp, arg):
    if arg != 'global':
        Dict2[namesp] = [arg] + Dict2[arg]
    else:
        Dict2[namesp] = ['global']
def Serch(arg, namesp):
    while namesp != 'global':
        if arg in Dict3[namesp]:
            print(namesp)
            break
        else:
            namesp = Dict2[namesp][0]
    else:
        if arg in Dict3['global']:
            print('global')
        else:
            print(None)
for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        Whrite_dict(namesp, arg)
        Dict3[namesp] = []
    elif cmd == 'add':
        Dict3[namesp] += [arg]
    else:
        Serch(arg, namesp)