class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome_linked_list(head):
    # Helper function to reverse a linked list
    def reverse_linked_list(node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Helper function to compare two linked lists
    def compare_linked_lists(list1, list2):
        while list1 and list2:
            if list1.value != list2.value:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    # Check if the linked list is empty or has only one friend
    if not head or not head.next:
        return True  # An empty or single-friend list is always a palindrome

    # Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    reversed_second_half = reverse_linked_list(slow)

    # Compare the first half with the reversed second half
    return compare_linked_lists(head, reversed_second_half)

# Example:
# Create a palindrome linked list: 1 -> 2 -> 3 -> 2 -> 1
palindrome_list = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

# Check if the linked list is a palindrome
result = is_palindrome_linked_list(palindrome_list)

print(result)  # Output: True