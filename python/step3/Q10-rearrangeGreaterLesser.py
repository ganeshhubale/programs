# Rearrange array such that elements greater are towards right and smaller toward left
#     - Given an unsorted array, rearrange it so that all elements greater than or equal to 
# a given pivot are on the right, and all smaller elements are on the left.

# Input:  arr = [3, 8, 5, 2, 7, 6, 1], pivot = 5
# Output: [3, 2, 1, 5, 8, 7, 6]  (Order of elements may vary)


def rearrange_array(arr, pivot):
    low, high = 0, len(arr) - 1

    while low <= high:
        if arr[low] < pivot:  # Correctly placed, move forward
            low += 1
        elif arr[high] >= pivot:  # Correctly placed, move backward
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]  # Swap
            low += 1
            high -= 1

    return arr

# Example Usage
arr = [3, 8, 5, 2, 7, 6, 1]
pivot = 5
result = rearrange_array(arr, pivot)
print("Rearranged Array:", result)

# Time Complexity: O(n) (Each element is traversed once)
# Space Complexity: O(1) (In-place rearrangement, no extra space used)
