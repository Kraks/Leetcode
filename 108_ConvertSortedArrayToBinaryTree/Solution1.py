# Just Another Solution, much more fast

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Auxiliary class just for test
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

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.path = []

        next_node = self.root
        while next_node:
            self.path.append(next_node)
            next_node = next_node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.path) != 0

    # @return an integer, the next smallest number
    def next(self):
        res = self.path.pop()
        if res.right:
            succ = res.right
            while succ:
                self.path.append(succ)
                succ = succ.left
        return res.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    t = BST().sortedArrayToBST(range(1, 9))
    s = BSTIterator(t)
    while s.hasNext():
        print s.next()
