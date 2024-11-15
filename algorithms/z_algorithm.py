from typing import List
from utils.explicit_comparison import explicit_comparison

"""
Gusfield's Z-algorithm.
Computes the Z-array for a given string, 
i.e., an array where z_arr[i] is the length of the longest substring starting at index i that matches the string's prefix.

Args:
    txt: The input string to process.

Returns:
    The corresponding Z-array of the string.

Raises:
    ValueError: When the input string is empty.
"""
def z_algorithm(txt: str) -> List[int]:
    # Error check
    if len(txt) == 0:
        raise ValueError("Invalid input string of length 0 detected.")
    
    # Prepare Z-array; the first element is always the length of the string itself
    z_arr = [None] * len(txt)
    z_arr[0] = len(txt)

    # Prepare right and left Z-box pointers
    r = 0
    l = 0

    # Iterate over the input string
    for i in range(1, len(txt)):

        # We are in a Z-box
        if i <= r:

            # Subcase 1: Z-value is entirely within the current Z-box
            if z_arr[i - l] < r - i + 1:
                z_arr[i] = z_arr[i - l]

            # Subcase 2: Z-value reaches the right boundary of the Z-box
            elif z_arr[i - l] == r - i + 1:
                _, _, k = explicit_comparison(txt, r - i + 1, txt, r + 1)
                z_arr[i] = k - i
                r = k - 1
                l = i

            # Subcase 3: Z-value extends beyond the right boundary of the Z-box
            else:
                z_arr[i] = r - i + 1

        # We are not in a Z-box
        else:
            # Begin comparison between the prefix and substring starting at index i
            _, _, k = explicit_comparison(txt, 0, txt, i)
            z_arr[i] = k - i

            if k - i > 0:
                r = k - 1
                l = i

    return z_arr
