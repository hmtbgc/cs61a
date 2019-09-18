def fib_iter(n):

    """

    >>> x = fib_iter(4)
    >>> next(x)
    0
    >>> next(x)
    1
    >>> next(x)
    1
    >>> next(x)
    2

    """

    a, b = 0, 1
    ans = [a, b]
    for i in range(n - 2):
        a, b = b, a + b
        ans.append(b)
    return iter(ans)
