'''
Author: Puffrora
Date: 2020-10-16 20:50:12
LastModifiedBy: Puffrora
LastEditTime: 2020-10-16 21:18:27
'''


class Solution:
    def orangesRotting(self, grid):

        def neighbor(i, j):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+dx < len(grid) and 0 <= j+dy < len(grid[0]):
                    yield i+dx, j+dy

        bad, good = 0, 0
        queue = []
        turn = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bad += 1
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    good += 1
        
        if good == 0: return 0
        if bad == 0: return -1
        
        infect = 0
        while queue:
            turn += 1
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                for nr, nc in neighbor(r, c):
                    if grid[nr][nc] == 1:
                        infect += 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
        
        # 因为 queue 里面会保存最后一轮被感染的橘子 所以 turn 需要减一轮
        return -1 if infect != good else turn - 1


