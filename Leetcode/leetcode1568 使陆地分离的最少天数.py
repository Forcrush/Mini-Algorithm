'''
Author: Puffrora
Date: 2021-03-13 13:07:03
LastModifiedBy: Puffrora
LastEditTime: 2021-03-13 15:31:32
'''



from typing import List


# 时间复杂度 O(row^2 * col^2) row=len(grid) col=len(grid[0]) 
# 空间复杂度 O(row*col)
"""
每个格子最多会有四条边和其他格子相连。在边上的格子最多有三条边。在角上的最多有两条边。
无论岛屿长成什么样子，肯定是会有角的，所以最多只需删除两次
"""
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def get_neighbor(x, y):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    yield x+dx, y+dy

        # 判断当前是否存在分离陆地
        def check():
            queue = []
            all_land = sum([sum(r) for r in grid])
            for i in range(m):
                if queue:
                    break
                for j in range(n):
                    if grid[i][j]:
                        queue.append((i, j))
                        break

            # BFS
            visited = set(queue)
            search_land = len(visited)
            while queue:
                for _ in range(len(queue)):
                    curx, cury = queue.pop(0)
                    for nx, ny in get_neighbor(curx, cury):
                        if grid[nx][ny] and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                            search_land += 1
            
            if all_land == 0:
                return True
            if search_land != all_land:
                return True
            return False
        
        # 一开始就存在分离陆地或者全是海洋
        if check():
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    if check():
                        return 1
                    grid[i][j] = 1
        
        return 2


# 时间复杂度 O(row*col) row=len(grid) col=len(grid[0])
# 空间复杂度 O(row*col)
"""
Tarjan算法 找割点
割点存在的两种情况
1. x 是非root节点 && 有儿子 && low[x的儿子] >= dfn[x]
2. x 是root节点 && 有儿子 && 儿子数量 >= 2
"""
class Solution2:
    def minDays(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def get_neighbor(x, y):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    yield x+dx, y+dy
        
        land = 0

        # 节点重标号
        relabel = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    relabel[i*n+j] = land
                    land += 1

        if land == 0: return 0
        if land == 1: return 1
        
        # 储存图
        G = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    land += 1
                    G[relabel[i*n+j]] = []
                    for nx, ny in get_neighbor(i, j):
                        if grid[nx][ny]:
                            G[relabel[i*n+j]].append(relabel[nx*n+ny])
        
        # 搜索节点计数
        count = -1
        # 节点数
        N = len(G)
        # 记录回溯值 即能到此点的最小序号点
        low = [-1] * N
        # 记录 dfs 中的时间戳
        dfn = [-1] * N
        # 记录节点的父节点
        parent = [-1] * N
        # 记录找到的割点
        cutting_vertices = []
        # 记录找到的连通分量数
        connected_components = 0

        # tarjan算法求割点
        def tarjan_getCuttingVertex(u, par, cvs):
            nonlocal count
            count += 1
            low[u] = count
            dfn[u] = count
            parent[u] = par
            child = 0
            iscv = False

            for v in G[u]:
                if dfn[v] == -1:
                    child += 1
                    tarjan_getCuttingVertex(v, u, cvs)
                    low[u] = min(low[u], low[v])
                    if not iscv and par != -1 and low[v] >= dfn[u]:
                        cvs.append(u)
                        iscv = True
                elif v != parent[u]:
                    low[u] = min(low[u], dfn[v])
            
            if not iscv and par == -1 and child >= 2:
                cvs.append(u)
                
        for i in range(N):
            if dfn[i] == -1:
                connected_components += 1
                tarjan_getCuttingVertex(i, -1, cutting_vertices)
        
        # 如果连通分量数大于1 说明存在分离陆地
        if connected_components > 1: return 0
        # 如果能找到割点 只需消除割点一次
        if cutting_vertices:
            return 1
        # 如果不能找到割点 需要消除两次
        return 2

