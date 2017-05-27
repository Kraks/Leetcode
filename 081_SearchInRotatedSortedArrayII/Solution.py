class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        p = len(nums)-1
        for i in xrange(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                p = i
                break

        lo = 0; hi = len(nums)-1
        if p == hi: pass
        elif target <= nums[p] and target >= nums[lo]:
            hi = p
        elif target >= nums[p+1] and target <= nums[hi]:
            lo = p+1

        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if target < nums[mid]: hi = mid-1
            elif target > nums[mid]: lo = mid+1
            else: return mid
        return -1

s = Solution()
print s.search([4, 5, 6, 7, 0, 1, 2], 0)
print s.search([1], 1)
print s.search([1], 0)
print s.search([1, 2, 3, 4, 5], 3)
