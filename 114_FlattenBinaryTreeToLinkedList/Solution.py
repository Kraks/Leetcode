# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        while root:
            if root.left:
                x = root.left
                while x.right:
                    x = x.right
                x.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    s.flatten(root)
