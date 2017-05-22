class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # num -> index
        d = dict()
        res = []
        for i, n in enumerate(nums):
            if d.has_key(target-n):
                res.append(d[target-n])
                res.append(i)
                return res
            d[n] = i
        return [-1,-1]

if __name__ == "__main__":
    S = Solution()
    print(S.twoSum([2,7,11,15], 18))

