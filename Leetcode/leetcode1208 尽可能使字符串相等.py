'''
Author: Puffrora
Date: 2021-02-05 15:09:54
LastModifiedBy: Puffrora
LastEditTime: 2021-02-05 15:28:23
'''


class Solution:
    def equalSubstring(self, s, t, maxCost):

        res = curCost = start = end = 0
        for end in range(len(s)):
            tmp = abs(ord(s[end])-ord(t[end]))
            while curCost + tmp > maxCost:
                curCost -= abs(ord(s[start])-ord(t[start]))
                start += 1
            if curCost + tmp <= maxCost:
                curCost += tmp
            res = max(res, end-start+1)
        return res
        
