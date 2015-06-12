class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        count = {}
        for x in nums:
            if count.has_key(x):
                count[x] += 1
            else:
                count[x] = 1
        for k, v in count.iteritems():
            if v == 1: return k
