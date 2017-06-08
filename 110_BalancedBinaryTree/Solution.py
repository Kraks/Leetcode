# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeFold(f, e, node):
    if node:
        return f(node.val, treeFold(f, e, node.left), treeFold(f, e, node.right))
    return e

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        def aux(v, c1, c2):
            res.append(abs(c1-c2)<=1)
            return max(c1, c2) + 1

        res = []
        treeFold(aux, 0, root)
        return reduce(lambda x, y: x and y, res, True)

# for testing
class BST:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self.aux(nums, 0, len(nums)-1)

    def aux(self, nums, left, right):
        if left > right: return None
        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = self.aux(nums, left, mid-1)
        node.right = self.aux(nums, mid+1, right)
        return node

if __name__ == "__main__":
    t = BST().sortedArrayToBST(range(1, 9))
    s = Solution()
    print s.isBalanced(t)
    print s.isBalanced(None)

    t2 = TreeNode(1)
    t2.right = TreeNode(2)
    t2.right.right = TreeNode(3)
    print s.isBalanced(t2)

    t3 = TreeNode(2)
    t3.left = TreeNode(1)
    t3.right = TreeNode(3)
    print s.isBalanced(t3)
