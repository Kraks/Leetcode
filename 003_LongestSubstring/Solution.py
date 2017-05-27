class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = dict() # char -> last_index
        longest = 0
        start = 0
        i = 0

        while i < len(s):
            if p.has_key(s[i]) and p[s[i]] >= start:
                start = p[s[i]]+1
            longest = max(longest, i - start + 1)
            p[s[i]] = i
            i += 1
        return longest

if __name__ == "__main__":
    S = Solution()
    assert(S.lengthOfLongestSubstring("abca") == 3)
    assert(S.lengthOfLongestSubstring("bbbb") == 1)
    assert(S.lengthOfLongestSubstring("pwwkew") == 3)
    assert(S.lengthOfLongestSubstring("a") == 1)
    assert(S.lengthOfLongestSubstring("") == 0)
    print(S.lengthOfLongestSubstring("aab"))
    print(S.lengthOfLongestSubstring("tmmzuxt"))
