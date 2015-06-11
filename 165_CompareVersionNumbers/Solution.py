class Solution:
    def getVer(self, v):
        return map(lambda x: int(x), v.split('.'))
    def verMinus(self, x, y):
        assert len(x) == len(y)
        res = []
        for i in range(0, len(x)):
            res.append(x[i] - y[i])
        return res

    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, v1, v2):
        v1 = self.getVer(v1)
        v2 = self.getVer(v2)
        s = max(len(v1), len(v2))
        if len(v1) < len(v2): v1.extend([0 for i in range(0, s-len(v1))])
        elif len(v2) < len(v1): v2.extend([0 for i in range(0, s-len(v2))])
        res = filter(lambda x: x != 0, self.verMinus(v1, v2))
        if len(res) == 0: return 0
        if res[0] > 0: return 1
        else: return -1
