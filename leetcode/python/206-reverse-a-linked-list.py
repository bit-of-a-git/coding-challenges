from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # When starting off, the previous node should be none
        prev = None

        while head:
            # We save what next pointed to before we modify it
            next = head.next
            # Update next to prev
            head.next = prev
            # Set prev to head
            prev = head
            # And move head to next
            head = next

        # We return prev, which should be the last item of head
        return prev
