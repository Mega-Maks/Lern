n = int(input())
Dict = {}
def Input(input):
    List = input.split()
    if List.count(":"):
        List.pop(List.index(':'))
    return List
for i in range(n):
    List = Input(input())
    if len(List) == 1:
        if List[0] in Dict:
            Dict[List[0]] += ['']
        else:
            Dict[List[0]] = ['']
    else:
        if List[0] in Dict:
            if Dict[List[0]] == ['']:
                Dict[List[0]] = List[1:]
            else:
                Dict[List[0]] += List[1:]
        else:
            Dict[List[0]] = List[1:]
Dict2 = Dict.copy()
for i in Dict2:
    for j in Dict[i]:
        if j == '':
            pass
        elif j in Dict:
            pass
        else:
            Dict[j] = ['']
print(Dict)
n = int(input())
var = ''
List = []
def Check(Parent, Chaild):
    if Parent in Dict[Chaild]:
        return True
    elif Dict[Chaild] == ['']:
        return None
    else:
        return False
def Serch(Parent, Chaild):
    if Chaild not in Dict:
        return ''
    elif Chaild == Parent:
        return Chaild
    else:
        if Dict[Chaild] == '':
            pass
        elif Parent in Dict[Chaild]:
            return Chaild
        elif Check(Parent, Chaild) == False:
            for i in Dict[Chaild]:
                if Serch(Parent, i) == i:
                    return Chaild
                    break
        return ''
for i in range(n):
    List.append(input())
m = 0
List2 = []
for i in List:
    for j in List[0:m]:
        var = Serch(j, i)
        if var != '':
            if var not in List2:
                List2 += [var]
    m += 1
for i in List2:
    print(i)
print(List)
