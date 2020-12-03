'''
Author: Puffrora
Date: 2020-11-13 15:58:52
LastModifiedBy: Puffrora
LastEditTime: 2020-11-14 11:13:41
'''


class Solution:
    def largestIsland(self, grid):

        from collections import defaultdict

        tmp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        cnt = 1
        island_dic = defaultdict(int)

        def neighbor(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    yield nr, nc

        def bfs(r, c, cnt):
            tmp[r][c] = cnt
            island_dic[cnt] += 1
            for nr, nc in neighbor(r, c):
                if grid[nr][nc] and not tmp[nr][nc]:
                    bfs(nr, nc, cnt)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and not tmp[r][c]:
                    bfs(r, c, cnt)
                    cnt += 1
        
        # 只有一个岛
        if len(island_dic) == 1:
            if island_dic[1] == len(grid) * len(grid[0]):
                return island_dic[1]
            else:
                return island_dic[1] + 1
        
        res = 0
        # 多个岛
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    around = set()
                    for nr, nc in neighbor(r, c):
                        if tmp[nr][nc]:
                            around.add(tmp[nr][nc])
                    cur = 0
                    for i in around:
                        cur += island_dic[i]
                    
                    res = max(res, cur+1)

        return res
