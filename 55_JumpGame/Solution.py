"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        r = 0
        for i in xrange(0, len(nums)):
            if i > r: break
            r = max(r, i+nums[i])
        return r >= len(nums)-1

    def canJump1(self, nums):
        p = nums[0]
        size = len(nums)-1
        while p <= size:
            print p, nums[p]
            if p == size: return True
            if nums[p] == 0: return False
            p += nums[p]
        return False

s = Solution()
print s.canJump([2, 3, 1, 1, 4])
print s.canJump([3, 2, 1, 0, 4])
print s.canJump([1, 0])
print s.canJump([1, 1, 1])
