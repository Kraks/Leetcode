# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        current = head
        while current:
            t = current.next
            while t and t.val == current.val: t = t.next
            current.next = t
            current = current.next
        return head

a = ListNode(1)
b = ListNode(1)
a.next = b

s = Solution()
s.deleteDuplicates(a)
