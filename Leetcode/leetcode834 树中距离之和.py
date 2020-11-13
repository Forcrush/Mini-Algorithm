'''
Author: Puffrora
Date: 2020-11-12 11:46:52
LastModifiedBy: Puffrora
LastEditTime: 2020-11-12 14:59:00
'''


# 树形 DP
# 时间复杂度 O(N)
# 空间复杂度 O(N)
# https://leetcode-cn.com/problems/sum-of-distances-in-tree/solution/shu-zhong-ju-chi-zhi-he-by-leetcode-solution/
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        
        from collections import defaultdict

        nodes = defaultdict(list)
        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        # dp[i] 记录 i 到其它点的距离之和
        dp = [0] * N
        # size[i] 记录以 i 为根的子树大小
        size = [1] * N
        # 记录结果
        res = [0] * N

        # 建立以 0 为根的树
        def dfs(cur, cur_par):
            for n in nodes[cur]:
                # ! 搜索节点不允许为当前节点的父节点
                if n != cur_par:
                    dfs(n, cur)
                    dp[cur] += dp[n] + size[n]
                    size[cur] += size[n]

        # 节点交换
        def dfs2(cur, cur_par):
            res[cur] = dp[cur]
            for n in nodes[cur]:
                # ! 交换子节点与当前节点
                if n != cur_par:
                    # ! 暂存
                    dp_cur, dp_n = dp[cur], dp[n]
                    size_cur, size_n = size[cur], size[n]

                    dp[cur] -= (dp[n] + size[n])
                    size[cur] -= size[n]
                    dp[n] += (dp[cur] + size[cur])
                    size[n] += size[cur]
                    dfs2(n, cur)

                    dp[cur], dp[n] = dp_cur, dp_n
                    size[cur], size[n] = size_cur, size_n

        dfs(0, -1)
        dfs2(0, -1)
        
        return res

