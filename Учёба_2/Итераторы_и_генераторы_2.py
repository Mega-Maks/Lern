import itertools


def primes():
    number = 2
    prime = True
    while prime:
        k = 0
        for i in range(1, number + 1):
            if number % i == 0:
                k += 1
        if k == 2:
            yield number
        number += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
