class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False
    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False
    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False
    def __init__(self, iterable, *funcs, judge = judge_any):
        self.pos = 0
        self.neg = 0
        self.List = []
        for i in iterable:
            for j in funcs:
                if j(i):
                    self.pos += 1
                else:
                    self.neg +=1
            if judge(self.pos, self.neg):
                self.List += [i]
            self.pos = 0
            self.neg = 0
    def __iter__(self):
        return iter(self.List)
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]