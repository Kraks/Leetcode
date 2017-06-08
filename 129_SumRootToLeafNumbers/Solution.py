# Definition for a binary tree node.
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        def aux(node, res, path):
            if node:
                path.append(node.val)
                if node.left or node.right:
                    aux(node.left, res, copy.deepcopy(path))
                    aux(node.right, res, copy.deepcopy(path))
                else:
                    res.append(path)

        res = []
        aux(root, res, [])
        return sum(map(lambda x: int("".join(map(lambda y: str(y), x))), res))

    # Another Solution
    def sumNumbers1(self, root):
        def aux(node, preSum):
            if node == None: return 0
            preSum = preSum * 10 + node.val
            if node.left or node.right:
                return aux(node.left, preSum) + aux(node.right, preSum)
            return preSum

        return aux(root, 0)

s = Solution()
t = TreeNode(1)
#t.left = TreeNode(2)
#t.left.left = TreeNode(4)
#t.left.right = TreeNode(5)
t.right = TreeNode(0)

print s.sumNumbers1(t)
