'''
Author: Puffrora
Date: 2020-12-08 17:59:08
LastModifiedBy: Puffrora
LastEditTime: 2020-12-08 18:04:25
'''


class Solution:
    def numSubarrayBoundedMax(self, A, L, R):

        # 计算最大值不超过 K 的连续子数组个数
        def atMostK(k):
            res, w = 0, 0
            for n in A:
                if n <= k: w += 1
                else: w = 0
                res += w
            return res
        
        return atMostK(R) - atMostK(L-1)
