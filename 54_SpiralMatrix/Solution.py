def rotate(A):
    if len(A) > 0:
        return [[line[i] for line in A] for i in reversed(range(0, len(A[0])))]
    return []

class Solution:
    def auxSpiralOrder(self, matrix, acc):
        if len(matrix) > 0:
            acc.extend(matrix[0])
            return self.auxSpiralOrder(rotate(matrix[1:]), acc)
        else: return acc

    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        return self.auxSpiralOrder(matrix, [])

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[5]]
c = [[4, 5, 6], [7, 8, 9]]
#print rotate(a)
#print rotate(b)
#print rotate(c)

s = Solution()
print s.spiralOrder(a)
