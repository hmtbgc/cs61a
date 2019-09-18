def count_up(n):
    '''
    Prints numbers from 1 to n.

    >>> count_up(1)
    1
    >>> count_up(2)
    1
    2
    >>> count_up(4)
    1
    2
    3
    4
    '''
    "*** YOUR CODE HERE ***"
    if n == 1:
        print(1)
    else:
        count_up(n - 1)
        print(n)

def sum_digits(n):
    '''
    Calculates the sum of the digits 'n'

    >>> sum_digits(9)
    9
    >>> sum_digits(19)
    10
    >>> sum_digits(2019)
    12
    '''
    "*** YOUR CODE HERE ***"
    if n < 10:
        return n
    else:
        return sum_digits(n // 10) + n % 10
