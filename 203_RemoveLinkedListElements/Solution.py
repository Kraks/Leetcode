# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, target):
        start = ListNode(0)
        start.next = head
        curr = start

        while curr.next:
            if curr.next.val == target:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return start.next
        
if __name__ == "__main__":
    def generateList(start, end):
        beg = ListNode(start)
        prev = beg
        for i in range(start+1, end+1):
            node = ListNode(i)
            prev.next = node
            prev = node
        return beg

    def printList(head):
        s = ""
        if head:
            s += str(head.val)
            while head.next:
                s += "->"
                s += str(head.next.val)
                head = head.next
        print s

    s = Solution()
    xs = generateList(1, 10)
    printList(xs)
    ys = s.removeElements(xs, 1)
    printList(ys)
