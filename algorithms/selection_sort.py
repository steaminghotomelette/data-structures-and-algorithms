from typing import List, TypeVar
from utils.swap import swap

# Generic type
T = TypeVar('T')

"""
Uses selection sort to sort an array of elements.
Generally not a very efficient sorting algorithm but has the advantage of using the minimum number of writes.
Unstable, but in-place.

Args:
    arr: The array to sort.

Returns:
    None, the sort is performed in place.
"""
def selection_sort(arr: List[T]) -> None:
    # Loop over the elements
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap with the minimum
        swap(arr, i, arr, min_idx)
