# Find the intersection point of two linked lists.

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def intersectionPoint(nodeA, nodeB):

    if not nodeA or not nodeB:
        return None
    
    ptrA = nodeA
    ptrB = nodeB

    while ptrA != ptrB:
        if ptrA: 
            ptrA = ptrA.next
        else:
            ptrA = nodeB
        
        if ptrB:
            ptrB = ptrB.next
        else:
            ptrB = nodeA
    return ptrA

# with interesection
# 1 -> 2 -> 3 \
#              -> 6 -> 7
#      4 -> 5 /

sharedNode = Node(6, Node(7))

nodeA = Node(1, Node(2, Node(3, sharedNode)))
nodeB = Node(4, Node(5, sharedNode))

# Check intersection
intersect = intersectionPoint(nodeA, nodeB)
if intersect:
    print("Intersection of 2 LL -> ", intersect.data)
else:
    print("No intersection")

# without intersection
# List A = 1 -> 2 -> 3
# List B = 4 -> 5 -> 6
nodeA = Node(1, Node(2, Node(3)))
nodeB = Node(4, Node(5, Node(6)))
# Check intersection
intersect = intersectionPoint(nodeA, nodeB)
if intersect:
    print("Intersection of 2 LL -> ", intersect.data)
else:
    print("No intersection")