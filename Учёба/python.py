a = input()
if a == 'треугольник':
    b = float(input())
    c = float(input())
    d = float(input())
    p = (b+c+d)/2
    print((p*(p-b)*(p-c)*(p-d))**0.5)
elif a == 'прямоугольник':
    b = float(input())
    c = float(input())
    print(b*c)
elif a == 'круг':
    b = float(input())
    print(3.14*b**2)