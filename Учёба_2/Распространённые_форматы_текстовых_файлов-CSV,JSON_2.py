import json
Dict = {}
flip_dict = {}
Set = set()
def Dictwriter(key, value, Dict):
    if key in Dict:
        Dict[key] += [value]
    else:
        Dict[key] = [value]
def Counter(Name):
    if Name in flip_dict:
        for parent in flip_dict[Name]:
            Set.add(parent)
            Counter(parent)
    return len(Set)
def Flip_dict():
    for elem in List:
        if elem['parents'] != []:
            for i in elem['parents']:
                Dictwriter(i, elem['name'], flip_dict)
with open('file.json', 'w') as g:
    g.write(input())
with open('file.json') as g:
    List = json.load(g)
Flip_dict()
for i in List:
    if i["name"] not in flip_dict:
        flip_dict[i["name"]] = []
for i in sorted(flip_dict):
    print(i, ':', Counter(i) + 1)
    Set.clear()

# Correct output
# A : 10
# B : 5
# C : 5
# D : 4
# E : 1
# F : 2
# G : 1
# TH : 1
# V : 2
# W : 1
# X : 5
# Y : 3
# Z : 3
# ZY : 2
# ZZZ : 3