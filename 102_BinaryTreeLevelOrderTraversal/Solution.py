# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def sortedArrayToBST(self, nums):
        return self.aux(nums, 0, len(nums)-1)

    def aux(self, nums, left, right):
        if left > right: return None
        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = self.aux(nums, left, mid-1)
        node.right = self.aux(nums, mid+1, right)
        return node

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root: return []

        q, res = [(root, 0)], []
        current_res, current_level = [], 0

        while len(q) > 0:
            node, level = q.pop(0)
            if level > current_level:
                res.append(current_res)
                current_res = []
            current_res.append(node.val)
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
            current_level = level
            
        res.append(current_res)
        return res

if __name__ == "__main__":
    s = Solution()
    t = BST().sortedArrayToBST(range(1, 9))
    print s.levelOrder(t)
    print s.levelOrder(None)
