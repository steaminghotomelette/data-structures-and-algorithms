from math import log10

"""
Gets the number of digits in a decimal integer.

Args:
    n: The input integer.

Returns:
    The number of digits in n.
"""
def get_digits(n: int) -> int:
    if n > 0:
        return int(log10(n)) + 1
    elif n == 0:
        return 1
    else:
        return int(log10(-n)) + 1
