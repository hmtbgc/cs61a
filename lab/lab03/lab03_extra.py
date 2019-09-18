""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i > (n ** 0.5):
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def helper(x, y):
        if y < 10:
            if y == x:
                return 1
            else:
                return 0
        else:
            c = y % 10
            if c == x:
                return 1 + helper(x, y // 10)
            else:
                return helper(x, y // 10)
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + helper(10 - (n % 10), n // 10)
