class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        for i, x in enumerate(nums):
            if x >= target: return i
        return len(nums)
