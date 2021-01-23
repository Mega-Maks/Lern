def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
    return d
c = {}
a = 0
while a != 'end' or b != 'end':
    a = int(input())
    b = int(input())
    update_dictionary(c, a, b)
    print(c)