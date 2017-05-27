class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        global_max, local = None, None
        for x in nums:
            if local == None: local = 0
            local = max(x, local + x)
            global_max = max(local, global_max)
            print "local ", local, " global ", global_max
        return global_max

s = Solution()
print s.maxSubArray([-1])
print s.maxSubArray([5, -4, -2, 1, 3, 2])
