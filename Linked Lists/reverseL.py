# Definition of a node in a linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to reverse a linked list
def reverse_linked_list(head):
# Initialize two pointers: prev (previous) and current
    prev, current = None, head

# Traverse the linked list
    while current:
# Swap the next pointer of the current node to point to the previous node
        current.next, prev, current = prev, current, current.next

# The head of the reversed list is the last node
    return prev

# Example Usage:
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print the reversed linked list
current = reversed_head
while current:
    print(current.value, end=" -> ")
    current = current.next