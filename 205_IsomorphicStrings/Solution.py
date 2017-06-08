class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dict, used = {}, {}
        for i, x in enumerate(s):
            if not dict.has_key(x):
                if used.has_key(t[i]): return False
                dict[x] = t[i]
                used[t[i]] = x
            elif not dict[x] == t[i]: return False
        return True

s = Solution()
print s.isIsomorphic('egg', 'add')
print s.isIsomorphic('foo', 'bar')
print s.isIsomorphic('paper', 'title')
print s.isIsomorphic('ab', 'aa')


