'''
Author: Puffrora
Date: 2021-01-24 10:39:36
LastModifiedBy: Puffrora
LastEditTime: 2021-01-24 11:25:49
'''


class Solution:
    def shortestPath(self, grid, k):
        
        m, n = len(grid), len(grid[0])
        from collections import deque

        if m == 1 and n == 1:
            return 0
            
        if k >= m + n - 2:
            return m + n - 2

        visited = set([(0, 0, k)])
        queue = deque([(0, 0, k)])

        def get_neighbor(i, j):
            nonlocal m, n
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i+dx < m and 0 <= j+dy < n:
                    yield i+dx, j+dy

        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y, cur_k = queue.popleft()
                for nx, ny in get_neighbor(x, y):
                    if grid[nx][ny] == 0 and (nx, ny, cur_k) not in visited:
                        if (nx, ny) == (m-1, n-1):
                            return step
                        queue.append((nx, ny, cur_k))
                        visited.add((nx, ny, cur_k))
                    if grid[nx][ny] == 1 and cur_k > 0 and (nx, ny, cur_k-1) not in visited:
                        queue.append((nx, ny, cur_k-1))
                        visited.add((nx, ny, cur_k-1))
        
        return -1
