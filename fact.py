

def fact(n):
    '''
    >>> fact(1)
    1

    >>> fact(0)
    Traceback (most recent call last):
    ...
    ValueError

    >>> fact('abc')
    Traceback (most recent call last):
    ...
    TypeError: unorderable types: str() < int()
    
    >>> fact(2)
    2
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__=='__main__':
    import doctest
    doctest.testmod()