from typing import List, TypeVar

# Generic type
T = TypeVar('T')

"""
Swaps two elements from the same or separate lists.

Args:
    arr1: The first list.
    i: The index of the element to swap in the first list.
    arr2: The second list.
    j: The index of the element to swap in the second list.

Returns:
    Nothing, mutates the lists in place.

Raises:
    IndexError: When either index is greater than or equal to the length of its list, or less than 0.
"""
def swap(arr1: List[T], i: int, arr2: List[T], j: int) -> None:
    # Error checks
    if i >= len(arr1) or i < 0:
        raise IndexError(f"Index {i} is out of bounds for list '{arr1}' of length {len(arr1)}.")
    if j >= len(arr2) or j < 0:
        raise IndexError(f"Index {j} is out of bounds for list '{arr2}' of length {len(arr2)}.")
    
    # Swap the items
    temp = arr1[i]
    arr1[i] = arr2[j]
    arr2[j] = temp
