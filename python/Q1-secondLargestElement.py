# 𝗔𝗿𝗿𝗮𝘆 𝗠𝗮𝗻𝗶𝗽𝘂𝗹𝗮𝘁𝗶𝗼𝗻 𝗮𝗻𝗱 𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴
# Q1: Write a python method to find the second largest element in an array.

# MY SOLUTION
def secondLargestElement(arr):
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[1]
    

arr = [1,2,3,4,5,44,33,22,66,33,44, 45]
print(secondLargestElement(arr))

# Time complexity - O(n^2)
# Space complexity - O(1) 
# Input space: The input array arr is modified in place, so no additional space is used for a copy of the array.
# Auxiliary space: The function does not use any additional data structures or recursion.

# CHATGPT SOLUTION
def secondLargestElementGPT(arr):

    if len(arr) < 2:
        return None
    
    if arr[0] > arr[1]:
        largest, secondLargest = arr[0], arr[1]
    else:
        largest, secondLargest = arr[1], arr[0]
    
    for num in arr[2:]:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num!=largest:
            secondLargest = num
    return secondLargest

arr = [-10, -20, -5, -8, -15]
print(secondLargestElementGPT(arr))