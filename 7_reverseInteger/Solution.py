## Some comment on integer overflows:
#  Actually, in Python, the max number of a Integer is system dependented,
#  testing the overflow behavior is non-sense in Python.

class Solution:
    def __auxReverse(self, x):
        rev = reversed(str(x))
        return int("".join([s for s in rev]))

    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
            return 0 - self.__auxReverse(abs(x))
        return self.__auxReverse(x)

if __name__ == "__main__":
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(1000)
    print s.reverse(1000000003)
