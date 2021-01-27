'''
Author: Puffrora
Date: 2021-01-26 20:36:14
LastModifiedBy: Puffrora
LastEditTime: 2021-01-26 20:59:57
'''


class Solution:
    def closedIsland(self, grid):
        
        from collections import deque

        row, col = len(grid), len(grid[0])
        
        def get_neighbor(x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x+dx < row and 0 <= y+dy < col:
                    yield x+dx, y+dy

        def bfs(x, y, flag):
            queue = deque([(x, y)])
            while queue:
                for _ in range(len(queue)):
                    cur_x, cur_y = queue.popleft()
                    grid[cur_x][cur_y] = flag
                    for nx, ny in get_neighbor(cur_x, cur_y):
                        if grid[nx][ny] == 0:
                            queue.append((nx, ny))

        # 把挨着边界的岛屿变成水域
        for r in range(row):
            if grid[r][0] == 0:
                bfs(r, 0, 1)
            if grid[r][col-1] == 0:
                bfs(r, col-1, 1)
        for c in range(col):
            if grid[0][c] == 0:
                bfs(0, c, 1)
            if grid[row-1][c] == 0:
                bfs(row-1, c, 1)

        for l in grid:
            print(l)
        # 寻找封闭岛屿
        flag = 2
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    bfs(r, c, flag)
                    flag += 1
        
        return flag - 2


class Solution1:
    def closedIsland(self, grid):

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        rows, cols= len(grid), len(grid[0])

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)

        count = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1

        return count
