class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        seg = filter(lambda x: len(x)>0, s.split(" "))
        seg.reverse()
        return " ".join(seg)

s = Solution()
print s.reverseWords("the sky is blue")
