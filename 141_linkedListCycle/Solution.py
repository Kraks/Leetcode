# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head): #WORK
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast == None:
                return False
            slow = slow.next
            if id(slow) == id(fast):
                return True
        return False

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    c.next = a
