#. Find the kth smallest/largest element in an array.

import random

def quickselect_largest(arr, k):
    """
    Find the kth largest element using the Quickselect algorithm.
    :param arr: List of integers
    :param k: Position (1-based)
    :return: kth largest element
    """
    # Convert kth largest to (n-k+1)th smallest
    n = len(arr)
    return quickselect(arr, n - k + 1)  # Reuse the kth smallest function

def quickselect(arr, k):
    """
    Find the kth smallest element using the Quickselect algorithm.
    :param arr: List of integers
    :param k: Position (1-based)
    :return: kth smallest element
    """
    if len(arr) == 1:  # Base case: single element
        return arr[0]

    pivot = random.choice(arr)  # Randomly choose a pivot
    lows = [x for x in arr if x < pivot]  # Elements smaller than pivot
    highs = [x for x in arr if x > pivot]  # Elements larger than pivot
    pivots = [x for x in arr if x == pivot]  # Elements equal to pivot

    if k <= len(lows):
        return quickselect(lows, k)  # Search in the "lows"
    elif k > len(lows) + len(pivots):
        return quickselect(highs, k - len(lows) - len(pivots))  # Search in the "highs"
    else:
        return pivots[0]  # Pivot is the kth element

# Example usage
arr = [7, 10, 4, 3, 20, 15]
print("3rd Largest:", quickselect_largest(arr, 3))  # Output: 10

arr = [7, 10, 4, 3, 20, 15]
print("3rd smallest:", quickselect(arr, 3))  # Output: 7


arr = [7, 7,7,7,7,7,7,543,23,3534,]
print("3rd Largest:", quickselect_largest(arr, 3))  # Output: 7

arr = [5,5,5,5,5,5,5,5,5,5, 1,2,2,455]
print("3rd smallest:", quickselect(arr, 3))  # Output: 7
# Time complexity - O(n)
# Space complexity - O(logN)

# With sorting approach
def kth_smallest(arr, k):
    """
    Find the kth smallest element in the array using sorting.
    :param arr: List of integers
    :param k: Position (1-based index)
    :return: kth smallest element
    """
    arr.sort()  # Sort the array in ascending order
    return arr[k - 1]  # Return the (k-1)-th index for 1-based indexing


def kth_largest(arr, k):
    """
    Find the kth largest element in the array using sorting.
    :param arr: List of integers
    :param k: Position (1-based index)
    :return: kth largest element
    """
    arr.sort(reverse=True)  # Sort the array in descending order
    return arr[k - 1]  # Return the (k-1)-th index for 1-based indexing


# Example Usage
arr = [7, 10, 4, 3, 20, 15]

# Find kth smallest
k_smallest = 3
print(f"{k_smallest}rd smallest element:", kth_smallest(arr, k_smallest))  # Output: 7

# Find kth largest
k_largest = 3
print(f"{k_largest}rd largest element:", kth_largest(arr, k_largest))  # Output: 10


# Time complexity - O (n log n)
# Space complexity - O(1)