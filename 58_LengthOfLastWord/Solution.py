class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        arr = filter(lambda x: len(x) > 0, s.split(' '))
        if len(arr) > 0: return len(arr[len(arr)-1])
        return 0
