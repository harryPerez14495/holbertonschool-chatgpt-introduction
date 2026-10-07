#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function description:
        Calculate the factorial of a non-negative integer recursively.
        The base case is 0! = 1.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
