'''
Author: Puffrora
Date: 2020-10-17 23:43:01
LastModifiedBy: Puffrora
LastEditTime: 2020-10-18 00:02:23
'''


"""
因为节点和边可重复通过 利用经过的节点顺序来储存路径会导致存储空间指数上升
因此利用 bit 位来记录路径， 因为题目最多有 12 个节点， 状态数最多为 2^12
"""
# 时间复杂度 O(N * 2^N)
# 空间复杂度 O(N * 2^N)
class Solution:
    def shortestPathLength(self, graph):
        from collections import deque, defaultdict

        N = len(graph)
        queue = deque()
        dist = defaultdict(lambda: float('inf'))
        for x in range(N):
            queue.append((1 << x, x))
            dist[(1 << x, x)] = 0

        while queue:
            path, node = queue.popleft()
            if path == 2**N - 1:
                return dist[(path, node)]
            for child in graph[node]:
                new_path = path | 1 << child
                if dist[(path, node)] + 1 < dist[(new_path, child)]:
                    dist[(new_path, child)] = dist[(path, node)] + 1
                    queue.append(((new_path, child)))


