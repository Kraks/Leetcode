class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        candidate = nums[0]
        for x, y in zip(nums, nums[1:]):
            if y < x: return y
        return candidate

s = Solution()
print s.findMin([4, 5, 6, 7, 0, 1, 2])
print s.findMin([1])
print s.findMin([1, 2])
print s.findMin([3, 1, 2])

