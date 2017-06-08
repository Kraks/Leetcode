class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        k = len(nums) - (k % len(nums)) -1
        t = nums[:k+1]
        for i in range(k+1, len(nums)):
            nums[i-k-1] = nums[i]
        for i in range(len(nums)-k-1, len(nums)):
            nums[i] = t[i-len(nums)+k+1]

s = Solution()
xs = range(1, 2)
xs = range(1, 8)
xs = [-1]
s.rotate(xs, 2)
print xs
