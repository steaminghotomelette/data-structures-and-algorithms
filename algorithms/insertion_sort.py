from typing import List, TypeVar
from utils.swap import swap

# Generic type
T = TypeVar('T')

"""
Uses insertion sort to sort an array of elements.
A reasonably efficient sorting algorithm with the benefit of being online,
stable, and in-place.

Args:
    arr: The array to sort.

Returns:
    None, the sort is performed in place.
"""
def insertion_sort(arr: List[T]) -> None:
    # Iterate over the elements
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
