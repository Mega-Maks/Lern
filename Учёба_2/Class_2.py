class Buffer:
    def __init__(self):
        pass
        self.List = []
    def add(self, *a):
        self.List += a
        while len(self.List) >= 5:
            print(sum(self.List[0:5]))
            for i in range(5):
                self.List.pop(0)
    def get_current_part(self):
        return self.List
buf = Buffer()

buf.add(1, 2, 3)
print(buf.get_current_part())
# вернуть [1, 2, 3]

buf.add(4)
print(buf.get_current_part())
# вернуть [1, 2, 3, 4]

buf.add(5)
print(buf.get_current_part())
# вернуть 15 - вывод суммы первой пятерки элементов

buf.add(6)
print(buf.get_current_part())
# вернуть [6]

buf.add(7, 8, 9, 10)
# print(40) – вывод суммы второй пятерки элементов

print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())