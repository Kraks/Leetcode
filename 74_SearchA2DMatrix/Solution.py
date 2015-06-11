class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        for x, y in zip(matrix[:-1], matrix[1:]):
            if target >= x[0] and target < y[0]:
                return search(x, target) != -1
        return search(matrix[-1], target) != -1

def search(nums, key):
    lo = 0 
    hi = len(nums)-1
    while lo <= hi: 
        mid = lo + (hi - lo)/2
        if key < nums[mid]: hi = mid-1
        elif key > nums[mid]: lo = mid+1
        else: return mid 
    return -1

if __name__ == "__main__":
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    s = Solution()
    print s.searchMatrix(m, 20)
