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

    def singleNumber1(self, nums):
        one, two, three = 0, 0, 0
        for i in range(0, len(nums)):
            two |= one & nums[i]
            one ^= nums[i]
            three = one & two
            one &= ~three
            two &= ~three
        return one

s = Solution()
print s.singleNumber1([1, 2, 3, 1, 2, 3, 4, 1, 2, 3])
