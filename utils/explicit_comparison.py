from typing import Tuple

"""
Explicitly compares two strings from given starting indices.

Args:
    str1: The first string to compare.
    i: The starting index within the first string.
    str2: The second string to compare.
    j: The starting index within the second string.
    reverse: Boolean value specifying if the comparison is done left to right (default) or right to left.

Returns:
    A tuple of the format (boolean, int, int) specifying if a mismatch occurs,
    and the stop indices for both strings.

Raises:
    IndexError: When either starting index is greater than or equal to the length of its string, or less than 0.
"""
def explicit_comparison(str1: str, i: int, str2: str, j: int, reverse: bool = False) -> Tuple[bool, int, int]:
    # Error checks
    if i >= len(str1) or i < 0:
        raise IndexError(f"Starting index {i} is out of bounds for string '{str1}' of length {len(str1)}.")
    if j >= len(str2) or j < 0:
        raise IndexError(f"Starting index {j} is out of bounds for string '{str2}' of length {len(str2)}.")
    
    # Compare both strings
    if reverse:
        while i >= 0 and j >= 0:
            if str1[i] != str2[j]:
                return (True, i, j)  # Mismatch found
            i -= 1
            j -= 1
    else:
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                return (True, i, j)  # Mismatch found
            i += 1
            j += 1
    
    # No mismatch found
    return (False, i, j)
