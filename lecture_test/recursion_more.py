def count_part(n, m):
    '''
    Count the number of ways to give out n(>0) pieces of chocolate
    if nobody can have more than m(>0) pieces

    >>> count_part(6, 4)
    9
    '''
    if n < 0:
        return 0
    elif n == 0 or m == 1:
        return 1
    else:
        return count_part(n - m, m) + count_part(n, m - 1)
