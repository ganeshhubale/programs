# Implement an algorithm to reverse a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        current = self.head
        prev = None
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev

l_obj = linkedList()

l_obj.append(1)
l_obj.append(2)
l_obj.append(3)
l_obj.append(4)
l_obj.append(5)

l_obj.printList()
l_obj.reverse()
l_obj.printList()

# Time complexity - O(n)
# Space complexity - O(1)