def fibonacci(n):
    """
    this function is meant to do a fibonacci sequence which starts fron 0 then 1 as a base cases
    and then the next number will be the sum of the privious 2 numbers

    it will return the nth number in the sequence
    [0,1,1,2,3,5,...]
    """
    # base case
    if n <= 1:
        return n
    # general case
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    """
    this function is meant to do a lucas sequence which starts fron 2 then 1 as a base cases
    and then the next number will be the sum of the privious 2 numbers

    it will return the nth number in the sequence
    [2, 1, 3, 4, 7, 11, ....]
    """
    # base cases
    if n == 0:
        return 2
    elif n == 1:
        return 1
    # general case
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(n, first=0, second=1):
    """
    return a sum sequence which is the first two values are 0 and 1 by 
    defualt and the next value will be the sum of privious two values
    """

    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1,first,second)+sum_series(n-2,first,second)
