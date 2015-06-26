# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, target):
        def aux(node, sum, allSums):
            if node:
                sum += node.val
                if node.left or node.right:
                    aux(node.left, sum, allSums)
                    aux(node.right, sum, allSums)
                else:
                    allSums.append(sum)

        allSums = []
        aux(root, 0, allSums)
        print allSums
        return len(filter(lambda x: x == target, allSums)) > 0

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.left.left = TreeNode(5)
    t.left.left.right = TreeNode(6)

    t1 = TreeNode(0)
    t1.left = TreeNode(1)
    t1.right = TreeNode(1)

    s = Solution()
    print s.hasPathSum(t1, 1)
