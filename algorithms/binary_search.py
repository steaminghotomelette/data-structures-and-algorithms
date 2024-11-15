from typing import List, Optional, TypeVar

# Generic type
T = TypeVar('T')

"""
Performs a binary search to find the index of a target element in a sorted array.

Args:
    arr: The input sorted array.
    target: The element to search for.

Returns:
    The index of the target within the array, or None if the target does not exist.
"""
def binary_search(arr: List[T], target: T) -> Optional[int]:
    # Initialize search space with low and high pointers
    low = 0
    high = len(arr)

    # Perform the binary search
    while low < high - 1:
        mid = (low + high) // 2
        if target >= arr[mid]:
            low = mid
        else:
            high = mid

    # Verify if the target is found at arr[low]
    if arr[low] == target:
        return low
    else:
        return None
