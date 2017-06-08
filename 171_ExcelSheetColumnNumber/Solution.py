start = ord('A')
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        num = 0
        for index, x in enumerate(reversed(s)):
            t = ord(x) - start + 1
            num += t * pow(26, index)
        return num

if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber('A')      #1
    print s.titleToNumber('Z')      #26
    print s.titleToNumber('AA')     #27
    print s.titleToNumber('BA')     #53
    print s.titleToNumber('BB')     #54
    print s.titleToNumber('AAA')    #703
    print s.titleToNumber('AJHX')   #24568

