class Friend:
    def __init__(self, number=0, next_friend=None):
        self.number = number
        self.next = next_friend

def remove_middle_friend(start_friend):
    # Check if there are enough friends to remove from the middle
    if not start_friend or not start_friend.next or not start_friend.next.next:
        return None

    slow_friend = fast_friend = start_friend
    previous_friend = None

    # Move the fast pointer twice as quickly as the slow pointer to find the middle
    while fast_friend and fast_friend.next and fast_friend.next.next:
        previous_friend = slow_friend
        slow_friend = slow_friend.next
        fast_friend = fast_friend.next.next

    # Remove the middle friend by updating the next pointer of the previous friend
    if previous_friend:
        previous_friend.next = slow_friend.next
    else:
        start_friend = slow_friend.next

    return start_friend

# Example:
start_friend = Friend(1, Friend(2, Friend(3, Friend(4, Friend(5)))))

# Remove the middle friend
new_start_friend = remove_middle_friend(start_friend)

# Print the modified list
current_friend = new_start_friend
while current_friend:
    print(current_friend.number, end=" -> ")
    current_friend = current_friend.next
