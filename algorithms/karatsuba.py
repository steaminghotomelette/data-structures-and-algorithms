from utils.get_digits import get_digits

"""
Karatsuba's multiplication algorithm. 
Performs multiplication in O(n^log_2(3)) versus naive O(n^2).

Args:
    x: The first integer to multiply.
    y: The second integer to multiply.

Returns:
    The result of multiplication.
"""
def karatsuba(x: int, y: int) -> int:
    # Get digits of x and y
    x_digits = get_digits(x)
    y_digits = get_digits(y)

    # Base case: single-digit multiplication
    if x_digits == 1 or y_digits == 1:
        return x * y

    # Recursive case
    else:
        # Find the splitting point
        n = max(x_digits, y_digits) // 2

        # Obtain high and low portions of integers
        x1 = x // 10 ** n
        y1 = y // 10 ** n
        x2 = x % 10 ** n
        y2 = y % 10 ** n

        # Compute intermediate sums
        u = x1 + x2
        v = y1 + y2

        # Recurse
        a = karatsuba(x1, y1)
        b = karatsuba(x2, y2)
        c = karatsuba(u, v)

        # Calculate the result
        z = c - a - b
        return (a * 10 ** (2 * n)) + (z * 10 ** n) + b
