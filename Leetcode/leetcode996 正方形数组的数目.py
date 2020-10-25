'''
Author: Puffrora
Date: 2020-10-24 19:09:00
LastModifiedBy: Puffrora
LastEditTime: 2020-10-24 19:57:41
'''


class Solution:
    def numSquarefulPerms(self, A):

        from collections import defaultdict
        from functools import lru_cache
        
        # 判断完全平方数  1 + 3 + 5 + ... + (2n-1) = n^2
        def is_squared_num(x):
            if x == 1: return True
            sub = 1
            while True:
                if x == 0: return True
                if x < 0: return False
                x -= sub
                sub += 2

        def square_edge(a, b):
            return is_squared_num(a+b)
        
        def factor(num):
            if num == 0: return 1
            return num * factor(num-1)

        graph = defaultdict(list)
        for i, node in enumerate(A):
            for j in range(i):
                if square_edge(node, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)
                    
        # 找到图中的哈密顿路径数量
        @lru_cache(None)
        def dfs(node, path):
            if path == (1 << len(A)) - 1: return 1

            res = 0
            for neighbor in graph[node]:
                if (path >> neighbor) & 1 == 0:
                    res += dfs(neighbor, path | (1 << neighbor))

            return res

        res = sum(dfs(i, 1<<i) for i in range(len(A)))
        cnt = defaultdict(int)
        for num in A:
            cnt[num] += 1
            
        # 对于 A 中拥有相同值的节点我们会重复计算。考虑这个因素，对于 A 中的值 x，如果 A 中包含 k 个值为 x 的节点，我们令最终答案除以 k!
        for k, v in cnt.items():
            res //= factor(v)
        
        return res
        