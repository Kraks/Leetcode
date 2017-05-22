# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addAux(l1, l2, 0)

    def addAux(self, l1, l2, carry):
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        sum = n1 + n2 + carry
        res = ListNode(sum % 10)
        carry = 1 if sum > 9 else 0
        x1 = l1.next if l1 else None
        x2 = l2.next if l2 else None
        if x1 or x2 or carry:
            res.next = self.addAux(x1, x2, carry)
        return res

def printList(l):
    if l:
        print l.val,
        print "->",
        printList(l.next)
    else:
        print "\n"

if __name__ == "__main__":
    S = Solution()
    n1 = ListNode(2)
    n2 = ListNode(5)
    n3 = S.addTwoNumbers(n1, n2)
    printList(n3)

    n2.next = n3
    n4 = S.addTwoNumbers(n1, n2)
    printList(n4)

    n1 = ListNode(5)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)
    n4.next = n5
    n5.next = n6

    n7 = S.addTwoNumbers(n1, n4)
    printList(n7)

    five = ListNode(5)
    ten = S.addTwoNumbers(five, five)
    printList(ten)

    z = ListNode(0)
    printList(S.addTwoNumbers(z, z))
