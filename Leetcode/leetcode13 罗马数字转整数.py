class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        if len(s) == 1:
            return dic[s]
        res = 0
        for i in range(len(s)-1):
            res += dic[s[i]] if dic[s[i+1]] <= dic[s[i]] else -1 * dic[s[i]]
        return res + dic[s[-1]]