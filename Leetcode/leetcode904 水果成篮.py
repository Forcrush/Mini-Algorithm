'''
Author: Puffrora
Date: 2020-12-08 21:48:56
LastModifiedBy: Puffrora
LastEditTime: 2020-12-08 21:57:29
'''


class Solution:
    def totalFruit(self, tree):

        # 有 k 个篮子时能摘到最多的水果数
        def getTree(k):
            from collections import defaultdict

            window = defaultdict(int)
            start, res = 0, 0
            for end in range(len(tree)):
                if window[tree[end]] == 0: k -= 1
                window[tree[end]] += 1
                
                while k < 0:
                    if window[tree[start]] == 1: k += 1
                    window[tree[start]] -= 1
                    start += 1
                
                res = max(res, end-start+1)
            
            return res
        
        return getTree(2)

