import math


def sample_function(t):
    if t < -2:
        return -2
    elif -2 <= t < 0:
        return t
    elif t == 0:
        return 0
    else:
        return t * math.sin(1 / t)

