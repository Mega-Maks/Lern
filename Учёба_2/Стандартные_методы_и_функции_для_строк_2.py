s = input()
t = input()
Index = 0
Count = 0
while Index != len(s):
    if s.count(t, Index) > 0:
        Count += 1
        Index += s.index(t, Index) - Index + 1
    else:
        break
print(Count)
