from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dummy node gives us a fixed starting point
        # so we can return dummyNode.next at the end
        dummyNode = ListNode()
        # tail walks forward through the list as we build it.
        # dummyNode stays at the start
        tail = dummyNode

        # Once either list is exhausted, stop comparing
        while list1 and list2:
            # Pick the smaller value to append next, maintaining sorted order
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Advance tail to the node we just appended
            tail = tail.next

        # One list may have remaining nodes — append them all at once
        tail.next = list1 if list1 else list2

        # Return the real head of the merged list, skipping the dummy node
        return dummyNode.next
