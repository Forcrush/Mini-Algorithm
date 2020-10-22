'''
Author: Puffrora
Date: 2020-10-22 14:22:09
LastModifiedBy: Puffrora
LastEditTime: 2020-10-22 15:16:00
'''


class Solution:
    def findLongestWord(self, s, d):
        
        def is_subseqence(a, b):
            if len(a) < len(b): return False
            i, j = 0, 0
            for i in range(len(a)):
                if a[i] == b[j]:
                    j += 1
                    if j == len(b):
                        return True
            return False
        
        res = ''
        for w in d:
            if is_subseqence(s, w):
                if len(w) > len(res):
                    res = w
                elif len(w) == len(res):
                    res = w if w < res else res
        
        return res