'''
Author: Puffrora
Date: 2021-01-29 16:34:58
LastModifiedBy: Puffrora
LastEditTime: 2021-01-29 16:50:54
'''


# MinMax 算法
# 时间复杂度 O(N^3)
# 空间复杂度 O(N^2)
# https://leetcode-cn.com/problems/cat-and-mouse/solution/mao-he-lao-shu-by-leetcode/
class Solution:
    def catMouseGame(self, graph):

        from collections import defaultdict, deque

        N = len(graph)

        # What nodes could paly their turn to arrive at node(m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 1
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 2
        
        DRAW, MOUSE, CAT = 0, 1 ,2
        color = defaultdict(int)

        # the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[(m, c, 1)] = len(graph[m])
                degree[(m, c, 2)] = len(graph[c]) - (0 in graph[c])

        # enqueue all colored nodes
        queue = deque([])
        for i in range(N):
            for t in [1, 2]:
                color[(0, i, t)] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[(i, i, t)] = CAT
                    queue.append((i, i, t, CAT))

        # perlocate
        while queue:
            # for nodes are uncolored
            i, j, t, c = queue.popleft()
            # for every parent of node (i, j, t)
            for i2, j2, t2 in parents(i, j, t):
                # is this parent is uncolored
                if color[(i2, j2, t2)] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c:
                        color[(i2, j2, t2)] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[(i2, j2, t2)] -= 1
                        if degree[(i2, j2, t2)] == 0:
                            color[(i2, j2, t2)] = 3 - t2
                            queue.append((i2, j2, t2, 3-t2))


        return color[(1, 2, 1)]


print(Solution().catMouseGame(
    [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
