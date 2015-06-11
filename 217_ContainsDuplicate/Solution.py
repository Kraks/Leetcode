import itertools

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicateWouldExceedMemoryLimit(self, nums):
        pmt = [x for x in itertools.permutations(nums, 2)]
        for (x, y) in pmt:
            if x == y: return True
        return False

    def containsDuplicateWouldExceedTimeLimit(self, nums):
        for index, x in enumerate(nums):
            for y in nums[index+1:]:
                if x == y: return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.containsDuplicate([1, 2, 3])
    print s.containsDuplicate([1, 2, 3, 4, 1])
