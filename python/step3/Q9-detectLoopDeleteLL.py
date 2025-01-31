# Detect loop in singly linked list and delete it
#     - Given a singly linked list, detect if a loop exists in the list. 
# If a loop is found, remove the loop to restore the linked list structure.

# Step 1: Detect the Loop (Floyd’s Cycle Detection Algorithm)
# Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare Algorithm):
# Use two pointers: slow and fast.
# Move slow one step at a time and fast two steps at a time.
# If slow and fast meet, a loop exists.
# If fast reaches None, there is no loop.
# Step 2: Remove the Loop
# After detecting the loop:
# Move slow to the head.
# Move both slow and fast one step at a time until slow.next == fast.next.
# Set fast.next = None to remove the loop.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_and_remove_loop(head):
    slow = head
    fast = head

    # Step 1: Detect Loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Loop detected
            remove_loop(head, slow)
            return True  # Loop found and removed

    return False  # No loop found

def remove_loop(head, loop_node):
    ptr1 = head
    ptr2 = loop_node

    # Find the start of the loop
    while ptr1.next != ptr2.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    # Remove loop
    ptr2.next = None

# --- Helper Functions ---
def create_linked_list_with_loop(values, loop_index):
    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        node = ListNode(val)
        nodes.append(node)
        current.next = node
        current = node

    if loop_index != -1:  # Creating a loop
        current.next = nodes[loop_index]

    return head

def print_linked_list(head):
    visited = set()
    while head:
        if head in visited:  # To prevent infinite loops in output
            print("... (loop detected)")
            break
        print(head.value, end=" -> ")
        visited.add(head)
        head = head.next
    print("None")

# --- Test the Function ---
head = create_linked_list_with_loop([1, 2, 3, 4, 5, 6], 2)  # Creates a loop at node index 2
print("Before removing loop:")
print_linked_list(head)

if detect_and_remove_loop(head):
    print("\nLoop detected and removed.")
else:
    print("\nNo loop detected.")

print("\nAfter removing loop:")
print_linked_list(head)
