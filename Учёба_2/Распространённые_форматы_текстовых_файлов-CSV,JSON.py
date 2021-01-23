import csv
Dict = {}
List = []
Max = 0
def Dictwriter(key):
    if key in Dict:
        Dict[key] += 1
    else:
        Dict[key] = 1
with open('Crimes.csv') as g:
    reader = csv.reader(g)
    for row in reader:
        if row[2][8:10] == "15":
            Dictwriter(row[5])
for i in Dict:
    print(i, Dict[i])
    if Dict[i] > Max:
        Max = Dict[i]
        key = i
print(key, Max)