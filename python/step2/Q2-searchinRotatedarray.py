# Search in Rotated Sorted Array

# - Check if left or right part of the array is sorted
# - Check if target is in left or right part
# - Use binary search to find out the target is available or not

def search_rotated_sorted_array(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right-left) // 2

        if nums[mid] == target:
            return f"Element {target} found at index {mid}"
        
        # check which side is sorted
        if nums[left] <= nums[mid]: # left part sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # right part sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else: 
                right = mid - 1
    return -1


nums = [1, 3]
print(search_rotated_sorted_array(nums, target=3))

# Time complexity: O(log n)
# Space complexity: O(1)