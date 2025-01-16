# Find Minimum in Rotated Sorted Array
# Given a rotated sorted array nums (with no duplicate elements), find the minimum element in the array.


def find_min_in_rotated_array(nums):
    left =0
    right = len(nums) -1

    while left < right:
        mid = left + (right-left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[right]

nums = [4, 5, 6, 7, 8, -1, 0, 1, 2]
print(find_min_in_rotated_array(nums))

# Time complexity: O(logn)
# Space complexity: O(1)