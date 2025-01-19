# Find Peak Element

# A peak element in an array is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element 
# and return its index. If the array contains multiple peaks, return the index of any one of the peaks.

# Use binary search
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left+right) // 2
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    
    return left

nums = [1, 2, 1, 3, 5, 6, 4]
print("Index of peak - ", find_peak_element(nums))

# Time complexity: O(log n)
# Space complexity: O(1)

# By Linear search
def find_peak_linear_Search(nums):
    for i in range(len(nums)):
        if (i==0 or nums[i] > nums[i-1]) and (i==len(nums) - 1 or nums[i] > nums[i+1]):
            return f"\nElement {nums[i]} is peak at index {i}"

nums = [40]
print(find_peak_linear_Search(nums))

# Time complexity: O(n)
# Space complexity: O(1)