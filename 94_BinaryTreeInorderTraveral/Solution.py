#Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        if not root: return self.res
        if root.left:
            self.inorderTraversal(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.res

