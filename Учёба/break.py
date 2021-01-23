a = 0
while True:
    a = float(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print(int(a))