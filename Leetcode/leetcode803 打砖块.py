'''
Author: Puffrora
Date: 2020-11-11 13:01:50
LastModifiedBy: Puffrora
LastEditTime: 2020-11-11 15:08:01
'''


# 并查集
class Disjoint_Set:
    def __init__(self, R, C):
        # R * C is a virtual square, isn't a grid square
        self.parent = list(range(R * C + 1))
        self.rank = [0] * (R * C + 1)
        self.size = [1] * (R * C + 1)

    def find(self, x):
        if self.parent[x] != x:
            # 路径压缩
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
    
    def top(self):
        # Size of component at ephemeral "source" node at index R*C,
        # minus 1 to not count the source itself in the size
        # s == R * C
        s = len(self.size) - 1
        return self.size[self.find(s)] - 1


# 时间复杂度：O(N * Q * α(N * Q))
# 空间复杂度：O(N)
# . 其中 N = R * C 是网格的大小，Q 是操作数目，α 是反阿克曼函数（Inverse-Ackermann Function）
class Solution:
    def hitBricks(self, grid, hits):
        R, C = len(grid), len(grid[0])

        def index(r, c):
            return r * C + c

        def neighbor(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        tmp = [row[:] for row in grid]
        for i, j in hits:
            tmp[i][j] = 0
        
        # ! 先删除 hits 中的点 进行并查集初始化
        ds = Disjoint_Set(R, C)
        for r, row in enumerate(tmp):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        ds.union(i, R*C)
                    if r and tmp[r-1][c]:
                        ds.union(i, index(r-1, c))
                    if c and tmp[r][c-1]:
                        ds.union(i, index(r, c-1))

        # ! 逆序加入 hits 中的点
        res = []
        for r, c in hits[::-1]:
            pre = ds.top()
            if grid[r][c] == 0:
                res.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbor(r, c):
                    if tmp[nr][nc]:
                        ds.union(i, index(nr, nc))
                if r == 0:
                    ds.union(i, R*C)
                tmp[r][c] = 1
                res.append(max(0, ds.top()-pre-1))
        
        return res[::-1]


