# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = ListNode(None)
        c1, c2 = l1, l2

        current = head
        while c1 and c2:
            if c1.val > c2.val:
                current.next = c2
                c2 = c2.next
            else:
                current.next = c1
                c1 = c1.next
            current = current.next
        if not c1: current.next = c2
        if not c2: current.next = c1

        return head.next
