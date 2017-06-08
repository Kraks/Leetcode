# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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

# Test

q = []
def inOrder(root):
    if root:
        inOrder(root.left)
        q.append(root.val)
        inOrder(root.right)
    return q

s = Solution()
t = s.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8])
r = inOrder(t)
print r
