# 1. Find the missing number in an array of integers.

arr = [3, 1, 5, 4]
def findMissingNumber(arr):

    n = len(arr)

    expected_sum = (n+1)*(n+2) // 2
    actual_sum = 0
    for num in arr:
        actual_sum = actual_sum + num
    return expected_sum - actual_sum

print("Missing number: ", findMissingNumber(arr))

# Time complexity - O(n)
# Space complexity - O(1)