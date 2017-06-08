# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeFold(f, e, n):
    if n:
        return f(n.val, treeFold(f, e, n.left), treeFold(f, e, n.right))
    return e

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        def aux(v, l, r):
            if l == 0: return r + 1
            if r == 0: return l + 1
            return min(l, r) + 1
        return treeFold(aux, 0, root)

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.right.left = TreeNode(4)

    s = Solution()
    print s.minDepth(t)
