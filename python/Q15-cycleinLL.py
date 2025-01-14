# Detect a cycle in a linked list.
# Floyd's Cycle Detection Algorithm

class Node:
    def __init__(self, data=0, next=None):
        self.data = data 
        self.next = next

def hasCycle(head):

    if not head or not head.next:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True
    return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# create cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

# check cycle
print("Cycle in LL -> ", hasCycle(node1))

# without cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

# check if cycle exist
print("Cycle in LL without cycle-> ", hasCycle(node1))

# Time complexity - O(N)
# Space complexity - O(1)


