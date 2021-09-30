# You can use sorting to solve a wide range of problems:

# Searching: Searching for an item on a list works much faster if the list is sorted.

# Selection: Selecting items from a list based on their relationship to the rest of the items is easier with sorted data. For example, finding the kth-largest or smallest value, or finding the median value of the list, is much easier when the values are in ascending or descending order.

# Duplicates: Finding duplicate values on a list can be done very quickly when the list is sorted.

# Distribution: Analyzing the frequency distribution of items on a list is very fast if the list is sorted. For example, finding the element that appears most or least often is relatively straightforward with a sorted list.




arr = [1,33,12,34,22,2,55,4,33,3,4,5]
temp = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        print(arr[j], arr[i], temp)
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)