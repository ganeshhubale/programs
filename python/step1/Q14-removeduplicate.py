#8. Write a program to remove duplicates from a sorted array.

arr = [1,1,2,2,2,2,3,3,4,5,6]

def removeDuplicates(arr):

    # Compare prev element with next
    # if prev == next then continue
    # if prev != next  then put next element next to prev element
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    print("Unique elements count -> ", j+1)
    print("Array after removing dupicates -> ", arr[:j+1])

removeDuplicates(arr)

# Time complexity - O(n)
# Space complexity - o(1)