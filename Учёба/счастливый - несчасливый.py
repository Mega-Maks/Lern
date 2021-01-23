a = int(input())
b = a % 1000
b = b % 10 + b % 100//10 + b//100
c = a//1000
c = c % 10 + c % 100//10 + c//100
if c == b:
    print('Счастливый')
else:
    print('Обычный')