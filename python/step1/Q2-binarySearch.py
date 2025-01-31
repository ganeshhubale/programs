# Q2: Given a sorted array, write a method to perform binary search on the array.

arr = [1,2,3,4,5,6,7,8,9, 55]

def binarySearch(arr, ele):

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            return f"Element {ele} found at index {mid}"
        elif arr[mid] < ele:
            start = mid + 1
        elif arr[mid] > ele:
            end = mid - 1
    return f"Element {ele} not found."

print(binarySearch(arr, 1))

# Time complexity
# best case  - O(1)
# worst case - The element is not in the array, or it is found after all divisions are performed. Time complexity = O(log₂(n)).
# Overall time complexity - O(log n)
# Space complexity - O(1)