import math
import random
for i in range(900):
    x = (random.randrange(-10, 50) / random.randrange(-10, -1) + random.randrange(1, 10)) * random.randrange(-10, 10)
    y = (random.randrange(-10, 50) / random.randrange(-10, -1) + random.randrange(1, 10)) * random.randrange(-10, 10)
    if math.floor(x) + math.floor(y) + math.floor(x + y) <= math.floor(2 * x) + math.floor(2 * y):
        print(math.floor(x) + math.floor(y) + math.floor(x + y), '<=', math.floor(2 * x) + math.floor(2 * y))
    else:
        print('                   ', math.floor(x) + math.floor(y) + math.floor(x + y), '>=', math.floor(2 * x) + math.floor(2 * y))