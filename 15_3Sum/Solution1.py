def search(key, nums):
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = lo + (hi - lo)/2
        if key < nums[mid]: hi = mid-1
        elif key > nums[mid]: lo = mid+1
        else: return mid
    return -1

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        res = []
        record = {}
        nums.sort()
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                p = search(-x-y, nums)
                t = (x, y, nums[p])
                if p > j+i+1 and not record.has_key(t):
                    res.append(t)
                    record[t] = 1
        return res

s = Solution()
print s.threeSum([1, 2, 3, 4, 5, 0, -1, -2, -3])
print s.threeSum([0, 2, 2, 2, -2, -2, -2])
