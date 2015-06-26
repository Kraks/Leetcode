# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root: return []

        q, res = [(root, 0)], []
        current_res, current_level = [], 0

        while len(q) > 0:
            node, level = q.pop(0)
            if level > current_level:
                res.insert(0, current_res)
                current_res = []
            current_res.append(node.val)
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
            current_level = level

        res.insert(0, current_res)
        return res

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    print Solution().levelOrderBottom(t)
