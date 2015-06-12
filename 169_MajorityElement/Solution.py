class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = {}
        for x in nums:
            if count.has_key(x):
                count[x] += 1
            else:
                count[x] = 1
        for k, v in count.iteritems():
            if v > len(nums) / 2: return k

    def majorityElement1(self, nums):
        # Moore's voting algorithms
        candidate, count = None, 0
        for x in nums:
            if count == 0:
                candidate, count = x, 1
            elif x == candidate:
                count += 1
            else:
                count -= 1
        return candidate
