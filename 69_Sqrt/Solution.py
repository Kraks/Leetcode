class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        return int(self.sqrtIter(1.0, x))

    def sqrtIter(self, guess, x):
        if self.goodEnough(guess, x):
            return guess
        return self.sqrtIter(self.improve(guess, x), x)
    
    def improve(self, guess, x):
        return (guess + (x / guess)) / 2
    
    def goodEnough(self, guess, x):
        return abs(guess ** 2 - x) < 0.001

s = Solution()
print s.mySqrt(4)
print s.mySqrt(6)
