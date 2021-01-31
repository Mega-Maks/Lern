Set = set()
objects = [1, 2, 3, 4, 5, True]
for i in objects:
    Set.add(id(i))
print(len(Set))
