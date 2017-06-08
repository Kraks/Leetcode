table = {'last': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        res = 0
        for pre, next in zip(s, s[1:]):
            if table[next] > table[pre]:
                res -= table[pre]
            else:
                res += table[pre]
        res += table[s[len(s)-1]]
        return res
        
