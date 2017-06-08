# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root: return self.aux(root.left, root.right)
        return True

    def aux(self, left, right):
        if left == None and right == None: return True
        if left == None  or right == None: return False

        return left.val == right.val and self.aux(left.left, right.right) \
                and self.aux(left.right, right.left)

if __name__ == "__main__":
    s = Solution()

    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(3)
    t.right.left = TreeNode(2)

    print s.isSymmetric(t)
