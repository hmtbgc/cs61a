def naturals():

 """
 >>> nat = naturals()
 >>> next(nat)
 0
 >>> next(nat)
 1
 >>> nat1, nat2 = naturals(), naturals()
 >>> [next(nat1) * next(nat2) for _ in range(5)]
 [0, 1, 4, 9, 25]
 """
 x = 0
 while True:
    yield x
    x += 1


def gen():
    start = 0
    while start != 10:
        yield start
        start += 1


def map_gen(fn, iter1):
    """
    >>> i = iter([1, 2, 3, 4])
    >>> fn = lambda x: x**2
    >>> m = map_gen(fn, i)
    >>> next(m)
    1
    >>> next(m)
    4
    >>> next(m)
    9
    >>> next(m)
    16
    >>> next(m)
    Traceback (most recent call last):
      ...
    StopIteration
    """
    "*** YOUR CODE HERE ***"
    try:
        while True:
            item = next(iter1)
            yield fn(item)
    except StopIteration:
        pass


def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b_yield_from(a, b):
    yield from a
    yield from b

def countdown(k):
    if k == 0:
        yield 'bottom'
    else:
        yield k
        yield from countdown(k - 1)
        
