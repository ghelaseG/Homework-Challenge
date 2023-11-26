## Pseudocde

# Write a function to reverse the nodes of a linked list

# Use three pointers: current, prev, and next_node.

    def reverse(head):
        if head == None:
            return head
        current = head
        prev = None
        next_node = None
        while current!= None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        return head

# Traverse through each node:
# 1) Store the next pointer in temp variable.
# 2) Change the link of the current node to point to previous node (prev).
# 3) Move both the prev and curr one step forward.


    ## Pseudocode
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
            def reverseLinkedList(head):
                if head == None:
                    return head
                current = head
                prev = None
                next_node = None
                while current!= None:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                head = prev
                return head
            self.reverseLinkedList = reverseLinkedList

# Update the head to the last node.
# Account for scenarios with no list or only one node.
# Furnish the head of the reversed linked list.
