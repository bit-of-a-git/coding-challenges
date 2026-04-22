from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialise a set to keep track of nodes previously seen
        nodesSeen = set()
        while head:
            # If we've seen it already, there's a cycle
            if head in nodesSeen:
                return True
            else:
                # Otherwise just add it
                nodesSeen.add(head)
            # Move forward to the next node
            head = head.next
        # If head = None, we have gone through the linked list and there is no cycle
        return False
