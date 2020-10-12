'''
Author: Puffrora
Date: 2020-10-08 23:23:32
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 23:35:37
'''


class Solution:
    def nextGreaterElement(self, n):
        s = list(str(n))

        increse = True
        for i in range(len(s)-2, -1, -1):
            if s[i] < s[i+1]:
                increse = False
                break
        
        if increse:
            return -1
        
        pos = i
        for j in range(i+1, len(s)):
            if s[j] > s[i]:
                pos = j
        
        s[pos], s[i] = s[i], s[pos]
        res = s[:i+1] + s[i+1:][::-1]
        res_num = int("".join(res))
        
        return res_num if res_num <= 2147483647 else -1
    
