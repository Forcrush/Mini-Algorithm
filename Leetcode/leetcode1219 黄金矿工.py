'''
Author: Puffrora
Date: 2021-01-25 19:08:10
LastModifiedBy: Puffrora
LastEditTime: 2021-01-25 19:42:10
'''


class Solution:
    def getMaximumGold(self, grid):

        row, col = len(grid), len(grid[0])

        def get_neighbor(i, j):
            nonlocal row, col
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i+dx < row and 0 <= j+dy < col:
                    yield i+dx, j+dy

        # 回溯
        def backtraceing(i, j, visited):
            visited.add((i, j))
            max_val = 0
            for nx, ny in get_neighbor(i, j):
                if grid[nx][ny] and (nx, ny) not in visited:
                    max_val = max(max_val, backtraceing(nx, ny, visited))
            
            # ! 需要删除避免影响另一个方向上的路线选择 反例参照 bottom example
            visited.discard((i, j))
            
            return grid[i][j] + max_val

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                v = set()
                res = max(res, backtraceing(i, j, v))

        return res


# example
print(Solution().getMaximumGold(
    [[0, 0, 0, 0, 0, 0, 32, 0, 0, 20], 
    [0, 0, 2, 0, 0, 0, 0, 40, 0, 32], 
    [13, 20, 36, 0, 0, 0, 20, 0, 0, 0], 
    [0, 31, 27, 0, 19, 0, 0, 25, 18, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 18, 0, 6], 
    [0, 0, 0, 25, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 21, 0, 30, 0, 0, 0, 0], 
    [19, 10, 0, 0, 34, 0, 2, 0, 0, 27], 
    [0, 0, 0, 0, 0, 34, 0, 0, 0, 0]]))
