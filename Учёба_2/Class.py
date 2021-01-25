class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.v = 0

    def can_add(self, v):
        if v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        self.capacity -= v

x = MoneyBox(30)
x.add(16)
x.can_add(3)

print(x.v, x.capacity)