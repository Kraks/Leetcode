class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

s = Solution()
xs = [1, 1, 1, 1, 2]
xs = [1, 2, 3, 4, 1, 2, 1]
print s.removeElement(xs, 1)
print xs
