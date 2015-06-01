class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        res = []
        i = 0
        n = len(nums)
        old = None
        while i < n:
            j = i + 1
            k = n - 1
            s = -nums[i]
            while j < k:
                if nums[j] + nums[k] < s: j += 1
                elif nums[j] + nums[k] > s: k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    old = nums[j]
                    j += 1
                    while nums[j] == old and j < k: j += 1
                    k -= 1
            old = nums[i]
            i += 1
            while i < n and nums[i] == old: i += 1
        return res

s = Solution()
print s.threeSum([1, 2, 3, 4, 5, 0, -1, -2, -3])
print s.threeSum([0, 2, 2, 2, -2, -2, -2])
