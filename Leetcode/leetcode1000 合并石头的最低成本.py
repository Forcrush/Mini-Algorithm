'''
Author: Puffrora
Date: 2020-10-25 22:45:19
LastModifiedBy: Puffrora
LastEditTime: 2020-10-25 23:07:16
'''


"""
dp[i][j]代表从 i 到 j 合并为最少堆的最小代价
"""
class Solution:
    def mergeStones(self, stones, K):
        if (len(stones) - 1) % (K - 1): return -1
        prefix = [0] * (len(stones) + 1)
        for i in range(1, len(stones)+1):
            prefix[i] = prefix[i-1] + stones[i-1]
        
        dp = [[0 for _ in range(len(stones))] for _ in range(len(stones))]
        # m 是合并区间长度 至少为 K
        for m in range(K, len(stones)+1):
            for i in range(len(stones)-m+1):
                dp[i][i+m-1] = min(dp[i][k]+dp[k+1][i+m-1] for k in range(i, i+m-1, K-1))
                # ! 当(m-1) % (K-1) == 0时，可以也必须进行合并成一堆的工作，此时用 prefix 计算合并代价
                dp[i][i+m-1] += prefix[i+m] - prefix[i] if (m - 1) % (K - 1) == 0 else 0
                
        return dp[0][len(stones)-1]