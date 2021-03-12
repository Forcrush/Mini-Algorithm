'''
Author: Puffrora
Date: 2021-03-12 19:20:48
LastModifiedBy: Puffrora
LastEditTime: 2021-03-12 20:22:59
'''


# 不加记忆化 时间复杂度 O(n^0.788)
# 加记忆化 时间复杂度 O(logn * logn)
"""
不加记忆化 时间复杂度证明
T(n) = T(n/2) + T(n/3) + O(1)
令 T(n) = O(n^t)
O(n^t) = O((n/2)^t) + O((n/3)^t) + O(1)
两边同时除以 O(n^t) 有 1 = (1/2)^t + (1/3)^t
t ≈ 0.788

加记忆化 时间复杂度证明
对于正整数 n, x, y 有 ⌊⌊n/x⌋/y⌋ = ⌊n/(xy)⌋ = ⌊⌊n/y⌋/x⌋
只有所有满足 i = ⌊n/(2^x * 3^y)⌋ 的 find(i) 值才会被计算
根据 i = ⌊n/(2^x * 3^y)⌋ 有 x ≤ ⌊log2(n)⌋ 以及  y ≤ ⌊log3(n)⌋
因此我们可以估计出需要计算的 find(i) 的个数不超过 
⌊log2(n)⌋ * ⌊log3(n)⌋ = O(logn * logn)
"""
class Solution:
    def minDays(self, n: int) -> int:
        
        from functools import lru_cache

        @lru_cache
        def find(num):
            if num <= 1: return num
            
            """
            * 在任意一次操作 2 之前最多只会有 1 次操作 1
            * 在任意一次操作 3 之前最多只会有 2 次操作 1
            * 除了最后的一次操作 1 之外其余连续的操作 1 之后都会有操作 2 或 3, 即 find(1) = 1
            """
            return min(num % 2 + 1 + find(num//2), num % 3 + 1 + find(num//3))
    
        return find(n)


# 时间复杂度 O((logn)^2 * loglogn)
# 空间复杂度 O((logn)^2)
# 对于节点数为 n'且边数为 m'的图，使用优先队列优化的 Dijkstra 算法的时间复杂度为 O((n'+m')logm') 代入 n' = m' = O((logn)^2)
"""
我们也可以将方法一中的思路抽象成一个「最短路」问题，即
图 G 中有若干个节点，每个节点表示着一个数。根据方法一，每个节点对应着一个 ⌊n/(2^x * 3^y)⌋ 节点数为 O((logn)^2)
图 G 中有若干条有向边，如果某个节点表示的数为 i，那么 i 到 ⌊i/2⌋ 有一条权值为 i % 2 + 1 的有向边
i 到 ⌊i/3⌋ 有一条权值为 i % 3 + 1 的有向边，边数也为 O((logn)^2)
我们需要求出 n 对应的节点到 1 对应的节点的最短路径的长度
"""
class Solution2:
    def minDays(self, n: int) -> int:

        import heapq

        q = [(0, n)]
        visited = set()
        res = 0

        while True:
            days, rest = heapq.heappop(q)
            if rest in visited:
                continue
            visited.add(rest)
            if rest == 1:
                res = days + 1
                break
            heapq.heappush(q, (days + rest % 2 + 1, rest // 2))
            heapq.heappush(q, (days + rest % 3 + 1, rest // 3))

        return res


# A*
class Solution3:
    def minDays(self, n: int) -> int:

        from functools import lru_cache
        import heapq, math

        @lru_cache(None)
        def getHeuristicValue(rest: float) -> int:
            return 0 if rest == 0 else int(math.log(rest) / math.log(3.0)) + 1

        q = [(getHeuristicValue(n), 0, n)]
        visited = set()
        res = 0

        while True:
            _, days, rest = heapq.heappop(q)
            if rest in visited:
                continue
            visited.add(rest)
            if rest == 1:
                res = days + 1
                break
            heapq.heappush(q, (
                days + rest % 2 + 1 + getHeuristicValue(rest // 2),
                days + rest % 2 + 1,
                rest // 2
            ))
            heapq.heappush(q, (
                days + rest % 3 + 1 + getHeuristicValue(rest // 3),
                days + rest % 3 + 1,
                rest // 3
            ))

        return res

