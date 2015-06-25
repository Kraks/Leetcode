# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        res = []
        def aux(node):
            if node:
                if node.left: aux(node.left)
                if node.right: aux(node.right)
                res.append(node.val)
            return res
        return aux(root)

if __name__ == "__main__":
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)

    print Solution().postorderTraversal(t)
