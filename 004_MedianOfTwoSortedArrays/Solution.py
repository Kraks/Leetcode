def isEven(x): return x % 2 == 0

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        i, j, p = 0, 0, 0
        size = len(nums1) + len(nums2)
        mid = size / 2
        res = []
        while p < size:
            if i >= len(nums1):
                res.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                res.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
            p += 1
            if p == mid + 1:
                if isEven(size): 
                    return sum(res[len(res)-2:len(res)])/2.0
                else:
                    return res[-1]

if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([1, 2, 3, 7], [4, 5, 6])
    print s.findMedianSortedArrays([8, 9, 10], [2, 4, 6])
    print s.findMedianSortedArrays([], [1])
    print s.findMedianSortedArrays([1], [1])
    print s.findMedianSortedArrays([1, 5, 10, 12], [1, 2, 3, 4, 5])
