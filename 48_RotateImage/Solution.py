import copy

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        m = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(0, n):
            line = m[i]
            for j in range(0, n):
                matrix[j][0-i-1] = line[j]

s = Solution()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(m)
print m
