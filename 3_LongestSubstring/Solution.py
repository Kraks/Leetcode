class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0

        d = dict()
        longest = 0
        start = 0
        i = 0

        while i < len(s):
            if d.has_key(s[i]) and d[s[i]] >= start:
                start = d[s[i]]+1
            longest = max(longest, i - start + 1)
            d[s[i]] = i
            i += 1
        return longest

    def lengthOfLongestSubstringNaive(self, s):
        g = 0
        for i in range(len(s)):
            d = dict()
            longest = 0
            for x in s[i:]:
                if d.has_key(x): 
                    if longest > g: g = longest
                    break
                longest += 1
                d[x] = None
            if longest > g: g = longest
        return g

if __name__ == "__main__":
    S = Solution()
    assert(S.lengthOfLongestSubstring("abca") == 3)
    assert(S.lengthOfLongestSubstring("bbbb") == 1)
    assert(S.lengthOfLongestSubstring("pwwkew") == 3)
    assert(S.lengthOfLongestSubstring("a") == 1)
    assert(S.lengthOfLongestSubstring("") == 0)
    print(S.lengthOfLongestSubstring("aab"))
    print(S.lengthOfLongestSubstring("tmmzuxt"))
