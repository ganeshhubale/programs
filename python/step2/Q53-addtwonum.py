# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each node contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zeros, except for the number 0 itself.

# input
# l1 = [2 -> 4 -> 3]
# l2 = [5 -> 6 -> 4]

# output: [7 -> 0 -> 8]

# Iterative Solution Using Two Pointers

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def twoSum(l1, l2):

    dummy_head = Node(0)  # Dummy node to simplify result construction
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        sum_value = carry  # Start with carry from previous operation
        
        if l1:
            sum_value += l1.val
            l1 = l1.next
        
        if l2:
            sum_value += l2.val
            l2 = l2.next
        
        carry = sum_value // 10  # Compute new carry
        current.next = Node(sum_value % 10)  # Create new node with the digit
        current = current.next  # Move current pointer

    return dummy_head.next  # Return result (excluding dummy head)

# def list_to_linked_list(lst):
#     dummy = ListNode()
#     current = dummy
#     for num in lst:
#         current.next = ListNode(num)
#         current = current.next
#     return dummy.next

def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))

node1 = Node(2, Node(4, Node(3))) # 243 > 342
node2 = Node(5, Node(6, Node(4, Node(4)))) # 564 > 465

# 807 > 7084
print_linked_list(twoSum(node1, node2))

# Time Complexity	: O(max(N, M))
# Space Complexity : O(max(N, M))
# N = length of l1, M = length of l2.
# O(max(N, M)) because we process each node once.
# Space complexity is also O(max(N, M)) since we create a new list
