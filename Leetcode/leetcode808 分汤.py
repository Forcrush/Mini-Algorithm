'''
Author: Puffrora
Date: 2020-11-14 13:24:39
LastModifiedBy: Puffrora
LastEditTime: 2020-11-14 13:52:08
'''


class Solution:
    def soupServings(self, N):

        from functools import lru_cache


        # ! N >= 6000 时，所求概率已经大于 0.999999
        if N >= 6000: return 1

        @lru_cache(None)
        def distribute(curA, curB):
            if not curA and not curB:
                return 0.5
            if not curA:
                return 1
            if not curB:
                return 0
            return 0.25 * distribute(max(curA-100, 0), curB) + \
                    0.25 * distribute(max(curA-75, 0), max(curB-25, 0)) + \
                    0.25 * distribute(max(curA-50, 0), max(curB-50, 0)) + \
                    0.25 * distribute(max(curA-25, 0), max(curB-75, 0))
        
        return distribute(N, N)

