'''
Author: Puffrora
Date: 2021-01-25 22:36:24
LastModifiedBy: Puffrora
LastEditTime: 2021-01-25 23:26:21
'''


class Solution:
    def minPushBox(self, grid):

        from collections import deque

        row, col = len(grid), len(grid[0])
        tar, box, player = None, None, None
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'T':
                    tar = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'B':
                    box = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'S':
                    player = (i, j)
                    grid[i][j] = '.'
                if tar and box and player:
                    break
                
        def get_neighbor(cur_box):
            nonlocal row, col
            x, y = cur_box
            res = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x+dx < row and 0 <= y+dy < col and grid[x+dx][y+dy] == '.':
                    res.append((x+dx, y+dy))
            return res

        def get_next_state(cur_box, cur_player):
            neighbors = get_neighbor(cur_box)

            q1 = deque([cur_player])
            reachable = []
            visited = set([cur_player])
            while q1:
                for _ in range(len(q1)):
                    x, y = q1.popleft()
                    if (x, y) in neighbors:
                        reachable.append((x, y))
                    
                    for nx, ny in get_neighbor((x, y)):
                        if (nx, ny) not in visited and (nx, ny) != cur_box:
                            visited.add((nx, ny))
                            q1.append((nx, ny))
            
            next_state = []
            bx, by = cur_box
            for rx, ry in reachable:
                symmetry_x, symmetry_y = 2 * bx - rx, 2 * by - ry
                if 0 <= symmetry_x < row and 0 <= symmetry_y < col and grid[symmetry_x][symmetry_y] == '.':
                    next_state.append(((symmetry_x, symmetry_y), cur_box))
            return next_state


        queue = deque([(box, player)])
        seen = set([(box, player)])
        step = -1
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur_box, cur_player = queue.popleft()
                if cur_box == tar:
                    return step
                
                for n_box, n_player in get_next_state(cur_box, cur_player):
                    if (n_box, n_player) not in seen:
                        seen.add((n_box, n_player))
                        queue.append((n_box, n_player))
        
        return -1


