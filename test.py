from collections import defaultdict as dfd


def f(sec_n, is_n):
    for i in mas[sec_n]:
        if i not in ans_mas:
            ans_mas[i] = is_n
    for i in mas[sec_n]:
        if ans_mas[i] == is_n:
            f(i, is_n + 1)


mas = dfd(lambda: [])
ans_mas = dfd(lambda: 0)
n = int(input())
for i in range(n):
    a = input().split()
    mas[a[0]].append(a[1])
    mas[a[0]].append(a[2])
    mas[a[1]].append(a[0])
    mas[a[1]].append(a[2])
    mas[a[2]].append(a[0])
    mas[a[2]].append(a[1])
ans_mas["Isenbaev"] = 0
f("Isenbaev", 1)
for i in mas:
    if i not in ans_mas:
        ans_mas[i] = "undefined"
ans_mas = sorted(ans_mas.items(), key=lambda x: x[0])
for i in ans_mas:
    print(i[0], i[1])
