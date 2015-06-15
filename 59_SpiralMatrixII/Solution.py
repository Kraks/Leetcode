# A collection of solutions in variety languages
# http://rosettacode.org/wiki/Spiral_matrix

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        #m = [[y for y in range(i, i+n)] for i in range(1, n*n+1, n)]
        m = [[None] * n for i in range(0, n)]
        x, y, dx, dy = 0, 0, 0, 1

        for i in xrange(1, n*n+1):
            m[x][y] = i
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and m[nx][ny] == None:
                x, y = nx, ny
            else:
                dx, dy = dy, -dx
                x, y = x + dx, y + dy
        return m

s = Solution()
print s.generateMatrix(3)
print s.generateMatrix(4)
