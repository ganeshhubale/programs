# Merge Two Sorted Lists

# You are given the heads of two sorted linked lists, list1 and list2. Merge the two lists into a 
# single sorted linked list and return the head of the merged list. 
# The merged list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def mergedList(list1, list2):
    if not list1.data:
        return list2
    if not list2.data:
        return list1
    
    # create dummy node
    dummy = ListNode()

    current = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If any list  remains, append it to the merged list
    current.next = list1 if list1 else list2

    return dummy.next


def printMerge(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

mergeListObj = mergedList(list1, list2)
printMerge(mergeListObj)

# Input: list1 = None, list2 = None
list1 = ListNode()
list2 = ListNode()

mergeListObj = mergedList(list1, list2)
printMerge(mergeListObj)

# Input: list1 = None, list2 = 0
list1 = ListNode()
list2 = ListNode(0)

mergeListObj = mergedList(list1, list2)
printMerge(mergeListObj)


# Time complexity: O(n+m)
# Space complexity: O(1)