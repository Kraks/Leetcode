class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        dp = [-1 for i in range(0, n+5)]
        dp[0], dp[1], dp[2] = 0, 1, 2
        return self.aux(n, dp)

    def aux(self, n, dp):
        if dp[n] != -1: return dp[n]
        else:
            dp[n] = self.aux(n-1, dp) + self.aux(n-2, dp)
            return dp[n]

s = Solution()
print s.climbStairs(5)

