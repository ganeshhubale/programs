# Rotate array
# Given an array nums and an integer k, rotate the array to the right by k steps.


def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k > n

    # Helper function to reverse a subarray
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)

    return nums
# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
print(rotate(nums, 3)) # Output: [5, 6, 7, 1, 2, 3, 4]

# Time complexity: O(n)
# Space complexity: O(1)
