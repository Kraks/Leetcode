start = int('A'.encode('hex'), 16)
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        num = 0
        for index, x in enumerate(reversed(s)):
            t = int(x.encode('hex'), 16) - start + 1
            if index == 0:
                num += t
            else:
                num += index * 26 * t
        return num

if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber('A')      #1
    print s.titleToNumber('Z')      #26
    print s.titleToNumber('AA')     #27
    print s.titleToNumber('BA')     #53
    print s.titleToNumber('BB')     #54

