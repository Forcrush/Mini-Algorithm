'''
Author: Puffrora
Date: 2020-10-19 22:40:43
LastModifiedBy: Puffrora
LastEditTime: 2020-10-19 22:53:34
'''


"""
定义 solve(i, j) 表示将开区间 (i, j) 内的位置全部填满气球能够得到的最多硬币数。
由于是开区间，因此区间两端的气球的编号就是 i 和 j，对应着 val[i] 和 val[j]
我们枚举开区间 (i, j) 内的全部位置 mid，令 mid 为当前区间第一个添加的气球，
该操作能得到的硬币数为 val[i] * val[mid] * val[j]。同时我们递归地计算分割出
的两区间对 solve(i, mid) 和 solve(mid, j) 的贡献，这三项之和的最大值，
即为 )solve(i, j) 的值。
"""
# 记忆化搜索
# 时间复杂度 O(N^3)
# 空间复杂度 O(N^2)
class Solution:
    def maxCoins(self, nums):
        from functools import lru_cache
        
        val = [1] + nums + [1]

        # ! 缓存式记忆化搜索
        @lru_cache(None)
        def solve(left, right):
            if left >= right -1: return 0

            res = 0
            for k in range(left+1, right):
                cur = val[left] * val[k] * val[right]
                cur += solve(left, k) + solve(k, right)
                res = max(res, cur)
            
            return res
        
        return solve(0, len(nums)+1)


# DP
# 时间复杂度 O(N^3)
# 空间复杂度 O(N^2)
class Solution2:
    def maxCoins(self, nums):
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    cur = val[i] * val[k] * val[j]
                    cur += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], cur)

        return dp[0][n+1]
