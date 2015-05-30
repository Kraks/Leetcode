class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums, 0)

xs = [1, 2, 3, 4, 1, 2, 4]
print Solution().singleNumber(xs)
