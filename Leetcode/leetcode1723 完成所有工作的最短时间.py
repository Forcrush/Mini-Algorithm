'''
Author: Puffrora
Date: 2021-03-11 09:58:22
LastModifiedBy: Puffrora
LastEditTime: 2021-03-12 08:35:34
'''


from typing import List
import time


# DFS
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        import heapq as hq

        # 贪心寻找一个次优解
        # 次优解越好 剪枝越多
        heap = [0] * k
        jobs = sorted(jobs)[::-1]
        for j in jobs:
            hq.heappush(heap, hq.heappop(heap)+j)
        res = max(heap)

        worker = [0] * k

        def dfs(j):
            nonlocal res
            
            if j == len(jobs):
                res = min(res, max(worker))
                return

            # 剪枝 第 j 个工作只能分配给前 j 个工人
            for i in range(min(k, j+1)):
                # 分配给第 i 个工人的钱大于已知最优 跳过
                if worker[i] + jobs[j] > res:
                    continue
                worker[i] += jobs[j]
                dfs(j+1)
                worker[i] -= jobs[j]

        dfs(0)

        return res


# 状态压缩 DP
# 时间复杂度 (k*3^N)
# 空间复杂度 (k*2^N)
"""
设 jobs 的长度为 N，则可以用一个 [0,2^N] 之间的整数代表 jobs 的任意一个子集
dp[i][j] 表示前 i 个工人为了完成作业子集 j 需要花费的最大工作时间的最小值
total[i] 代表每个工作子集 i 的时间和

dp[j][i]= min(max(dp[j−1][i−s], total[s]))
          s⊆i

"""
class Solution1:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        n = len(jobs)

        # 代表每个工作子集的时间和
        total = [0 for _ in range(1<<n)]
        for i in range(1, 1<<n):
            for j in range(n):
                if (i & (1 << j)) == 0:
                    continue
                remain = i - (1<<j)
                total[i] = total[remain] + jobs[j]
                break
        
        dp = [[-1 for _ in range(1<<n)] for _ in range(k)]
        for i in range(1<<n):
            dp[0][i] = total[i]
        
        """
        对于有 i 个 1 的二进制数字，需要 2^i的时间复杂度
        而有 i 个 1 的二进制数字有 C(n, i)个，所以下面这段代码的时间复杂度为 k * (∑C(n, i) * 2^i)
        由二项式定理，我们有(1+x)^n = C(n, 0)⋅x^0 + C(n, 1)⋅x^1 + C(n, 2)⋅x^2 + C(n, 3)⋅x^3 + … +C(n, n)⋅x^n，代入 x = 2，就可以得到 3^n
        """
        for i in range(1, k):
            # . 对于每个 1 11 111 1111 ... 去找它的子集
            for j in range(1<<n):
                minv = float('inf')
                # 枚举 j 的全部子集
                s = j
                while s:
                    remain = j - s
                    minv = min(minv, max(dp[i-1][remain], total[s]))
                    s = (s - 1) & j

                dp[i][j] = minv
        
        return dp[k-1][(1<<n)-1]


# 状态压缩 DP 二分搜索
# 时间复杂度 (3^N * log(Σjob[i]))
# 空间复杂度 (2^N)
"""
任意给定一个整数 limit，我们能够求出当每个工人的工作时间都不超过 limit 时，最少需要多少个工人
所需工人的数量为 limit 的函数，设为 f(limit)。不难发现， limit 越大，f(limit) 就越小
（因为可以尽可能地将任务分配给同一个工人）。因此，f(limit) 是一个单调递减的函数。
由于工人数量为 k，有 f(limit)≤k 因此我们利用二分搜索的方法可以找到满足 f(limit)≤k 的最小 limit 值

dp[i] 为完成作业子集 i 最少需要的工人数量
dp[i]= min(dp[i−s]+1)
       s⊆i
       s.t. total[s]≤limit

"""
class Solution2:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        n = len(jobs)

        # 代表每个工作子集的时间和
        total = [0 for _ in range(1 << n)]
        for i in range(1, 1 << n):
            for j in range(n):
                if (i & (1 << j)) == 0:
                    continue
                remain = i - (1 << j)
                total[i] = total[remain] + jobs[j]
                break
        
        # 二分搜索上下界
        l, r = max(jobs), sum(jobs)
        while l < r:
            mid = (l + r) // 2
            dp = [float('inf') for _ in range(1<<n)]
            dp[0] = 0
            for i in range(1<<n):
                s = i
                while s:
                    if total[s] <= mid:
                        dp[i] = min(dp[i], dp[i-s]+1)
                    s = (s - 1) & i
            
            if dp[(1<<n)-1] <= k:
                r = mid
            else:
                l = mid + 1

        return l


# ? 就TM离谱
# 模拟退火法
class Solution3:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        import random, math

        n = len(jobs)
        final_res = float('inf')
        worker = [0 for _ in range(k)]

        def cal():
            nonlocal final_res
            for i in range(k):
                worker[i] = 0

            for i in range(n):
                w = 0
                for j in range(1, k):
                    if worker[j] < worker[w]:
                        w = j
                worker[w] += jobs[i]
            
            res = max(worker)
            final_res = min(final_res, res)

            return res 

        def simulate_anneal():
            random.shuffle(jobs)

            t = 1e4
            while (t := t*0.95) > 1e-4:
                a, b = random.randint(0, n-1), random.randint(0, n-1)
                res1 = cal()
                jobs[a], jobs[b] = jobs[b], jobs[a]
                res2 = cal()
                diff = res2 - res1
                if math.exp(min(-diff/t, 1)) > random.random():
                    continue
                jobs[a], jobs[b] = jobs[b], jobs[a]


        for _ in range(100):
            simulate_anneal()
        
        return final_res


t = time.time()
print(Solution().minimumTimeRequired([685, 314, 222, 532, 411, 882, 724, 851, 649, 161, 100, 540], 8))
print(f'Time cost: {time.time()-t}s')
t = time.time()
print(Solution1().minimumTimeRequired([685, 314, 222, 532, 411, 882, 724, 851, 649, 161, 100, 540], 8))
print(f'Time cost: {time.time()-t}s')
t = time.time()
print(Solution2().minimumTimeRequired([685, 314, 222, 532, 411, 882, 724, 851, 649, 161, 100, 540], 8))
print(f'Time cost: {time.time()-t}s')
t = time.time()
print(Solution3().minimumTimeRequired([685, 314, 222, 532, 411, 882, 724, 851, 649, 161, 100, 540], 8))
print(f'Time cost: {time.time()-t}s')
