def find_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

"""
This algorithm has a time complexity of O(n), where n is the number of nodes in the linked list. The space complexity is O(1) since it only uses two pointers to keep track of the current position.
"""
