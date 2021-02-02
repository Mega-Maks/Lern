n, k = map(int, input().split())


def C(n, k):
    '''

    :param n:
    :param k:
    :return:
    '''
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


print(C(n, k))
