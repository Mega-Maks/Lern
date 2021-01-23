a = int(input())
x = 0
y = 0
for i in range(a):
    List  = input().split()
    List[1] = int(List[1])
    if List[0] == 'север':
        y += List[1]
    elif List[0] == 'юг':
        y -= List[1]
    elif List[0] == 'восток':
        x += List[1]
    elif List[0] == 'запад':
        x -= List[1]
print(x, y)